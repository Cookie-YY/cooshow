import datetime
import json


table = "xf_xfj_cy_shij_a_abjc_acjc_adjc_bcjc_bdjc_cdjc"
name_a = "一般信访行为"
name_b = "到省访"
name_c = "非接待地区到省访"
name_d = "非接待地区进京访"

def get_yj_summary_template(from_, to_, zhl, jb):
    if jb == 1:  # 最强：红色
        return f"""<p style="font-size: 18px;
          color: #fff;line-height: 30px;">
            <b style="color: #ff0010;">{from_}</b>
            转化为 <b style="color: #ff0010;">{to_}</b>转化率为 <b style="color: #ff0010;">{zhl*100}%</b>，实施 <b style="color: #ff0010;">红色预警</b>
            </p >"""
    elif jb == 2:  # 次之: 橙色
        return f"""<p style="font-size: 18px;
          color: #fff;line-height: 30px;">
            <b style="color: #fe5e00;">{from_}</b>
            {to_} <b style="color: #fe5e00;">到省访</b>转化率为 <b style="color: #fe5e00;">{zhl*100}%</b>，实施 <b style="color: #fe5e00;">橙色预警</b>
            </p >
        """
    elif jb == 3:           # 最弱: 蓝色
        return f"""<p style="font-size: 18px;
          color: #fff;line-height: 30px;">
              <b style="color: #2a5cfd;">{from_}</b>
            转化为 <b style="color: #2a5cfd;">{to_}</b>转化率为 <b style="color: #2a5cfd;">{zhl*100}%</b>，实施 <b style="color: #2a5cfd;">蓝色预警</b>
            </p >  """
    else:
        return ""


def get_yj_summary(from_, to_, zhl):
    jb = 0
    if zhl > 0.12:
        jb = 1
    elif zhl > 0.05:
        jb = 2
    elif zhl > 0.03:
        jb = 3
    return get_yj_summary_template(from_, to_, zhl, jb)


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


def get_table_data(conn, table, index, year, shij_02):
    # index = table.split("_")[-1]
    sql = f"select {index} from {table} where year={year} and shij_02='{shij_02}'"
    return get_data(conn, sql)


def get_loudou(zb_pymysql, year, shij_02):
    """
    获取柱子漏斗的方法
    """
    a = get_table_data(zb_pymysql, table, "a", year, shij_02)
    ab = get_table_data(zb_pymysql, table, "abjc", year, shij_02)
    ac = get_table_data(zb_pymysql, table, "acjc", year, shij_02)
    bc = get_table_data(zb_pymysql, table, "bcjc", year, shij_02)
    ad = get_table_data(zb_pymysql, table, "adjc", year, shij_02)
    bd = get_table_data(zb_pymysql, table, "bdjc", year, shij_02)
    cd = get_table_data(zb_pymysql, table, "cdjc", year, shij_02)

    from app import app
    sig = app.config.get("SIGNIFICANT_DIGITS", 4)
    # 点击a
    a = a
    yj_a = ""
    # 点击b
    b = ab
    a2b = round(ab/a, 4) if a!=0 else 0
    yj_a2b = get_yj_summary(name_a, name_b, a2b)
    yj_b = yj_a2b
    # 点击c
    c = ac + bc
    a2c = round(ac/a, 4) if a!=0 else 0
    b2c = round(bc/b, 4) if b!=0 else 0
    yj_a2c = get_yj_summary(name_a, name_c, a2c)
    yj_b2c = get_yj_summary(name_a, name_c, b2c)
    yj_c = yj_a2c + yj_b2c
    # 点击d
    d = ad + bd + cd
    a2d = round(ad/a, 4) if a!=0 else 0
    b2d = round(bd/b, 4) if b!=0 else 0
    c2d = round(cd/c, 4) if c!=0 else 0

    yj_a2d = get_yj_summary(name_a, name_d, a2d)
    yj_b2d = get_yj_summary(name_b, name_d, b2d)
    yj_c2d = get_yj_summary(name_c, name_d, c2d)
    yj_d = yj_a2d + yj_b2d + yj_c2d

    return [
        {"name": name_a, "value": a, "yj": yj_a},
        {"name": name_b, "value": b, "yj": yj_b},
        {"name": name_c, "value": c, "yj": yj_c},
        {"name": name_d, "value": d, "yj": yj_d},
    ]


def run(fx_pymysql, zb_pymysql, year, shij_02="昆明市", **kwargs):
    data = get_loudou(zb_pymysql, year, shij_02)
    result = {"data": data}
    return 200, "success", result