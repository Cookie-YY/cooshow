import decimal

import pandas as pd
from datetime import datetime


def results2df_ready(results, columns):
    data = []

    # 查询结果格式转换：转成[{"column1": "value1"}, {}] 的格式
    # data = [dict(zip(result.keys(), result)) for result in results]
    for result in results:
        from utils.time_format import date2datetime
        result2dt = [date2datetime(i) for i in result]
        data.append(dict(zip(result.keys(), result2dt)))

    # 空数据填充None，方便后续排序补零
    if not data:  # 空数据需要返回初始化的0，并且是空数据
        data = [dict(zip(columns, [None] * len(columns)))]  # 返回的结果只有一行，全是None
    return data


def results2df(results, columns, apis_copy=None):  # sql模式的get_data_from_db和params_search中
    df = pd.DataFrame(results2df_ready(results, columns), columns=columns)

    # 转换decimal类型
    for col in df:
        if isinstance(df[col][0], decimal.Decimal):
            df[col] = df[col].astype(float)

    # 字段映射（网上投诉-->来信，网上信访-->来信）
    from utils.value_mapped import value_mapped
    df = value_mapped(df, apis_copy=apis_copy)

    # 时间处理
    if "day" in df.columns:
        df["day"] = df["day"].apply(lambda x: str(x).split()[0])
    if "date" in df.columns and isinstance(apis_copy, dict):
        df["date"] = df["date"].apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))
        df["date"] = df["date"].apply(lambda x: datetime.strftime(x, apis_copy.get("time_format")))
    return df


def df2results(df):
    res_list = []
    for value in df.values.tolist():
        res_one = {list(df.columns)[i]: value[i] for i in range(len(value))}
        res_list.append(res_one)
    return res_list
