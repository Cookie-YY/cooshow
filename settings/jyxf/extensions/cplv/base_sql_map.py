# from settings.gdxf.extensions.jssllv import *
import importlib
from settings.gdxf.extensions.cplv.get_sql_from_file import *

from flask import g


def get_base_sql_map():
    base_sql_map = {
        "1-1-全": sql_1_1_all,
        "1-1-形式": sql_1_1_xfxs,
        "1-2-全": sql_1_2_all,
        "1-2-形式": sql_1_2_xfxs,
        "1-3-全": sql_1_3_all,
        "1-3-形式": sql_1_3_xfxs,
        "2-1-全": sql_2_1_all,
        "2-1-形式": sql_2_1_xfxs,
        "2-2-全": sql_2_2_all,
        "2-2-形式": sql_2_2_xfxs,
    }
    # 返回加载完毕的map
    return base_sql_map


# # 动态导入
# def getter(sql_name):
#     moduel = importlib.import_module(sql_name)
#     sql = moduel.getter()
#     return sql

if __name__ == '__main__':
    print(getter('2-5-形式'))
