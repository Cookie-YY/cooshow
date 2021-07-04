import re
from datetime import datetime, timedelta

from utils.parse_compute import parse_compute


def process_now(api_dict):
    """
    输入：{'day': "[2020-06-22, now-4]"}
    输入：{'month': "[now-2, now]"}
    输入：{'year': "[now-2, now]"}
    输出：{'day': "2020-06-22, 2020-06-24"}
    输出：{'month': "4, 6"}
    输出：{'year': "2018, 2020"}
    """
    update_dict = {}
    for k, v in api_dict.items():
        value = str(v)
        # 解析now
        if "now" in value:
            if k in ["year", "month", "day", "date"]:
                if k == "year":
                    value = value.replace("now", str(datetime.now().year))
                    # update_dict[k] = value  # 直接赋值，如果是范围的，在后面可以覆盖
                elif k == "month":
                    value = value.replace("now", str(datetime.now().month))
                    update_dict["year"] = str(datetime.now().year)
                elif k == "day":
                    value = value.replace("now", datetime.now().strftime("%Y/%m/%d"))
                elif k == "date":
                    value = value.replace("now", datetime.now().strftime("%Y/%m/%d"))
                if "," not in value:  # 说明不是范围
                    code, msg, value = parse_compute(value)  # 直接赋值，如果是范围的，在后面可以覆盖
                    if code != 200:
                        return code, msg, {}
                update_dict[k] = value
        # 解析范围（同时去掉中括号）
        if str(value).startswith("[") and str(value).endswith("]"):
            min_value = value.strip("[").strip("]").split(",")[0]  # "2020-1"
            max_value = value.strip("[").strip("]").split(",")[1]  # "2020"
            code, msg, start = parse_compute(min_value)
            if code != 200:
                return code, msg, {}
            code, msg, end = parse_compute(max_value)
            if code != 200:
                return code, msg, {}
            value_parsed = f"{start},{end}"
            update_dict[k] = value_parsed
    api_dict.update(update_dict)
    return 200, "success", api_dict


if __name__ == '__main__':
    api_dict = {'day': "[2020-06-22,2020-06-24]", "year":"[now-3,now]", "month":"[now-3,now]"}
    test = process_now(api_dict)
    print(test)