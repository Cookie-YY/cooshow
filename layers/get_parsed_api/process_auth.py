from flask import g


def process_auth(api_dict):
    level_auth_code = g.get("level_auth", "")
    # 如果g变量中没有权限等级,跳出
    if not level_auth_code:
        return 200, "success", api_dict

    # 如果g变量中有权限等级, 却没有查到对应的权限，跳出
    from app import app
    LEVEL_AUTH_MAP = app.config.get("LEVEL_AUTH_MAP", {})  # 只要调用这个方法一定是有LEVEL_AUTH_MAP
    qh_ceiling = LEVEL_AUTH_MAP.get(level_auth_code)
    if not qh_ceiling:
        return 400, "No qh_code match the given one", {}
    g.level_auth_name = qh_ceiling   # 用名称替换原来的代码

    # 检查权限
    from utils.qh_processor import get_qh_with_auth
    qh = api_dict.get("Cqh") or (api_dict.get("xj_02") or api_dict.get("shij_02") or api_dict.get("shej_02"))
    table = api_dict.get("table", "")
    qh_with_auth = get_qh_with_auth(qh, qh_ceiling, table)
    if qh_with_auth:  # 开启level_auth但是没传Cqh 也没传shej_02/shij_02/xj_02
        api_dict.pop("shej_02", "")
        api_dict.pop("shij_02", "")
        api_dict.pop("xj_02", "")
        api_dict.update({"Cqh": qh_with_auth})

    return 200, "success", api_dict