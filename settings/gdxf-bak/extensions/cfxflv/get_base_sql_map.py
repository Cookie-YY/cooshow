import importlib
from settings.gdxf.extensions.cfxflv.get_sql_from_file import *

def get_base_sql_map():
    base_sql_map = {
        "1-1-全": sql_1_1_all,
        "1-1-形式": sql_1_1_xfxs,
        "1-2-全": sql_1_2_all,
        "1-2-形式": sql_1_2_xfxs,
    }
    return base_sql_map


# def getter(sql_name):
#     moduel = importlib.import_module(f"settings.gdxf.extensions.jssllv.{sql_name}")
#     sql = moduel.getter()
#     return sql


if __name__ == '__main__':
    print(get_base_sql_map())
