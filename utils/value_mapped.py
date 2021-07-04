import re
import pandas as pd


def value_mapped(df, map_type="VALUE_MAP", apis_copy=None):
    """
    将计算完的结果做一次映射
    """
    if apis_copy is None:
        apis_copy = {}
    from app import app
    config_map = app.config.get(map_type, {})  # {"xfxs": {"网信"： "网上投诉|网上信访"}}
    api_vm_names = apis_copy.get("value_map", "").split(",")
    api_vm_list = [value for key, value in config_map.items() if key.startswith("global_") or key in api_vm_names]

    for vm in api_vm_list:
        for col, mapping in vm.items():
            if "->" in col and col in df:
                old, new = col.split("->")
                if old in df:
                    for after, condition in mapping.items():  # 字段的多中映射方法
                        df[new] = df[old].apply(lambda x: after if re.match(condition, str(x)) else x)
                    df = df.drop([old], axis=1)  # drop不会就地修改，创建副本返回
                    if apis_copy.get("name") == old:
                        apis_copy["name"] = new  # 这里会同步影响外面的apis_copy
            elif "->" not in col and col in df:
                for after, condition in mapping.items():  # 字段的多中映射方法
                    df[col] = df[col].apply(lambda x: after if re.match(condition, str(x)) else x)
    return df


    # # value_map_from_api = eval(apis_copy.get("value_map", {}))
    # value_map = {**config_map, **config_map}
    # for col, mapping in value_map.items():
    #     if col in df:  # 如果目标字段在df中
    #         for after, condition in mapping.items():  # 字段的多中映射方法
    #             df[col] = df[col].apply(lambda x: after if re.match(condition, str(x)) else x)
    # return df

