import os

from flask import g


def get_splited_columns(dataframe):
    """
    1. 找到有关系的列
    找到有关系的列，直接把对应的关系表丢进dict{"关系表名":"（仿linux权限设计）"}，返回这个dict
    剩下的是没有关系的列 用一个list存起来直接返回
    """
    df = dataframe
    # 1. 读取配置，并转换成：
    # col_file_map = {
    #     "shij_02": "shej_02+shij_02+xj_02",
    #     "shej_02": "shej_02+shij_02+xj_02",
    #     "xj_02": "shej_02+shij_02+xj_02",
    # }
    from app import app
    INITIALIZATION_FILE_PATH = app.config.get("INITIALIZATION_FILE_PATH")
    RELATION_COLS = [i for i in os.listdir(INITIALIZATION_FILE_PATH) if "+" in i]
    # RELATION_COLS = app.config.get("RELATION_COLS", [])  # ["shej_02+shij_02+xj_02", "shej_02+shij_02+xj_02"]
    RELATION_COLS = {col: table for table in RELATION_COLS for col in table.split("+")}

    # 2. 遍历所有列，拆分有联动和没有联动的列
    before_splited_columns = list(df.columns).copy()
    re_col_file = {}  # 最终有联动的列的字典
    for column in df.columns:
        if column in RELATION_COLS and column not in g.get("modified_initialization"):  # 如果也不在g变量的修改过的初始化清单里面
            table = RELATION_COLS[column]  # 获得联动的表名
            table_columns = table.split("+")
            # 构造re_col_file = {"shej_02+shij_02+xj_02": ["xj_02", ""]}
            take = re_col_file.setdefault(table, [None]*len(table_columns))
            take[table_columns.index(column)] = column
            re_col_file[table] = take
            before_splited_columns.remove(column)

    # 3. 删除空项
    re_col_file = {k: [i for i in v if i] for k, v in re_col_file.items()}

    return before_splited_columns, re_col_file

if __name__ == '__main__':
    no_re_col, re_col_file, df_cols_list = column_filter(dataframe)
    print(no_re_col, re_col_file)
