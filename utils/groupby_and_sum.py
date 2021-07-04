import pandas as pd


def groupby_and_sum(data, value):
    df = pd.DataFrame(data)
    groupby_list = df.columns.to_list()
    groupby_list.remove(value)
    grouped = df.groupby(groupby_list, as_index=False)[value].sum()

    return grouped
    # print(grouped)