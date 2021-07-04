import re


def params_check_each(apis):
    apis_copy = apis.copy()
    checked_params = {}

    # 1.特殊参数的校验，和删除
    from app import app
    SPECIAL_PARAMS = app.config.get("SPECIAL_PARAMS", {})
    for k, v in SPECIAL_PARAMS.items():
        if k in apis_copy:
            condition = v[1]
            if condition and apis_copy[k]:  # 如果该参数有条件 并且 v 有值
                if not re.match(condition, apis_copy[k]):  # 如果不满足条件
                    return 400, f"ParamsStructureError: [{k}] must match {condition}, now is [{apis_copy[k]}]", {}
        apis.pop(k, "")  # 删除所有特殊参数
    checked_params.update(apis_copy)

    # 2. 处理默认值无法写的参数
    # value
    index = checked_params.get("index")
    table = checked_params.get("table")
    index_defalut = index.split("_")[0] if index else table.replace("_zb", "").replace("_tb", "").replace("_hb", "").split("_")[-1]
    checked_params["value"] = apis_copy.get("value", index_defalut)

    # ceil_value
    checked_params["ceil_value"] = apis_copy.get("ceil_value", checked_params["ceil"])

    # 3. 其他检验
    # 3.1 transformer 检验
    transformer = checked_params["transformer"].strip("@")
    transformer_ = transformer.split("(")[0]
    if transformer_ not in app.config.get("EXTENSIONS", []):
        return 400, f"ParamsStructureError: [transformer] must be registered", {}
    checked_params["transformer"] = transformer

    return 200, "success", {"apis_copy": checked_params, "apis": apis}
