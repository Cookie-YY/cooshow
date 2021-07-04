import os

import pandas as pd


def get_relation_valuelist(re_col_file, dataframe):
    from app import app
    INITIALIZATION_FILE_PATH = app.config["INITIALIZATION_FILE_PATH"]
    re_list = []  # [[["北京市", "海淀区"], ["北京市", "朝阳区"]], [["体育": "足球"], ["体育", "篮球"]]]
    re_cols = []  # 带有关系的列名，并保持顺序，可能跨表
    for file_name, re_df_cols in re_col_file.items():
        re_df = pd.read_csv(os.path.join(INITIALIZATION_FILE_PATH, file_name), sep=app.config.get("INITIALIZATION_FILE_SEP", "\t"))
        re_cols.extend(re_df_cols)

        # 筛选符合条件的数据
        filter_cols = [i for i in dataframe if i in re_df.columns]
        for col in filter_cols:
            re_df[re_df_cols] = re_df[re_df_cols][re_df[col] == dataframe[col]]
        res = re_df[re_df_cols].dropna()

        # 将这个df中所需要的列的取值，去重后放到全局取值中
        tmp_re_list = [list(row) for _, row in res.iterrows()]
        from utils.get_unilist import get_unilist
        re_list.append(get_unilist(tmp_re_list))

    return re_list, re_cols


def get_norelation_valuelist(dataframe):
    from app import app
    from flask import g
    from utils.init_date_valuelist import init_date_valuelist
    init_date_valuedict = init_date_valuelist(dataframe)
    INITIALIZATION = app.config.get("INITIALIZATION")
    modified_initialization = g.get("modified_initialization", {})
    INITIALIZATION.update(init_date_valuedict)           # 由于指定时间范围导致的取值变化
    INITIALIZATION.update(modified_initialization)       # 由于param_trans导致的取值变化
    INITIALIZATION = get_random_or_zero(INITIALIZATION)

    return INITIALIZATION


def get_random_or_zero(df_dict):
    from app import app
    value_dict = {k: [0] for k, v in df_dict.items() if len(v) == 1 and "VALUE_" in str(v[0])}
    random_value_dict = {}

    if app.config.get("RANDOM_OR_ZERO", "ZERO") == "RANDOM":
        efficient_digits = app.config.get("EFFICIENT_DIGITS", 4)
        random_int_lower = app.config.get("RANDOM_INT_LOWER", 100)
        random_int_upper = app.config.get("RANDOM_INT_UPPER", 999)
        random_float_lower = app.config.get("RANDOM_FLOAT_LOWER", 0)
        random_float_upper = app.config.get("RANDOM_FLOAT_UPPER", 1)
        random_dict = {"random_int_lower": str(random_int_lower),
                       "random_int_upper": str(random_int_upper),
                       "random_float_lower": str(random_float_lower),
                       "random_float_upper": str(random_float_upper),
                       "efficient_digits": str(efficient_digits)}

        for column in value_dict:
            int_or_float = df_dict.get(column)[0]
            # int_or_float = "VALUE_FLOAT(0.5,0.8)"
            if "VALUE_FLOAT" in int_or_float:
                if "(" in int_or_float and ")" in int_or_float:
                    lower, upper = int_or_float.strip(")").split("(")[1].split(",")
                    random_dict["random_float_lower"] = lower
                    random_dict["random_float_upper"] = upper
                random_str = "round(random.uniform({random_float_lower},{random_float_upper}),{efficient_digits})".format(**random_dict)
            else:
                if "(" in int_or_float and ")" in int_or_float:
                    lower, upper = int_or_float.strip(")").split("(")[1].split(",")
                    random_dict["random_int_lower"] = lower
                    random_dict["random_int_upper"] = upper
                random_str = "random.randint({random_int_lower},{random_int_upper})".format(**random_dict)
            random_value_dict[column] = [random_str]

    return {**df_dict, **value_dict, **random_value_dict}
