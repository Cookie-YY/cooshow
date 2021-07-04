import pandas as pd
import json
import datetime

debug = True
table_fsf = "xf_xfjxx"
sql_cs = """
select * from 
(SELECT a.xfxsmc, a.nrflmc, a.xm, a.xfmdmc, a.wtsdmc, a.xfrq, a.xfjztmc, b.cs, 
	CASE 
		WHEN b.cs = 1 THEN '1次'
		WHEN b.cs BETWEEN 2 AND 5 THEN '2-5次'
		WHEN b.cs BETWEEN 6 AND 10 THEN '6-10次'
		WHEN b.cs BETWEEN 11 AND 30 THEN '11-30次'
		WHEN b.cs BETWEEN 31 AND 50 THEN '31-50次'
		WHEN b.cs > 50 THEN '50次以上'
	END as csrange
FROM xf_xfjxx a INNER JOIN (
SELECT
	count(id) as cs,
	repeated_id,
	djsj 
FROM
	xf_xfjxx 
WHERE
	djsj >= '{start}' 
	AND djsj <= '{end}' 
 	{jjf_or_fsf_sql_cond}
	AND djjglbdm = '0000' 
	AND wtsddm LIKE '53%'
	AND repeated_id is not null
GROUP BY djsj, repeated_id) b
ON a.repeated_id=b.repeated_id
) t
WHERE t.csrange='{query}'
ORDER BY t.cs desc"""
sql_rs = """
SELECT * FROM (
SELECT
	xfrs,xfxsmc,nrflmc,xm,xfmdmc,wtsdmc,xfrq,xfjztmc,
	CASE 
		WHEN xfrs = 1 THEN '1人'
		WHEN xfrs BETWEEN 2 AND 5 THEN '2-5人'
		WHEN xfrs BETWEEN 6 AND 10 THEN '6-20人'
		WHEN xfrs BETWEEN 31 AND 50 THEN '21-50人'
		WHEN xfrs > 50 THEN '50人以上'
	END as rsrange
FROM
	xf_xfjxx 
WHERE
	djsj >= '{start}' 
	AND djsj <= '{end}' 
    {jjf_or_fsf_sql_cond}
	AND djjglbdm = '0000' 
	AND wtsddm LIKE '53%'
	AND xfrs is not null) a WHERE a.rsrange = '{query}'
"""

mapping_ch = {"xfxsmc": "信访形式", "nrflmc": "内容分类", "xm": "信访人姓名", "xfjztmc": "信访件状态",
              "xfmdmc": "信访目的", "wtsdmc": "问题属地", "xfrq": "信访日期",
              "cs": "重复访次数", "csrange": "重复访次数段", "xfrs": "信访人数", "rsrange": "信访人数段"}

def run(fx_pymysql, fx_engine, start, end, query, query_level, **kwargs):
    start = start.split()[0]
    end = end.split()[0]
    sql_cs_or_rs = sql_cs if "次" in query else sql_rs
    if debug:
        jjf_or_fsf_sql_cond = ""
    else:
        jjf_or_fsf_sql_cond = "AND djjgdm = '5300000000000000299' " if query_level == "fsf" else "AND djjgdm = '0000000000000020119' "

    sql = sql_cs_or_rs.format(start=start, end=end, query=query, jjf_or_fsf_sql_cond=jjf_or_fsf_sql_cond).replace("%", "%%")
    try:
        data = fx_engine.execute(sql+" limit 20")
        columns = data.keys()
        df = pd.DataFrame(data.fetchall(), columns=columns)
        df["nrflmc"] = df["nrflmc"].apply(lambda x: x.split("/")[0])
        df["xfrq"] = df["xfrq"].apply(lambda x: str(x))
        data = df.to_json(orient='records', force_ascii=False)
        data = json.loads(data)
        mapping = dict(zip(columns, [mapping_ch.get(i) for i in columns]))
    except Exception as e:
        return 400, f"There must be some error while search fx_db {e}", {}

    result = {'mapping': mapping, 'data': data}
    return 200, "success", result
