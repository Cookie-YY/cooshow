from layers.api_gateway import api_gateway
from layers.convert_dataframe import convert_dataframe
from layers.get_dataframe import get_dataframe
from layers.get_parsed_api import get_parsed_apis
from layers.get_splited_apis import get_splited_apis
from layers.makeup_dataframe import makeup_dataframe

from flask import request


def parse_data(realm, index, request_args):
    """
    组装所有层的方法：
    0. 网关层 [api_gateway]:         权限校验 以及 指标分发                                         request_args -> api_dicts
    1. 拆分层 [get_splited_apis]:    遇到 extra_index和 main_name 把组合指标的 url 拆分              api_dicts   -> api_dicts
    2. 解析层 [get_parsed_apis]:     解析 drop/invalid/$引用/now 的简写情况                         api_dicts   -> api_dicts
    3. 查询层 [get_dataframe]:       按照 api 的内容查库                                           api_dicts   -> dataframes
    # 4. 计算层 [compute_dataframe]
    5. 补充层 [makeup_dataframe]:    按照标准的格式排序补零                                         dataframes   -> dataframes
    6. 转换层 [convert_dataframe]:   将 pandas转成需要的格式                                       dataframes   -> json
    """
    # 0.网关层(apis -> apis)
    # 1. 权限验证
    # 2. apis 分发：如果传过来的request_args只有参数 graph_id\d+ 那么需要拼接 graph_id 做分发
    code, msg, api_dicts_or_result = api_gateway(realm, index, request_args)
    if code != 200:
        return code, msg, api_dicts_or_result

    # 1.拆分层(apis -> apis)
    # 返回 api_dicts = {
    #     "总数": {"name": "", "value": ""},
    #     "2": {"name": "", "value": ""}}
    code, msg, api_dicts = get_splited_apis(realm, index, api_dicts_or_result)
    if code != 200:
        return code, msg, {}

    # 如果开启调试模式，在这里跳出
    from flask import g
    if g.get("debug") == "true":
        return 999, "调试模式", [{main_name: request.base_url+"?"+"&".join([f"{k}={v}" for k, v in api_dict.items() if v and k!="debug"])} for main_name, api_dict in api_dicts.items()]

    g.index_idx = 0    # 指标的索引
    # 开始分流，逐一对每一个拆出来的请求做处理
    data_frame_list = []
    for main_name, api_dict in api_dicts.items():
        g.index_idx += 1                # 指标的索引
        g.modified_initialization = {}  # 等待装填内容  每个指标有自己的
        # 2.解析层(apis   -> apis)
        # 对请求参数做解析，拿到最终的请求字典
        code, msg, api_dict = get_parsed_apis(api_dict)      # 处理 =drop/$引用问题/=now的解析
        if code != 200:
            return code, msg, {}
        from flask import g
        g.req_str = "&".join([f"{k}={v}" for k, v in api_dict.items() if v])  # 请求中增加的全局属性

        if g.get("debug"):
            if g.get("debug") == str(g.get("index_idx")):
                return 999, "调试模式", {main_name: request.base_url + "?" + "&".join(
                    [f"{k}={v}" for k, v in api_dict.items() if v and k != "debug"])}

        # 3.查询层(apis   -> pandas)
        code, msg, dataframe = get_dataframe(api_dict)  # 返回df
        if code != 200:
            return code, msg, dataframe

        # 4.补充层(pandas -> pandas)
        # 返回data = pd.DataFrame()
        code, msg, dataframe = makeup_dataframe(dataframe)
        if code != 200:
            return code, msg, {}

        data_frame = dict(**{"main_name": main_name}, **dataframe, **{"req": g.get("req_str")})
        data_frame_list.append(data_frame)

    # 5.转换层(pandas -> json)
    # 返回data = [{"name": "", "value": ""}, {"name": "", "value": ""}]
    code, msg, data = convert_dataframe(data_frame_list)
    if code != 200:
        return code, msg, {}

    return 200, "success", data


if __name__ == '__main__':
    # parse_data("xf", "xfjc", {"timetype": "cy",
    #                 "lx": "xfxs_cfxfbz",
    #                 "name": "cfxfbz",
    #                 "value": "xfjc",
    #                 "stack": "cfxfbz",
    #                 "extra_index": "value@to:zb,index@to:xfrc_zb;value@to:xfrc,index@to:xfrc_zb;value@to:zb;year@math:-1",
    #                 "main_name": "信访件次,件次占比,信访人次,人次占比",
    #                 "xfxs": "drop",
    #                 "year": "2020"})

    parse_data("xf", "xfjc", {
        "timetype": "cy", "qh": "shij", "name": "shij_02", "stack": "shij_02", "extra_index": "lx@to:xfxs;stack@to:xfxs","main_name": "总数,", "year": 2020
    })
