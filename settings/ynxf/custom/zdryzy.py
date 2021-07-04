import datetime
import json

table_xwzs = "xf_xfr_cm_zjhm_xm_xfxwzs"
table_yy = "xf_xfr_cy_zjhm_xm_yy_xfjc"


def get_data(conn, sql):
    try:
        # conn = pymysql.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWD, port=DB_PORT, db=DB_DBNAME, charset='utf8')
        cur = conn.cursor()       # 建立游标
        cur.execute(sql)
        res = cur.fetchall()
        if res:
            res = res[0][0] or 0
        else:
            res = 0
        return res
    except Exception as e:
        return 0


def get_table_data(conn, table, year, month, zjhm):
    index = table.split("_")[-1]
    sql = f"select {index} from {table} where year={year} and month={month} and zjhm='{zjhm}'"
    return get_data(conn, sql)


def get_yearmonth(year, month):  # month 和 year 需要用整数类型
    if month == 1:
        month_last3 = 10
        month_last2 = 11
        month_last1 = 12
        year_last3 = year-1
        year_last2 = year-1
        year_last1 = year-1
    elif month == 2:
        month_last3 = 11
        month_last2 = 12
        month_last1 = 1
        year_last3 = year-1
        year_last2 = year-1
        year_last1 = year
    elif month == 3:
        month_last3 = 12
        month_last2 = 1
        month_last1 = 2
        year_last3 = year-1
        year_last2 = year
        year_last1 = year

    else:
        month_last3 = month-3
        month_last2 = month-2
        month_last1 = month-1
        year_last3 = year
        year_last2 = year
        year_last1 = year
    return year_last3, month_last3, year_last2, month_last2, year_last1, month_last1


def get_yj(zb_pymysql, year, month, zjhm):
    year_last3, month_last3, year_last2, month_last2, year_last1, month_last1 = get_yearmonth(int(year), int(month))
    present_data = get_table_data(zb_pymysql, table_xwzs, year, month, zjhm)
    last1_data = get_table_data(zb_pymysql, table_xwzs, year_last1, month_last1, zjhm)
    last2_data = get_table_data(zb_pymysql, table_xwzs, year_last2, month_last2, zjhm)
    last3_data = get_table_data(zb_pymysql, table_xwzs, year_last3, month_last3, zjhm)

    if present_data > last1_data > last2_data > last3_data:
        return ("连续三个月呈上涨趋势，进行 ", "形势预警")
    else:
        return ("指数平稳",)


def run(fx_pymysql, zb_pymysql, month, year, zjhm, **kwargs):
    # 处理时间
    data_time = f"{year}年{month}月"
    # 处理指数
    data_fxzs = round(get_table_data(zb_pymysql, table_xwzs, year, month, zjhm),2)
    # 处理预警
    data_yj = get_yj(zb_pymysql, year, month, zjhm)
    # 处理概要[目前只有扬言]
    data_yy = get_table_data(zb_pymysql, table_yy, year, month, zjhm)

    # 包装指数
    wrapper_fxzs = f'<span style="color: rgb(243, 73, 141);font-weight: bold;padding: 0px 2px;font-size: 18px;line-height: 30px;">{data_fxzs}</span>'
    # 包装预警
    if len(data_yj) == 2: # 需要预警
        wrapper_yj = f'<span style="color: rgb(0, 228, 255); font-size: 18px; line-height: 30px;">{data_yj[0]}<span style="color: rgb(243, 73, 141); font-weight: bold; padding: 0px 2px;font-size: 18px;line-height: 30px;">{data_yj[1]}</span></span>'
    else:
        wrapper_yj = f'<span style="color: rgb(0, 228, 255); font-size: 18px; line-height: 30px;">{data_yj[0]}</span>'
    # 包装概要
    wrapper_gy = f'<p style="color: rgb(0, 228, 255); font-size: 18px; line-height: 30px;">扬言<span style="color: rgb(243, 73, 141); font-weight: bold; padding: 0px 2px;font-size: 18px;line-height: 30px;">{data_yy}</span>次</p>' \
                 # f'<p style="color: rgb(0, 228, 255); font-size: 18px; line-height: 30px;">扬言<span style="color: rgb(243, 73, 141); font-weight: bold; padding: 0px 2px;font-size: 18px;line-height: 30px;">{data_yy}</span>次</p>'

    data = [
        {"name": "时间", "value": data_time},
        {"name": "分析指数", "value": wrapper_fxzs},
        {"name": "指数预警", "value": wrapper_yj},
        {"name": "信访行为", "value": wrapper_gy+wrapper_gy},
    ]
    result = {"data": data}
    return 200, "success", result