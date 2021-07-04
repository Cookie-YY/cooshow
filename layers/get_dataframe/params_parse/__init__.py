from sqlalchemy import or_


def parse_condition(ex_table, k, value):
    # like条件
    if str(k).startswith("LIKE-"):
        k = k.replace("LIKE-", "")
        k = k.strip("C")
        if "%" not in value:
            return getattr(ex_table.columns, k).like(f"%{value}%")
        return getattr(ex_table.columns, k).like(value)

    # in条件
    elif str(k).startswith("IN-"):
        k = k.replace("IN-", "")
        k = k.strip("C")
        if isinstance(value, list):
            return getattr(ex_table.columns, k).in_(value)
        return getattr(ex_table.columns, k).in_(value.split(","))

    # or条件
    elif str(k).startswith("OR-"):
        k = k.replace("OR-", "")
        k = k.strip("C")
        or_list = []
        v_list = value if isinstance(value, list) else value.split(",")
        for v in v_list:
            cond = getattr(ex_table.columns, k) != v.replace("!", "") if v.startswith("!") else getattr(ex_table.columns, k) == v
            or_list.append(cond)
        return or_(*or_list)

    # 分段条件
    elif "," in str(value):
        value_splited = value.split(",")
        if len(value_splited) != 2:
            return 400, "the condition which contains [] is in a wrong format, it should be [yyyy-mm-dd,yyyy-mm-dd] or [a,b]", {}
        min_value = value_splited[0]
        max_value = value_splited[1]
        return getattr(ex_table.columns, k).between(min_value, max_value)

    # 等或不等条件
    else:
        if str(value).startswith("!"):  # 不等于条件
            return getattr(ex_table.columns, k) != str(value).strip("!")
        return getattr(ex_table.columns, k) == value


def get_conditions(ex_table, conditions_dict):
    conditions = []
    for k, value in conditions_dict.items():
        k = k.strip("C")

        if not hasattr(ex_table.columns, k) and \
                not hasattr(ex_table.columns, k.strip("LIKE-").lstrip("C")) and \
                not hasattr(ex_table.columns, k.strip("IN-").lstrip("C")) and \
                not hasattr(ex_table.columns, k.strip("OR-").lstrip("C")):
            from app import app
            NOCOLUMN_ERROR = app.config.get("NOCOLUMN_ERROR", True)
            if NOCOLUMN_ERROR:
                return 400, f"NoSuchColumnError: the {ex_table.fullname} has no condition columns [{k}]", {}
            return 200, f"NoSuchColumnError: the {ex_table.fullname} has no condition columns [{k}]", []

        conditions.append(parse_condition(ex_table, k, value))

    return 200, "success", conditions
