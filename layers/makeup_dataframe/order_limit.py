import re
import pandas as pd


def order_limit(dataframe):
    df = dataframe["df"]
    order = dataframe.get("order")
    limit = dataframe.get("limit")

    if order:
        if order in ["desc", "asc"]:
            lx = "-" if "desc" in order else ""
            order = lx + dataframe.get("value")
        order_list = order.split(",")
        rank_col = [od.lstrip("-") for od in order_list]     # 排序字段
        rank_asc = ["-" not in od for od in order_list]      # 是否升序
        df = df.sort_values(by=rank_col, axis=0, ascending=rank_asc, inplace=False).reset_index(drop=True)
        dataframe["df"] = df

    if limit:
        if 0 < int(limit) < df.shape[0]:
            df = df.head(int(limit))
    return df


def name_stack_limit(dataframe, condition, need_limit, value):
    df = dataframe['df']
    limit_condition = dataframe.get(condition)
    limit_obj1 = re.search('\d+', limit_condition)
    limit_obj2 = re.findall('\d\+(.*)', limit_condition)
    groupe_df = df.groupby([need_limit], as_index=True)[value].sum().reset_index()
    rows = groupe_df.iloc[:, 0].size
    if limit_obj1 and limit_obj2:
        limit = limit_obj1.group()
        limit_df = groupe_df.loc[:, [need_limit]].head(int(limit))
        value_sum = ((groupe_df.tail(rows - int(limit)))[value]).sum()
        new_df = pd.merge(limit_df, df, how="inner", on=need_limit)
        rows_l = []
        for i in range(len(list(df))):
            rows_l.append(limit_obj2[0])
        df_dict = dict(zip(list(df), rows_l))
        df_dict[value] = value_sum
        new_df = new_df.append([df_dict], ignore_index=False)
        return new_df
    elif limit_obj1 and not limit_obj2:
        limit = limit_obj1.group()
        limit_df = groupe_df.loc[:, [need_limit]].head(int(limit))
        new_df = pd.merge(limit_df, df, how="inner", on=need_limit)
        return new_df
    else:
        return df
