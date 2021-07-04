import pandas as pd

from layers.get_dataframe.get_dataframe_from_extension import get_dataframe_from_extension
from layers.get_dataframe.get_dataframe_from_plugin import get_dataframe_from_plugin
from layers.get_dataframe.params_check.params_check_real_table import get_real_table
from layers.get_dataframe.params_check.params_check_each import params_check_each


def get_dataframe(apis):
    """
    输入：{'value': 'xfjc', 'lx': "xfxs_cfxfbz", 'xfxs': "drop"},
    输出：dataframe
    """
    # 1.参数逐一校验【extension/plugin】
    code, msg, apis_and_apis_copy_after_check = params_check_each(apis)
    if code != 200:
        return code, msg, {}
    apis_copy, apis = apis_and_apis_copy_after_check["apis_copy"], apis_and_apis_copy_after_check["apis"]

    # 2.plugin【plugin模式，直接返回数据】
    code, msg, apis_or_result = get_dataframe_from_plugin(apis_copy)
    if code in [202]:  # 说明走的是插件的过程，不需要走后面了
        return code, msg, apis_or_result
    if code != 200:
        return code, msg, {}

    # 3.extension【除CUS_EXTENSIONS外，其他的EXTENSION需要寻找real_table】
    from app import app
    code, msg, dataframe = get_dataframe_from_extension(apis_or_result, apis)
    if code != 200:
        return code, msg, dataframe

    # 4.保留有效数字
    SIGNIFICANT_DIGITS = app.config.get("SIGNIFICANT_DIGITS", 4)
    try:
        if isinstance(dataframe["df"], pd.DataFrame):
            dataframe["df"][dataframe.get("value")] = dataframe["df"][dataframe.get("value")].apply(lambda x: round(x, SIGNIFICANT_DIGITS))
        else:
            dataframe["df"] = round(dataframe["df"], SIGNIFICANT_DIGITS)
    except Exception:
        pass
    return 200, "success", dataframe

