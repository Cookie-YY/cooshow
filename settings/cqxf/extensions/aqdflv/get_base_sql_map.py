import importlib
from settings.gdxf.extensions.aqdflv.get_sql_from_file import *

def get_base_sql_map():
    base_sql_map = {
        "3-4-全": sql_3_4_all,
        "3-4-形式": sql_3_4_xfxs,
        "3-2-全": sql_3_2_all,
        "3-2-形式": sql_3_2_xfxs
    }
    return base_sql_map


# def getter(sql_name):
#     moduel = importlib.import_module(f"settings.gdxf.extensions.jssllv.{sql_name}")
#     sql = moduel.getter()
#     return sql


if __name__ == '__main__':
    print(get_base_sql_map())
