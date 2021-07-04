def process_default(api_dict):
    # 默认值
    from app import app
    SPECIAL_PARAMS = app.config["SPECIAL_PARAMS"]
    params_with_default = {k: v[0] for k, v in SPECIAL_PARAMS.items() if isinstance(v[0], str)}

    # param_trans参数 如果设置了特殊参数 是在默认值的基础上进行拼接
    if SPECIAL_PARAMS.get("param_trans", ""):
        params_trans_default = SPECIAL_PARAMS.get("param_trans", "")[0]
        if isinstance(params_trans_default, str):
            params_trans_default_list = params_trans_default.split(",")
            params_trans_list = api_dict.get("param_trans", "").split(",")
            pt_list = params_trans_default_list + params_trans_list
            # 对结果去重
            from utils.get_unilist import get_unilist
            api_dict["param_trans"] = ",".join(get_unilist(pt_list))

    # transformer的参数存在默认值
    # predict
    transformer = api_dict.get("transformer", "")
    if "predict" in transformer:
        if "(" in transformer and ")" in transformer:
            args = transformer.replace(")", "")
            if "realdata_show" not in args:
                args += "+realdata_show=1d)"
            api_dict["transformer"] = args



    params_with_default.update(api_dict)
    return 200, "success", params_with_default