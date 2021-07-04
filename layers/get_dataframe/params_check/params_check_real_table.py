import re
from sqlalchemy import Table
from werkzeug.exceptions import abort

from utils.error_page import InvalidUsage


def get_table_when_table(table, realm, busin, timetype, qh, lx, index):
    if realm:  # pass
        pass
    if busin:  # pass
        pass
    if timetype:  # cm/cy之间的变动
        table = table.replace("_cm", f'_{timetype}').replace("_cy", f'_{timetype}')
    if qh:  # shej/shij/xj之间的变动
        table = table.replace("_shej", f'_{qh}').replace("_shij", f'_{qh}').replace("_xj", f'_{qh}')
    if lx:  # pass
        pass
    if index:  # 肯定是最后一个有变动：zb/tb/hb除外
        if not table.startswith("search"):
            components = table.split("_")
            if table.endswith("_zb") or table.endswith("_tb") or table.endswith("_hb"):
                table = f'{"_".join(components[:-2])}_{index}'
            else:
                table = f'{"_".join(components[:-1])}_{index}'
    return table


def get_candidate_tables(apis_copy):
    table, realm, busin, timetype, qh, lx, index = apis_copy.get("table", ""), \
                                                   apis_copy.get("realm", ""), \
                                                   apis_copy.get("busin", ""), \
                                                   apis_copy.get("timetype", ""), \
                                                   apis_copy.get("qh", ""), \
                                                   apis_copy.get("lx", ""), \
                                                   apis_copy.get("index", "")
    # qh=shej但是库里没有shej    qh是空，但是库里有shej
    # index 有_zb，但是库里没有 _zb    qh没有zb但是库里有占比

    # table: 如果存在table参数，table指定唯一的表
    if table:
        table = get_table_when_table(table, realm, busin, timetype, qh, lx, index)
        return [table]

    shej = ["shej", ""]
    index_list = [index.replace("_zb", ""), index.replace("_zb", "") + "_zb"]
    qh_theother = "none"
    if qh in shej:
        shej.remove(qh)
        qh_theother = shej[0]

    index_list.remove(index)
    index_theother = index_list[0]

    table1 = f"{realm}_{busin}_{timetype}_{qh}_{lx}_{index}"
    table3 = f"{realm}_{busin}_{timetype}_{qh}_{lx}_{index_theother}"
    table1 = re.sub(r'_+', '_', table1)
    table3 = re.sub(r'_+', '_', table3)
    if qh_theother != "none":
        table2 = f"{realm}_{busin}_{timetype}_{qh_theother}_{lx}_{index}"
        table4 = f"{realm}_{busin}_{timetype}_{qh_theother}_{lx}_{index_theother}"
        table2 = re.sub(r'_+', '_', table2)
        table4 = re.sub(r'_+', '_', table4)
        return [table1, table2, table3, table4]

    return [table1, table3]


def get_real_table(apis_copy):
    db_engine = apis_copy.get("db_engine")
    candidate_tables = get_candidate_tables(apis_copy)
    from utils.db_connection import metadata
    if db_engine == "zb_db":
        from utils.db_connection import zb_engine as engine
    else:
        from utils.db_connection import fx_engine as engine
    metadata.reflect(bind=engine)
    tables = metadata.tables.keys()
    for table in candidate_tables:
        if table in tables:
            ex_table = Table(table, metadata, autoload=True, autoload_with=engine)
            return 200, "success", {"table": table, "ex_table": ex_table}

    from app import app
    if not app.config.get("NOTABLE_ERROR", True):
        return 200, f"NoSuchTableError: ater trying all of the candidate tables, nothing found {candidate_tables}", {"table": "test", "ex_table": "test"}
    return 400, f"NoSuchTableError: ater trying all of the candidate tables, nothing found {candidate_tables}", {}
