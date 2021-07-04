sql_3_2_all = """(SELECT
	r.region_name,
	r.region_code,
	count( DISTINCT ( t.xfjbh ) ) AS ydfzs,
	count( DISTINCT ( CASE WHEN t.bjbz = 1 THEN t.xfjbh END ) ) AS ydf,
	count( DISTINCT ( CASE WHEN ( t.bjbz = 1 AND t.bjsj <= t.xbjzsj ) THEN t.xfjbh END ) ) AS aqdf,
	count( DISTINCT ( CASE WHEN ( t.bjbz = 1 AND t.bjsj > t.xbjzsj ) THEN t.xfjbh END ) ) AS cqdf,
	count( DISTINCT ( CASE WHEN t.bjbz = 0 AND SYSDATE( ) <= t.xbjzsj THEN t.xfjbh END ) ) AS wdf,
	count( DISTINCT ( CASE WHEN t.bjbz = 0 AND SYSDATE( ) > t.xbjzsj THEN t.xfjbh END ) ) AS cqwdf 
FROM
	rpt_region r
	LEFT JOIN (
	SELECT DISTINCT
		( x.xfjbh ) AS xfjbh,
	CASE
			
			WHEN x.xfxsmc = '来信' THEN
			'来信' 
			WHEN x.xfxsmc = '来访' THEN
			'来访' ELSE '网信' 
		END xfxs,
	substr( IFNULL( x.zjqxdm, x.wtsddm ), 1, 4 ) AS wtsddm,
	x.ddzrdwsj,
	x.zrdwslsj,
	x.bjbz,
	x.xbjzsj,
	x.bjsj,
	x.dfsj 
FROM
	rpt_xfjxx x
	LEFT JOIN xf_dbxx e ON e.xfjbh = x.xfjbh
	LEFT JOIN xf_ybinfo y ON x.xfjbh = y.xfjbh 
WHERE
	1 = 1 
	AND x.xbjzsj >= '{start}' 
	AND x.xbjzsj <= '{end}' 
	AND x.djjglbdm IN ( '0000', '0100', '0200', '0300', '1000', '1100', '1200', '1300', '1400' ) 
	AND x.xfrs >= 1 
	AND x.xfrs <= 9999 
	AND x.check_flag = 0 
	AND x.sfnrtj = 1 
	AND x.xfxsdm IN ( '100', '200', '300', '303' ) 
	AND x.sfssbz = 0 
	) t ON r.region_code = concat( t.wtsddm, '00000000' ) 
WHERE
	r.region_code LIKE '44__00000000%%' 
GROUP BY
	r.region_code
)"""

sql_3_2_xfxs = """(SELECT
	r.region_name,
	r.region_code,
	xfxs,
	count( DISTINCT ( t.xfjbh ) ) AS ydfzs,
	count( DISTINCT ( CASE WHEN t.bjbz = 1 THEN t.xfjbh END ) ) AS ydf,
	count( DISTINCT ( CASE WHEN ( t.bjbz = 1 AND t.bjsj <= t.xbjzsj ) THEN t.xfjbh END ) ) AS aqdf,
	count( DISTINCT ( CASE WHEN ( t.bjbz = 1 AND t.bjsj > t.xbjzsj ) THEN t.xfjbh END ) ) AS cqdf,
	count( DISTINCT ( CASE WHEN t.bjbz = 0 AND SYSDATE( ) <= t.xbjzsj THEN t.xfjbh END ) ) AS wdf,
	count( DISTINCT ( CASE WHEN t.bjbz = 0 AND SYSDATE( ) > t.xbjzsj THEN t.xfjbh END ) ) AS cqwdf 
FROM
	rpt_region r
	LEFT JOIN (
	SELECT DISTINCT
		( x.xfjbh ) AS xfjbh,
	CASE
			
			WHEN x.xfxsmc = '来信' THEN
			'来信' 
			WHEN x.xfxsmc = '来访' THEN
			'来访' ELSE '网信' 
		END xfxs,
	substr( IFNULL( x.zjqxdm, x.wtsddm ), 1, 4 ) AS wtsddm,
	x.ddzrdwsj,
	x.zrdwslsj,
	x.bjbz,
	x.xbjzsj,
	x.bjsj,
	x.dfsj 
FROM
	rpt_xfjxx x
	LEFT JOIN xf_dbxx e ON e.xfjbh = x.xfjbh
	LEFT JOIN xf_ybinfo y ON x.xfjbh = y.xfjbh 
WHERE
	1 = 1 
	AND x.xbjzsj >= '{start}' 
	AND x.xbjzsj <= '{end}' 
	AND ( CASE x.xfxsmc WHEN '来信' THEN '来信' WHEN '来访' THEN '来访' ELSE '网信' END ) = '{xfxs}' 
	AND x.djjglbdm IN ( '0000', '0100', '0200', '0300', '1000', '1100', '1200', '1300', '1400' ) 
	AND x.xfrs >= 1 
	AND x.xfrs <= 9999 
	AND x.check_flag = 0 
	AND x.sfnrtj = 1 
	AND x.xfxsdm IN ( '100', '200', '300', '303' ) 
	AND x.sfssbz = 0 
	) t ON r.region_code = concat( t.wtsddm, '00000000' ) 
WHERE
	r.region_code LIKE '44__00000000%%' 
GROUP BY
	r.region_code,
	xfxs
)"""

sql_3_4_all = """(SELECT
	r.region_name,
	r.region_code,
	count( DISTINCT ( t.xfjbh ) ) AS ydfzs,
	count( DISTINCT ( CASE WHEN t.bjbz = 1 THEN t.xfjbh END ) ) AS ydf,
	count( DISTINCT ( CASE WHEN ( t.bjbz = 1 AND t.bjsj <= t.xbjzsj ) THEN t.xfjbh END ) ) AS aqdf,
	count( DISTINCT ( CASE WHEN ( t.bjbz = 1 AND t.bjsj > t.xbjzsj ) THEN t.xfjbh END ) ) AS cqdf,
	count( DISTINCT ( CASE WHEN t.bjbz = 0 AND SYSDATE( ) <= t.xbjzsj THEN t.xfjbh END ) ) AS wdf,
	count( DISTINCT ( CASE WHEN t.bjbz = 0 AND SYSDATE( ) > t.xbjzsj THEN t.xfjbh END ) ) AS cqwdf 
FROM
	rpt_region r
	LEFT JOIN (
	SELECT DISTINCT
		( x.xfjbh ) AS xfjbh,
	CASE
			
			WHEN x.xfxsmc = '来信' THEN
			'来信' 
			WHEN x.xfxsmc = '来访' THEN
			'来访' ELSE '网信' 
		END xfxs,
	substr( IFNULL( x.zjqxdm, x.wtsddm ), 1, 6 ) AS wtsddm,
	x.ddzrdwsj,
	x.zrdwslsj,
	x.bjbz,
	x.xbjzsj,
	x.bjsj,
	x.dfsj 
FROM
	rpt_xfjxx x
	LEFT JOIN xf_dbxx e ON e.xfjbh = x.xfjbh
	LEFT JOIN xf_ybinfo y ON x.xfjbh = y.xfjbh 
WHERE
	1 = 1 
	AND x.xbjzsj >= '{start}' 
	AND x.xbjzsj <= '{end}' 
	AND x.djjglbdm IN ( '0000', '0100', '0200', '0300', '1000', '1100', '1200', '1300', '1400' ) 
	AND x.xfrs >= 1 
	AND x.xfrs <= 9999 
	AND x.check_flag = 0 
	AND x.sfnrtj = 1 
	AND x.xfxsdm IN ( '100', '200', '300', '303' ) 
	AND x.sfssbz = 0 
	) t ON r.region_code = concat( t.wtsddm, '000000' ) 
WHERE
	r.region_code LIKE '44____000000%%'
GROUP BY
	r.region_code
)"""

sql_3_4_xfxs = """(SELECT
	r.region_name,
	r.region_code,
	xfxs,
	count( DISTINCT ( t.xfjbh ) ) AS ydfzs,
	count( DISTINCT ( CASE WHEN t.bjbz = 1 THEN t.xfjbh END ) ) AS ydf,
	count( DISTINCT ( CASE WHEN ( t.bjbz = 1 AND t.bjsj <= t.xbjzsj ) THEN t.xfjbh END ) ) AS aqdf,
	count( DISTINCT ( CASE WHEN ( t.bjbz = 1 AND t.bjsj > t.xbjzsj ) THEN t.xfjbh END ) ) AS cqdf,
	count( DISTINCT ( CASE WHEN t.bjbz = 0 AND SYSDATE( ) <= t.xbjzsj THEN t.xfjbh END ) ) AS wdf,
	count( DISTINCT ( CASE WHEN t.bjbz = 0 AND SYSDATE( ) > t.xbjzsj THEN t.xfjbh END ) ) AS cqwdf 
FROM
	rpt_region r
	LEFT JOIN (
	SELECT DISTINCT
		( x.xfjbh ) AS xfjbh,
	CASE
			
			WHEN x.xfxsmc = '来信' THEN
			'来信' 
			WHEN x.xfxsmc = '来访' THEN
			'来访' ELSE '网信' 
		END xfxs,
	substr( IFNULL( x.zjqxdm, x.wtsddm ), 1, 6 ) AS wtsddm,
	x.ddzrdwsj,
	x.zrdwslsj,
	x.bjbz,
	x.xbjzsj,
	x.bjsj,
	x.dfsj 
FROM
	rpt_xfjxx x
	LEFT JOIN xf_dbxx e ON e.xfjbh = x.xfjbh
	LEFT JOIN xf_ybinfo y ON x.xfjbh = y.xfjbh 
WHERE
	1 = 1 
	AND x.xbjzsj >= '{start}' 
	AND x.xbjzsj <= '{end}' 
	AND ( CASE x.xfxsmc WHEN '来信' THEN '来信' WHEN '来访' THEN '来访' ELSE '网信' END ) = '{xfxs}' 
	AND x.djjglbdm IN ( '0000', '0100', '0200', '0300', '1000', '1100', '1200', '1300', '1400' ) 
	AND x.xfrs >= 1 
	AND x.xfrs <= 9999 
	AND x.check_flag = 0 
	AND x.sfnrtj = 1 
	AND x.xfxsdm IN ( '100', '200', '300', '303' ) 
	AND x.sfssbz = 0 
	) t ON r.region_code = concat( t.wtsddm, '000000' ) 
WHERE
	r.region_code LIKE '44____000000%%'
GROUP BY
	r.region_code,
	xfxs)"""