from layers.get_dataframe.get_dataframe_from_extension.ext_executor import ext_executor


def get_dataframe_from_extension(apis_copy, apis):
    # 0.初始化：加载自定义extension
    # 0.1 判断来自系统的extension还是自定义extension并加载
    transformer = apis_copy["transformer"]
    extension_module = transformer.split("(")[0]
    extension_class = extension_module.capitalize()
    from app import app
    module_path = f"settings.{app.config['PROJECT']}.extensions.{extension_module}" \
        if extension_module in app.config.get("CUS_EXTENSIONS", []) \
        else f"libs.extensions.{extension_module}"
    extension_setting = __import__(module_path, globals(), locals(), [extension_class])  # 导入extension
    Ext = getattr(extension_setting, extension_class)

    # 0.2 解析transformer参数
    params_with_parentheses = transformer.replace(extension_module, "")
    params = params_with_parentheses.strip("(").strip(")").split("+")  # params=["7d"]    params=["7d", "p=1", "q=2"]
    kwargs = {param.split("=")[0]: param.split("=")[1] for param in params if "=" in param}
    args = [i for i in params if "=" not in i]  # args=[""] (当params没有传)

    # 1. ext的核心过程
    ext = Ext(apis_copy, apis, *args, **kwargs)
    code, msg, results = ext_executor(ext)
    if code != 200:
        return code, msg, results
    df, apis_copy = results["df"], results["apis_copy"] # 执行ext的方法

    # # 2.如果df是dataframe（不是np.int64） 且不只是一个列（只有一个列是只有value的情况）
    # import pandas as pd
    # if isinstance(df, pd.DataFrame) and len(df.columns) > 1:
    #     df = df.fillna(None)

    # 3.封装dateframe对象以供返回
    dataframe = {**apis_copy, **{"df": df}}
    dataframe["table"] = ["SQL OR Reuse Last results"]  # 兼容没有waiting_for_search的情况
    if ext.waiting_for_search:
        dataframe["table"] = [i.get("table") for i in ext.waiting_for_search if "table" in i]
    return 200, "success", dataframe


if __name__ == '__main__':
    apis = {'realm': "xf", 'value': 'xfjc', 'lx': "yjnr", "qh": "shij", "index": "xfjc_zb", "timetype": "cd",
            "name": "yjnr", "day": "2020-01-9,2020-01-10", "transformer": "@grouby:shij_02+@hb"}
    code, msg, test = get_dataframe_for_each_api(apis)

    print(code, msg, test)
