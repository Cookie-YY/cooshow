def process_drop(api_dict):
    """
    输入：{'value': ['xfjc@zb'], 'lx': ["xfxs_cfxfbz"], 'xfxs': ["drop"]}
    输出：{'value': ['xfjc@zb'], 'lx': ["cfxfbz"]}
    """
    # 处理drop：
    # shij_02=drop    month=drop    xfxs=drop   api_dict中有    报错
    remove_list = []; update_dict = {}

    for k, v in api_dict.items():
        if v == "drop":
            remove_list.append(k)
            if k == "xj_02":
                update_dict["qh"] = "shij"
                update_dict["table"] = api_dict.get("table", "").replace("xj", "shij")
                if api_dict.get("name") == "xj_02":
                    remove_list.append("name")
            if k == "shij_02":
                update_dict["qh"] = "shej"
                update_dict["table"] = api_dict.get("table", "").replace("shij", "shej")
                if api_dict.get("name") == "shij_02":
                    remove_list.append("name")
            elif k == "month":
                update_dict["timetype"] = "cy"
                update_dict["table"] = api_dict.get("table", "").replace("cm", "cy")
                if api_dict.get("name") == "month":
                    remove_list.append("name")
            elif k.strip("C") in api_dict.get("lx", ""):
                k_strip = k.strip("C")
                lx = api_dict.get("lx", "")
                lx = lx.replace(f"_{k_strip}", "").replace(f"{k_strip}_", "").replace(f"{k_strip}", "")
                api_dict["lx"] = lx
                update_dict["table"] = api_dict.get("table", "").replace(f"_{k_strip}", "").replace(f"{k_strip}_", "").replace(f"{k_strip}", "")
                if api_dict.get("name") == k_strip:
                    remove_list.append("name")
            elif k.strip("C") in api_dict.get("table", ""):
                k_strip = k.strip("C")
                update_dict["table"] = api_dict.get("table", "").replace(f"_{k_strip}", "").replace(f"{k_strip}_", "").replace(f"{k_strip}", "")
                if api_dict.get("name") == k_strip:
                    remove_list.append("name")
            else:
                remove_list.append(k)

    for k in remove_list:
        api_dict.pop(k, "")
    api_dict.update(update_dict)
    return 200, "success", api_dict


if __name__ == '__main__':
    api_dict = {'value': 'xfjc@zb', 'lx': "xfxs_cfxfbz", 'xfxs': "drop", "name": "shij_02"}
    code, msg, test = process_drop(api_dict)
    print(test)
