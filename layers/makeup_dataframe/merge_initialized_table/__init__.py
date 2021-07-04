from layers.makeup_dataframe.merge_initialized_table.get_splited_columns import get_splited_columns
from layers.makeup_dataframe.merge_initialized_table.get_columns_valuelist import get_relation_valuelist, get_norelation_valuelist
from layers.makeup_dataframe.merge_initialized_table.get_init_df import get_init_df
from layers.makeup_dataframe.merge_initialized_table.get_merged_df import get_merged_df
from layers.makeup_dataframe.merge_initialized_table.get_random_df import fill_random_or_real


def merge_initialized_table(dataframe):
    """
    1.从df中拆出所有的列 筛出无从属关系的列和有从属关系的列 column filter
    2.根据df中的列从一个大的父子关系表中查到一个list 怎么查？读哪个文件？ 如[爷，父，子] query
    3.利用查到的list和那些无从属关系的list做笛卡尔积 拆掉内部括号 填补 返回一个df  product_unzip
    4.融合返回 merge
    5.根据value列中的NaN进行随机初始化 random_init
    """
    value = dataframe.get("value")
    df = dataframe.get("df")
    table = dataframe.get("table")  # 当需要用table判断某个字段用哪种初始化方式的时候必须传
    # 0. 初始化，获得所有独立列取值[random_or_zero] && 如果只有一列直接返回【on会为空，报错】
    INITIALIZATION = get_norelation_valuelist(dataframe)  # 加载没有联动关系的取值

    if len(df.columns) == 1:
        if df.columns[0] not in INITIALIZATION:
            return 400, f"The Column {df.columns[0]} must be registered", {}
        df[df.columns[0]] = df[df.columns[0]].apply(lambda x: fill_random_or_real(x, INITIALIZATION, df.columns[0], table))
        return 200, "success", df

    # 1. 列拆分，获得没有联动的列  和  有联动的列的集合
    no_re_col, re_col_file = get_splited_columns(df)
    # 2. 处理联动列的所有取值
    re_list, re_col = get_relation_valuelist(re_col_file, dataframe)  # re_list/re_col可能跨表存在
    # 3. 处理独立列的所有取值
    for item in no_re_col:
        if item not in INITIALIZATION:
            return 400, f"The Column {item} must be registered", {}
    no_re_list = [INITIALIZATION.get(item) for item in no_re_col]  # 获得所有独立字段的取值
    # 4. 初始化df
    init_df = get_init_df(re_list, no_re_list, re_col, no_re_col)
    # 5. 融合初始化的df和数据df
    merged_df = get_merged_df(df, init_df, value)
    # 6. 随机值处理
    merged_df[value] = merged_df[value].apply(lambda x: fill_random_or_real(x, INITIALIZATION, value, table))
    return 200, "success", merged_df
