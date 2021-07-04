from layers.get_parsed_api.process_datestr import process_datestr
from layers.get_parsed_api.process_drop import process_drop
from layers.get_parsed_api.process_dollar import process_dollar
from layers.get_parsed_api.process_now import process_now
from layers.get_parsed_api.process_invalid import process_invalid
from flask import g


def get_parsed_apis(api_dict):
    """
    输入：{"name": "", "value": ""}
    """
    # 1.处理默认值问题
    from layers.get_parsed_api.process_default import process_default
    code, msg, result_this = process_default(api_dict)
    if code != 200:
        return code, msg, {}

    # 2.处理invalid问题[Pinvalid 或者 invalid]
    code, msg, result_this = process_invalid(result_this)
    if code != 200:
        return code, msg, {}

    # 3.处理drop问题
    code, msg, result_this = process_drop(result_this)
    if code != 200:
        return code, msg, {}

    # 4.处理now问题(去掉范围条件的中括号)
    code, msg, result_this = process_now(result_this)
    if code != 200:
        return code, msg, {}

    # 5.处理时间的字段类型兼容问题
    code, msg, result_this = process_datestr(result_this)
    if code != 200:
        return code, msg, {}

    # 6.处理权限问题
    from layers.get_parsed_api.process_auth import process_auth
    code, msg, result_this = process_auth(result_this)
    if code != 200:
        return code, msg, {}

    # 7.处理start/end
    for k, v in result_this.copy().items():
        if k in ["day", "date", "year"] and "," in str(v):
            start, end = v.split(",")
            result_this["start"] = start
            result_this["end"] = end

    ############ 此时将没有经过param_trans的内容放到g变量中，保存一份完整的用户参数 ############
    g.reqdicts_before_pt = result_this.copy()
    result_this.pop("start", "")
    result_this.pop("end", "")

    # 8.处理param_trans
    from layers.get_parsed_api.process_paramtrans import process_paramtrans
    code, msg, result_this = process_paramtrans(result_this)
    if code != 200:
        return code, msg, {}

    # 9.处理$引用问题
    code, msg, result_this = process_dollar(result_this)
    if code != 200:
        return code, msg, {}

    return 200, "success", result_this


if __name__ == '__main__':
    api_dicts = {"1": {'value': 'xfjc@zb', 'lx': "xfxs_cfxfbz", "name": "$index-xxx", "index": "xfjc", "stack": "$index", "transformer":"@groupby:$stack + @zb:xfxs/xfxs", "xfxs": "drop", "day": "[2018-02-02,2019-02-02]"},
                 "2": {'value': 'xfjc@zb', 'lx': "xfxs_cfxfbz", "name": "$index", "index": "xfjc", "xfxs": "drop", "year": "[now-2,now]"}}
    code, msg, test = get_parsed_apis(api_dicts)
    print(code, msg)
    for i in test:
        print(i, test[i])
    # print(code, msg, test)
    # python test.py $1
    # python test.py test.py