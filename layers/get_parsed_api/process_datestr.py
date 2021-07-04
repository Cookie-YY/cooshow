def process_datecolumn(api_dict, column):
    tar = api_dict.get(column)
    if tar:
        if isinstance(tar, str):
            if "," in tar:
                start, end = tar.split(",")
                from app import app
                tar = f"{start} {app.config.get('DATE_START','00:00:00')},{end} {app.config.get('DATE_END','00:00:00')}"
                # tar = ",".join((list(map(lambda x: x + " 00:00:00", tar.split(",")))))
            else:
                tar = tar + " 00:00:00"
        else:
            return 400, "unsupported date type", {}
        api_dict[column] = tar
    return 200, "success", api_dict


def process_datestr(api_dict):
    """
    输入：{'data': '2020-01-01'}  or {'data': ['2020-01-01', '2020-10-10']}
    or
    输入：{'day': '2020-01-01'}  or {'day': ['2020-01-01', '2020-10-10']}

    输出：{'data': '2020-01-01 00:00:00'}  or {'data': ['2020-01-01 00:00:00', '2020-10-10 00:00:00']}
    or
    输出：{'day': '2020-01-01 00:00:00'}  or {'day': ['2020-01-01 00:00:00', '2020-10-10 00:00:00']}
    """

    code, msg, api_dict = process_datecolumn(api_dict, "day")
    if code != 200:
        return code, msg, {}
    code, msg, api_dict = process_datecolumn(api_dict, "date")
    if code != 200:
        return code, msg, {}
    return 200, "success", api_dict
