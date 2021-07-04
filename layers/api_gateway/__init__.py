from layers.api_gateway.authentication import authentication
from layers.api_gateway.get_dispatched_apis import get_dispatched_apis


def api_gateway(realm, index, request_args):
    # 1. 权限验证 [登录/等级/加密]
    code, msg, result = authentication(request_args)
    if code != 200:
        return code, msg, {}

    # 2. apis 分发 [参数保护/空格转加号]
    code, msg, api_dict = get_dispatched_apis(request_args)
    if code != 200:
        return code, msg, api_dict

    return 200, "success", api_dict
