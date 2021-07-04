from utils.get_unilist import get_trimed_list, get_unilist
import numpy as np


def groupby_and_sum(df, value):
    # df = pd.DataFrame(data)
    groupby_list = list(df.columns)
    groupby_list = get_trimed_list(value, groupby_list)  # value 指定的内容不做 groupby
    groupby_list = get_trimed_list("zb", groupby_list)   # zb 列不做 groupby
    groupby_list = get_trimed_list("tb", groupby_list)  # zb 列不做 groupby
    groupby_list = get_trimed_list("hb", groupby_list)  # zb 列不做 groupby

    # groupby 的四种情况
    # 1. value列是数字      对 groupby_list 做 groupby 对 value 做 sum
    # 2. value列是汉字      对 groupby_list 做 groupby 对 value 做 concatenate

    if df[value][0] is None:
        return df
    if np.issubdtype(df[value].dtype, np.number):  # 判断这一列是否是数字
        if groupby_list:
            grouped = df.groupby(groupby_list, as_index=False)[value].sum()
        else:
            grouped = df[value].sum()
    else:
        if groupby_list:
            grouped = df.groupby(groupby_list, as_index=True, sort=False)[value].apply(lambda x: get_unilist((x.str.cat(sep=',')).split(","))).reset_index()
        else:
            df["temp"] = 1
            grouped = df.groupby(["temp"], as_index=True, sort=False)[value].apply(lambda x: get_unilist((x.str.cat(sep=',')).split(","))).reset_index()
            grouped = grouped.drop(columns=["temp"])
    return grouped