# -*- coding: utf-8 -*-
import datetime


def xfj_xx(conn, sql):
    try:
        # conn = pymysql.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWD, port=DB_PORT, db=DB_DBNAME, charset='utf8')
        cur = conn.cursor()       # 建立游标
        sql = sql + " limit 20"
        cur.execute(sql)
        return cur
    except Exception as e:
        print(e)


def run(fx_pymysql, start, end, query, query_date, **kwargs):
    # day = (request.args['day']).split(",")
    # s_time = day[0].strip("[")
    # e_time = day[1].strip("]")
    # query = request.args.get('query', '来信')
    s_time = start.split()[0]
    e_time = end.split()[0]
    sql_qhauth_qh = kwargs.get("sql_qhauth_qh")
    qh = sql_qhauth_qh.replace("'", "").replace("qh","").replace("=","").strip()


    # query = "('" + query + "')" if query != '网信' else ('网上投诉', '网信', '领导信箱')
    s_time1 = datetime.datetime.strptime(s_time, "%Y-%m-%d")
    e_time1 = datetime.datetime.strptime(e_time, "%Y-%m-%d")
    # query_date = request.args.get('query_date', 'xfrq')
    query_date = 'xfrq' if query_date == '信访日期' else 'djsj'
    xfxssql = "select xfjbh, xfxsmc, nrflmc, djjgmc,wtsdmc ,xfrs, cfxfbz, xfrq,djsj from xf_xfjxx  where xfxsmc = '%s' and %s  between '%s' and '%s'" % (query, query_date, s_time1, e_time1) + f" and wtsdmc like '%{qh}%'"
    xfxssql_wx = "select xfjbh, xfxsmc, nrflmc, djjgmc,wtsdmc ,xfrs, cfxfbz, xfrq,djsj from xf_xfjxx  where xfxsmc != '来信' and xfxsmc != '来访' and %s  between '%s' and '%s'" % (query_date, s_time1, e_time1) + f" and wtsdmc like '%{qh}%'"
    wtsd_sql = "select xfjbh, xfxsmc, nrflmc, djjgmc,wtsdmc ,xfrs, cfxfbz, xfrq,djsj from xf_xfjxx  where wtsdmc like '%s' and %s  between '%s' and '%s'" % (
        '%' + query + '%', query_date, s_time1, e_time1)
    nrfl_sql = "select xfjbh, xfxsmc, nrflmc, djjgmc,wtsdmc ,xfrs, cfxfbz, xfrq,djsj from xf_xfjxx  where nrflmc like '%s' and %s  between '%s' and '%s'" % (
        query + '%', query_date, s_time1, e_time1) + f" and wtsdmc like '%{qh}%'"
    map = {'xfjbh': '信访件编号', 'xfxs': '信访形式', 'nrfl': '内容分类', 'djjg': '登记机构', 'wtsd': '问题属地', 'xfrs': '信访人数', 'cfxfbz': '是否重复件', 'xfrq': '信访日期', 'djrq': '登记日期'}
    xf_dict = {}
    data = []
    if query in ('来信', '来访', '网信'):
        cur = xfj_xx(fx_pymysql, xfxssql_wx) if query == "网信" else xfj_xx(fx_pymysql, xfxssql)
    elif '市' in query or "县" in query or "区" in query or "镇" in query:
        cur = xfj_xx(fx_pymysql, wtsd_sql)
    else:
        cur = xfj_xx(fx_pymysql, nrfl_sql)
    res = cur.fetchall()  # 获取结果
    for i in res:
        xf_dict['xfjbh'] = i[0]
        xf_dict['xfxs'] = i[1]
        xf_dict['nrfl'] = (i[2]).replace('/', '_')
        xf_dict['djjg'] = i[3]
        xf_dict['wtsd'] = i[4]
        xf_dict['xfrs'] = i[5]
        xf_dict['cfxfbz'] = '初件' if i[6] == 0 else '重件'
        xf_dict['xfrq'] = str(i[7])
        xf_dict['djrq'] = str(i[8])[0:11]
        data.append(xf_dict)

    result = {'mapping': map, 'data': data}
    return 200, "success", result


if __name__ == '__main__':
    query = "来信来访网信/某个一级内容/市县"
    query_date = "信访日期/登记日期"
    day = "[]"