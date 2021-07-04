from app import app
import pandas as pd
qh_info = app.config["QH_INFO"]


def get_qh_sub(target, sub="all"):
    if sub == "all":  # 含所有小弟【信访绩效考核】
        if target in qh_info["shej_02"].tolist():
            shij = qh_info["shij_02"].tolist()
            xj = qh_info["xj_02"].tolist()
            return shij + xj
        if target in qh_info["shij_02"].tolist():
            xj = qh_info["xj_02"][qh_info["shij_02"]==target].tolist()
            return xj
        if target in qh_info["xj_02"].tolist():
            return []
    else:  # 只走下面一层是 go_down
        if target in qh_info["shej_02"].tolist():
            shij = qh_info["shij_02"].tolist()
            return shij
        if target in qh_info["shij_02"].tolist():
            xj = qh_info["xj_02"][qh_info["shij_02"]==target].tolist()
            return xj
        if target in qh_info["xj_02"].tolist():
            return [target]


def get_qh_level(target):
    if target in qh_info.get("shej_02", pd.Series()).tolist():
        return "shej_02"
    if target in qh_info.get("shij_02", pd.Series()).tolist():
        return "shij_02"
    if target in qh_info.get("xj_02", pd.Series()).tolist():
        return "xj_02"


def get_qh_levelindex(target):
    return list(qh_info.columns).index(get_qh_level(target))


def get_qh_godown(qh):
    if qh in qh_info["shej_02"].tolist():
        return "shij_02"
    else:
    # if qh in qh_info["shij_02"].tolist():
        return "xj_02"


def get_qh_include_sub(qh, sub="all"):
    return [qh] + get_qh_sub(qh, sub=sub)


def get_qh_with_auth(qh, qh_ceiling, table):
    if qh:
        qh_level, qh_ceiling_level = get_qh_level(qh), get_qh_level(qh_ceiling)
        qh_level_container = list(qh_info.columns)
        if qh_level_container.index(qh_level) <= qh_level_container.index(qh_ceiling_level):
            return qh_ceiling
        return qh
    elif table == "" or ("qh" in table or "shej" in table or "shij" in table or "xj" in "table"):
        if table not in ["search_qh"]:
            return qh_ceiling
    return ""
