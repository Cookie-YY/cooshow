import os

from flask import current_app


def check_plugin_args(plugin_apis):
    """
    检查用户配置的 apis_plugins文件
    返回检查后的内容
    """
    if len(plugin_apis) == 0:
        return 400, "No url in plugins can match gd_id", {}
    if len(plugin_apis) > 1:
        return 400, "PluginLengthError: There are more than 1 plugin_config match", {}
    plugin_api = plugin_apis[0]
    fx_db_sql = plugin_api.get("fx_db_sql")
    zb_db_sql = plugin_api.get("zb_db_sql")
    mapping = plugin_api.get("map")
    on = plugin_api.get("on")
    time_format = plugin_api.get("time_format")
    value_map = plugin_api.get("value_map", [])
    mode = plugin_api.get("mode", "sql")  # 默认模式是sql，支持sql/custom/
    full = plugin_api.get("full", {})
    variables = plugin_api.get("variables", {})
    file = ""
    if mode == "custom":
        file = plugin_api.get("file", "")
        file = file if file.endswith(".py") else file + ".py"
        if not file or not os.path.exists(os.path.join(current_app.config["SETTINGS_DIR"], "custom", file)):
            return 400, "PluginCustomError: The param 'file' must be specified and exist", {}
    if mode == "sql":
        if not mapping:
            return 400, "PluginMapError: No 'map' Found", {}
        if not fx_db_sql and not zb_db_sql:
            return 400, "PluginURLError: At least one SQL, specify fx_db_sql or zb_db_sql", {}
        if full and "value" not in full:
            return 400, "PluginFullError: When using param 'full', please specify 'value'", {}

    if mode not in ["sql", "custom"]:
        return 400, "PluginModeError: Wrong mode", {}
    return 200, "success", {"fx_db_sql": fx_db_sql,
                            "zb_db_sql": zb_db_sql,
                            "mapping": mapping,
                            "on": on,
                            "time_format": time_format,
                            "value_map": value_map,
                            "mode": mode,
                            "file": file,
                            "full": full,
                            "variables": variables}
