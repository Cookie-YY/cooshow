from datetime import datetime, timedelta
import re


def parse_date_add_or_sub(now, operator, content):
    now = datetime.strptime(now, "%Y/%m/%d")
    if operator == "+":
        if "m" in content:
            content = content.replace("m", "")
            res = now + timedelta(days=int(content)*30)
        elif "y" in content:
            content = content.replace("y", "")
            res = now + timedelta(days=int(content)*365)
        else:
            res = now + timedelta(days=int(content))
    else:
        if "m" in content:
            content = content.replace("m", "")
            res = now - timedelta(days=int(content) * 30)
        elif "y" in content:
            content = content.replace("y", "")
            res = now - timedelta(days=int(content) * 365)
        else:
            res = now - timedelta(days=int(content))
    res = datetime.strftime(res, "%Y-%m-%d")
    return res


def parse_compute(express):
    """
    输入："2020-01-02,-,2d"   "3,-,1"       "1"        "2020-01-02"
    需要返回数字或"2020-01-01"类型的字符串
    """
    express = express.strip()
    if re.match(r"^\d{4}-\d{2}-\d{2}$|^\d{4}/\d{2}/\d{2}$", express):
        return 200, "success", express.replace("/", "-")
    elif "+" in express:
        express_list = express.split("+")
        if len(express_list) != 2:
            return 400, f"the length of calculation [{express}] must be 2", 0
        if express_list[0].isdigit():  # 简单的数字加减
            result = int(express_list[0])+int(express_list[1])
        else:  # 走时间处理的过程
            result = parse_date_add_or_sub(express_list[0], "+", express_list[1])

    elif "-" in express:
        express_list = express.split("-")
        if len(express_list) != 2:
            return 400, f"the length of calculation [{express}] must be 2", 0
        if express_list[0].isdigit():  # 简单的数字加减
            result = int(express_list[0]) - int(express_list[1])
        else:  # 走时间处理的过程
            result = parse_date_add_or_sub(express_list[0], "-", express_list[1])
    else:
        if not express.isdigit():  # 不是时间格式，没有+-，不是数字
            return 400, f"unsupported calculator [{express}]", 0
        return 200, "success", int(express)
    return 200, "success", result


def parse_judge(express):
    if "==" in express:
        pre, post = express.split("==")
        return 200, "success", pre == post
    elif "<" in express:
        pre, post = express.split("<")
        if not pre.isdigit() or not post.isdigit():
            return 400, "if use <, the ones must be numbers", {}
        return 200, "success", int(pre) < int(post)
    elif ">" in express:
        pre, post = express.split(">")
        if not pre.isdigit() or not post.isdigit():
            return 400, "if use >, the ones must be numbers", {}
        return 200, "success", int(pre) > int(post)
    elif "<=" in express:
        pre, post = express.split("<=")
        if not pre.isdigit() or not post.isdigit():
            return 400, "if use <=, the ones must be numbers", {}
        return 200, "success", int(pre) <= int(post)
    elif ">=" in express:
        pre, post = express.split(">=")
        if not pre.isdigit() or not post.isdigit():
            return 400, "if use >=, the ones must be numbers", {}
        return 200, "success", int(pre) >= int(post)
    return 400, f"unsupported calculator [{express}]", {}
