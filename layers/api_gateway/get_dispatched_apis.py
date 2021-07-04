import re


def after_param_protect(param_protect, request_args_copy):
    # param_protect = request_args_copy.get("param_protect","")
    black_list = re.search(r"black_list\((.*?)\)", param_protect)
    white_list = re.search(r"white_list\((.*?)\)", param_protect)
    if black_list:
        bk_list = black_list.groups()[0].split("+")
        for i in bk_list:
            request_args_copy.pop(i, "")
    elif white_list:
        wt_list = white_list.groups()[0].split("+")
        [request_args_copy.pop(i) for i in list(request_args_copy.keys()) if i not in wt_list]
    else:
        pass

    return request_args_copy


def url2dict(url):
    url = url.split("?")[1]
    request_args = {}
    for item in url.split("&"):
        if item:
            k, v = item.split("=", 1)
            if k:
                request_args[k] = v
    return request_args


def check_graph_id_dict(graph_id_dict):
    # # 检查是否所有key都是 gd_id0 的格式
    # for graph_id in graph_id_dict:
    #     if not re.match(r"gd_id[-]?\d+", graph_id):
    #         return 400, f"GRAPHIDERROR: The structure must be graph_id and number {graph_id}", {}

    # 按照数字排序
    graph_id_list = sorted(graph_id_dict, key=lambda x: int(x.strip("gd_id")))
    graph_id_list = [graph_id_dict[i] for i in graph_id_list]
    graph_id = "_".join(graph_id_list)

    # 检查是否在settings中存在映射
    from app import app
    url_dispatch_map = app.config["URL_DISPATCH_MAP"]

    url = None
    for graph_id_assigned in url_dispatch_map:
        if re.match(graph_id_assigned.lstrip("#"), graph_id):  # 去掉开头的井号再去匹配，带井号的是待废弃的
            url = url_dispatch_map[graph_id_assigned]
            break  # 匹配到就退出，多个匹配后面的不管
    # 如果查找后依然没有，报错
    if url is None:
        return 400, f"GRAPHIDERROR: No such specific gd_id combinations {graph_id}", {}
    # 如果是$开头作为分发的引用，用于构建测试接口【$引用的gd_id必须是正常的字符串url或者list/dict数据】
    elif isinstance(url, str) and url.startswith("$"):
        url = url_dispatch_map.get(url.lstrip("$"))
        if url is None:
            return 400, f"GRAPHIDERROR: No such specific gd_id combinations {graph_id}", {}
    # 如果是dict直接当作数据返回[如果走了$, 这里检查的是拿到$引用的]
    if isinstance(url, dict):
        res = {"map": url.get("map", {}), "data": url.get("data", {})} if "map" in url else {"data": url.get("data", {})}
        return 203, "success", res
    return 200, "success", url


def get_dispatched_apis(request_args):
    """
    如果 request_args中有 graph_id，根据 id 内容和 settings 中的 DISPATCH_MAP 进行分发
    1. 判断是否有 graph_id, 如果没有直接返回 request_args
    2. 如果有，在 settings 中寻找 URL_DISPATCH_MAP，如果没有，返回 code 400
    3. 如果有对应的 ID， 得到 url的字符串，对字符串处理得到字典
    4. 将request_args剩下的部分更新进字典中
    5. 返回更新的字典
    """
    # 1.去掉带有 invalid 的项 & 同时将空格变回加号(需要兼容空格紧跟逗号的情况)  兼容k里面出现不知道哪里来的中括号的情况
    request_args = {k.replace("[]", ""): v.replace(" ", "+").replace(",+", ",") for k, v in request_args.items() if v and not (v == "invalid" and k.startswith("gd_id"))}
    request_args_copy = request_args.copy()  # 备份，方便遍历/方便最后给url填空

    # 2.选出用于拼接得到分发标识的gd_id参数
    graph_id_dict = {i: request_args.pop(str(i), "") for i in request_args_copy if re.match(r"gd_id[-]?\d+", i)}

    # 3.如果要走分发
    if graph_id_dict:
        code, msg, url = check_graph_id_dict(graph_id_dict)  # 得到映射后的url
        if code != 200:
            return code, msg, url

        # 3.1 得到格式化后的url
        url = url.format(**request_args_copy)
        # 3.2 url --> dict
        graph_id_url_dict = url2dict(url)
        # 3.3 外界可以取消保护
        if "param_protect" in request_args:
            graph_id_url_dict.update({"param_protect": request_args["param_protect"]})
        # 3.4 url保护  param_protect=black_list|white_list
        request_args = after_param_protect(graph_id_url_dict.get("param_protect", ""), request_args)
        # 3.5 更新request_args
        graph_id_url_dict.update(request_args)
        return 200, "success", graph_id_url_dict
    return 200, "success", request_args


if __name__ == '__main__':
    t = url2dict("http://39.107.240.28:3389/api/xf/xfjc_zb/?timetype=cd&qh=shij&lx=yjnr&name=shij_02&value=xfjc&transformer=@groupby&day=[2019-01-01,2019-02-02]")
    print(t)
