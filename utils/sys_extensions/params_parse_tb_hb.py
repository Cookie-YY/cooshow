import datetime


# 同比的参数解析
def params_parse_tb(conditions_dict):
    day_condition = conditions_dict.get("day")
    year_condition = conditions_dict.get("year")
    month_condition = conditions_dict.get("month")
    if day_condition:
        min_value, max_value = day_condition.split(",")
        min_value = min_value.split()[0]
        max_value = max_value.split()[0]
        min_date = datetime.datetime.strptime(min_value, "%Y-%m-%d")
        max_date = datetime.datetime.strptime(max_value, "%Y-%m-%d")
        last_min_date = min_date.replace(year=min_date.year - 1)
        last_max_date = max_date.replace(year=max_date.year - 1)
        conditions_dict["day"] = f"{last_min_date.strftime('%Y-%m-%d')},{last_max_date.strftime('%Y-%m-%d')}"
    elif year_condition and month_condition:
        conditions_dict["year"] = int(year_condition) - 1
        conditions_dict["month"] = month_condition
    else:
        return
    return conditions_dict


# 环比的参数解析
def params_parse_hb(conditions_dict):
    day_condition = conditions_dict.get("day")
    year_condition = conditions_dict.get("year")
    month_condition = conditions_dict.get("month")
    if day_condition:
        min_value, max_value = day_condition.split(",")
        min_value = min_value.split()[0]
        max_value = max_value.split()[0]
        min_date = datetime.datetime.strptime(min_value, "%Y-%m-%d")
        max_date = datetime.datetime.strptime(max_value, "%Y-%m-%d")
        diff = max_date - min_date
        last_min_date = min_date - diff - datetime.timedelta(days=1)
        last_max_date = max_date - diff - datetime.timedelta(days=1)
        conditions_dict["day"] = f"{last_min_date.strftime('%Y-%m-%d')},{last_max_date.strftime('%Y-%m-%d')}"
    elif year_condition and month_condition:
        date = datetime.datetime.strptime(f"{year_condition}-{month_condition}-1", "%Y-%m-%d")
        date_hb = date - datetime.timedelta(days=2)
        year_hb, month_hb = date_hb.year, date_hb.month
        conditions_dict["year"] = year_hb
        conditions_dict["month"] = month_hb
    else:
        return
    return conditions_dict
