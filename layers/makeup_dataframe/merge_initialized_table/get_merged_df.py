import pandas as pd


def get_merged_df(df, init_df, val_col):
    """
    融合真实df和补充df，用真实df中的VALUE覆盖掉补充df中的VALUE返回融合后的df
    """
    on = list(df.columns)
    on.remove(val_col)
    # merge_df = pd.merge(full_df, real_df, how="outer", on=on)
    try:
        # 如果直接merge出错，说明出现了int64和object不能merge的情况，直接全部变成字符串
        merged_df = pd.merge(init_df, df, how="left", on=on, suffixes=("_x", ""))
    except Exception as e:
        init_df[on] = init_df[on].astype("str")
        df[on] = df[on].astype("str")
        # df[val_col] = df[val_col].astype("float")
        # init_df[val_col] = init_df[val_col].astype("float")
        merged_df = pd.merge(init_df, df, how="left", on=on, suffixes=("_x", ""))
    merge_df = merged_df.drop([val_col+'_x'], axis=1)
    return merge_df
