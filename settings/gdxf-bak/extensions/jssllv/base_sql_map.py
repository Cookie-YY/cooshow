# from settings.gdxf.extensions.jssllv import *
import importlib
from settings.gdxf.extensions.jssllv.get_sql_from_file import *

from flask import g


def get_base_sql_map():
    base_sql_map = {
        "1-2-形式": sql_1_2_xfxs,
        "1-4-形式": sql_1_4_xfxs,
        "2-2-形式": sql_2_2_xfxs,
        "2-4-形式": sql_2_4_xfxs,
        "1-5-形式": sql_1_5_xfxs,
        "1-6-形式": sql_1_6_xfxs,
        '2-5-形式': sql_2_5_xfxs,
        "1-2-全": sql_1_2_all,
        "1-4-全": sql_1_4_all,
        "2-2-全": sql_2_2_all,
        "2-4-全": sql_2_4_all,
        "1-5-全": sql_1_5_all,
        "1-6-全": sql_1_6_all,
        '2-5-全': sql_2_5_all,
        '2-6-全': sql_2_6_all,
        '2-6-形式': sql_2_6_xfxs,
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
