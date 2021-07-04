import pandas as pd
import numpy as np
import random  # eval中可能会有random


def fill_random_or_real(x, init_dicts, column, table):
    if pd.isna(x) or not x or x in [np.inf, -np.inf]:
        value_list = init_dicts.get(column)  # 默认 所有取值可能 是一个list
        if not value_list:
            return
        if isinstance(init_dicts.get(column), dict):  # {"yy": {"table1": [], "table2": []}}
            value_list = init_dicts.get(column).get(table[0])
        if str(value_list[0]).startswith("random") or str(value_list[0]).startswith("round"):
            return eval(init_dicts.get(column)[0])
        else:
            return value_list[0]
    return x
