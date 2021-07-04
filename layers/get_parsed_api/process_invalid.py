def process_invalid(api_dict):
    """
    输入：{'value': 'xfjc@zb', 'lx': "xfxs_cfxfbz", 'xfxs': "invalid"}
    输出：{'value': 'xfjc@zb', 'lx': "xfxs_cfxfbz"}
    """
    # 处理invalid：
    return 200, "success", {k: v for k, v in api_dict.items() if v not in ["invalid", "Pinvalid"]}


if __name__ == '__main__':
    api_dict = {"1": "a", "2": "b", "3": "invalid"}
    print(process_invalid(api_dict))