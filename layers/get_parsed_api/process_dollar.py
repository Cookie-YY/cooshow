import re


def get_refer(api_dict, refer):
    target = api_dict.get(refer)
    if target is None:
        return 400, "if use '$' in the url, there must be the corresponding content", {}
    if "$" not in target:
        return 200, "success", target
    else:
        return get_refer(api_dict, target.strip("$"))


def process_dollar(api_dict):
    """
    输入：{'value': 'xfjc@zb', 'lx': "xfxs_cfxfbz", "name": "$index", "index": "xfjc"}
    输出：{'value': 'xfjc@zb', 'lx': "xfxs_cfxfbz", "name": "xfjc", "index": "xfjc"}
    """
    # 处理 $引用
    # order = -$index      name=$timetype    name=$qh
    # transformer=@groupby:$name,$stack + @zb:xfxs/xfxs      transformer=@groupby:-day+@zb:xfxs/all
    # 去掉zb               cy转year           shij转02
    # order = -xfjc        name=year         name=shij_02

    update_dict = {}
    for k, v in api_dict.items():
        value = str(v)  # year=2020传进来是 "year"="2020"      但是如果math:-1， 传进来是 "year"=2019
        if "$" in value:
            dollar_list = re.findall(r"\$\w+", value)  # 等待被替换的列表
            if not dollar_list:
                return 400, "if use '$' in the url, there must be the reference value", {}
            for refer in dollar_list:
                if refer not in ['$name', '$stack', '$index', '$timetype', '$qh', '$value']:
                    return 400, "if use '$' in the url, there must be the right reference value", {}
                # 递归获得最终的引用内容
                refer_nodollar = refer.strip("$")
                code, msg, target_value = get_refer(api_dict, refer_nodollar)
                if code != 200:
                    return code, msg, {}
                # 对最终的引用内容做修改
                from app import app
                need_transfer = app.config.get("URL_REFERENCE")
                if target_value in need_transfer:
                    target_value = need_transfer[target_value]  # target_value: ["year", "xfjc_zb"]
                target_value = target_value.replace("_zb", "")  # target: ["year, xfjc", "month", "shij_02", "shej_02"]
                value = value.replace(refer, target_value)
                update_dict[k] = value
    api_dict.update(update_dict)
    return 200, "success", api_dict


if __name__ == '__main__':
    api_dict = {'value': 'xfjc@zb', 'lx': "xfxs_cfxfbz", "name": "$index", "index": "xfjc", "transformer":"@groupby:$name,$stack + @zb:xfxs/xfxs"}
    # code,msg, target = get_refer(api_dict, "name")
    # print(target)

    code, msg, test = process_dollar(api_dict)
    print(code, msg, test)
