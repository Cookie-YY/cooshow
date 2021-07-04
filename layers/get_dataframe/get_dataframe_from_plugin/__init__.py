import re

from flask import request, g

from layers.get_dataframe.get_dataframe_from_plugin.check_plugin import check_plugin_args
from layers.get_dataframe.get_dataframe_from_plugin.mode_custom import get_custom_apis
from layers.get_dataframe.get_dataframe_from_plugin.mode_sql import get_sql_apis


def get_dataframe_from_plugin(request_args):
    if request_args.get("gd_id", ""):  # 判断理论上是否需要走插件过程
        # 匹配url
        plugin_apis = []
        from app import app
        for i in app.config.get("APIS_PLUGIN", []):
            if re.match(i.get("url"), request.full_path):  # 如果能够匹配到全路径
                plugin_apis.append(i); break
            if re.search(r'gd_id=(.*)&', i.get("url")):    # 如果是 apis_dispatch 转发过来的
                if re.search(r'gd_id=(.*)&', i.get("url")).groups()[0] == request_args.get("gd_id", ""):
                    plugin_apis.append(i); break

        # 检查url
        code, msg, results = check_plugin_args(plugin_apis)
        if code != 200:
            return code, msg, {}

        # 获取mode，并判断模式
        mode = results.get("mode")

        # 格式化变量池
        from utils.db_connection import fx_pymysql, zb_pymysql, fx_engine, zb_engine
        # param_trans 之后的参数也能拿到[sql_qhauth]
        format_pool_custom = dict(**request_args,  **app.config, fx_pymysql=fx_pymysql, zb_pymysql=zb_pymysql, fx_engine=fx_engine, zb_engine=zb_engine)
        format_pool_custom.update(g.get("reqdicts_before_pt"))   # 用保存的param_trans之前的参数覆盖
        format_pool_sql = dict(**request_args, **app.config)
        format_pool_sql.update(g.get("reqdicts_before_pt"))      # 用保存的param_trans之前的参数覆盖

        # custom模式
        if mode == "custom":
            code, msg, data = get_custom_apis(results, format_pool_custom)
            if code != 200:
                return code, msg, {}
            mapping = data.pop("mapping", "")
            data = data.pop("data", [])

        # sql模式
        elif mode == "sql":
            mapping = results.get("mapping")
            code, msg, data = get_sql_apis(results, format_pool_sql)
            if code != 200:
                return code, msg, {}
        else:
            return 400, "", {}
        res = {"map": mapping, "data": data} if mapping else {"data": data}
        code = 204 if code==204 else 202
        return code, "success", res
    return 200, "success", request_args
