from utils.get_unilist import get_unilist


def add_global_info(data_frame_list, results):
    table_list = []
    req_list = []
    for dataframe in data_frame_list:
        table_list.extend(dataframe["table"])
        req_list.append(dataframe["req"])
    results["table"] = get_unilist(table_list)
    # results["req"] = get_unilist(req_list)
    return results
