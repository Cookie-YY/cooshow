sql_1_1_all = """(SELECT
	r.region_name,
	t.xfxs xfxs,
	r.region_code,-- 总件次
	count( t.xfjbh ) AS zjc,-- 初件次
	count( CASE WHEN t.check_flag = 0 THEN t.xfjbh END ) AS cjc,-- 重复件次
	count( CASE WHEN t.check_flag <> 0 THEN t.xfjbh END ) AS cfjc 
FROM
	rpt_region r
	LEFT JOIN (
SELECT DISTINCT
	( x.xfjbh ) AS xfjbh,
	x.xfxsmc AS xfxs,
	substr( ( CASE WHEN x.zjqxdm LIKE '44%%' THEN x.zjqxdm ELSE x.wtsddm END ), 1, 4 ) AS wtsddm,
	x.xfrs,
	x.check_flag 
FROM
	rpt_xfjxx x 
WHERE
	x.djsj >= '{start}' -- 参数3 终了时间end
	
	AND x.djsj < '{end}' -- 参数4 登记机构类别
	
	AND x.djjglbdm IN ( '0000', '0100', '0200', '0300', '1000', '1100', '1200', '1300', '1400' ) -- 统计范围(是否本机构)
-- 参数5 信访形式\
-- 参数6,7 信访人数
	
	AND x.xfrs >= 1 
	AND x.xfrs <= 9999 
	AND x.xfxsdm IN ( '100', '200', '300', '303' ) 
	) t --  8 wtsd 拼接'00000000'
	ON r.region_code = concat( t.wtsddm, '00000000' ) 
	WHERE--  9 wtsd  '13%%'
	r.region_code LIKE '44__00000000%%' 
GROUP BY
	r.region_code,
	xfxs)"""

sql_1_1_xfxs = """(SELECT
	r.region_name,
	t.xfxs xfxs,
	r.region_code,-- 总件次
	count( t.xfjbh ) AS zjc,-- 初件次
	count( CASE WHEN t.check_flag = 0 THEN t.xfjbh END ) AS cjc,-- 重复件次
	count( CASE WHEN t.check_flag <> 0 THEN t.xfjbh END ) AS cfjc 
FROM
	rpt_region r
	LEFT JOIN (
SELECT DISTINCT
	( x.xfjbh ) AS xfjbh,
	x.xfxsmc AS xfxs,
	substr( ( CASE WHEN x.zjqxdm LIKE '44%%' THEN x.zjqxdm ELSE x.wtsddm END ), 1, 4 ) AS wtsddm,
	x.xfrs,
	x.check_flag 
FROM
	rpt_xfjxx x 
WHERE
	x.djsj >= '{start}' -- 参数3 终了时间end
	
	AND x.djsj < '{end}' -- 参数4 登记机构类别
	
	AND x.djjglbdm IN ( '0000', '0100', '0200', '0300', '1000', '1100', '1200', '1300', '1400' ) -- 统计范围(是否本机构)
-- 参数5 信访形式\
-- 参数6,7 信访人数
	
	AND x.xfrs >= 1 
	AND x.xfrs <= 9999 
	AND x.xfxsdm IN ( '100', '200', '300', '303' ) 
	) t --  8 wtsd 拼接'00000000'
	ON r.region_code = concat( t.wtsddm, '00000000' ) 
	WHERE--  9 wtsd  '13%%'
	r.region_code LIKE '44__00000000%%' 
GROUP BY
	r.region_code,
	xfxs)"""

sql_1_2_all = """(SELECT
	r.region_name,
	r.region_code,
CASE
		
		WHEN instr( r.region_code, '0000000000' ) > 0 THEN
		'省级' 
		WHEN instr( r.region_code, '00000000' ) > 0 THEN
		'市级' 
		WHEN instr( r.region_code, '000000' ) > 0 THEN
		'县级' 
	END bmjb,
	count( t.xfjbh ) AS zjc,
	count( CASE WHEN t.check_flag = 0 THEN t.xfjbh END ) AS cjc,
	count( CASE WHEN t.check_flag <> 0 THEN t.xfjbh END ) AS cfjc 
FROM
	rpt_region r
	LEFT JOIN (
	SELECT DISTINCT
		( x.xfjbh ) AS xfjbh,
		substr( ( CASE WHEN x.zjqxdm LIKE '44%' THEN x.zjqxdm ELSE x.wtsddm END ), 1, 6 ) AS wtsddm,
		x.xfrs,
		x.check_flag 
	FROM
		rpt_xfjxx x 
	WHERE
		x.djsj >= '{start}' 
		AND x.djsj < '{end}' 
		AND x.djjglbdm IN ( '0000', '0100', '0200', '0300', '1000', '1100', '1200', '1300', '1400' ) 
		AND x.xfrs >= 1 
		AND x.xfrs <= 9999 
		AND x.xfxsdm IN ( '100', '200', '300', '303' ) 
	) t ON r.region_code = concat( t.wtsddm, '000000' ) 
WHERE
	r.region_code LIKE '44____000000%%' 
GROUP BY
	r.region_code)"""


sql_1_2_xfxs = """(SELECT
	r.region_name,
	r.region_code,
CASE
		
		WHEN instr( r.region_code, '0000000000' ) > 0 THEN
		'省级' 
		WHEN instr( r.region_code, '00000000' ) > 0 THEN
		'市级' 
		WHEN instr( r.region_code, '000000' ) > 0 THEN
		'县级' 
	END bmjb,
	t.xfxs xfxs,
	count( t.xfjbh ) AS zjc,
	count( CASE WHEN t.check_flag = 0 THEN t.xfjbh END ) AS cjc,
	count( CASE WHEN t.check_flag <> 0 THEN t.xfjbh END ) AS cfjc 
FROM
	rpt_region r
	LEFT JOIN (
	SELECT DISTINCT
		( x.xfjbh ) AS xfjbh,
		x.xfxsmc AS xfxs,
		substr( ( CASE WHEN x.zjqxdm LIKE '44%' THEN x.zjqxdm ELSE x.wtsddm END ), 1, 6 ) AS wtsddm,
		x.xfrs,
		x.check_flag 
	FROM
		rpt_xfjxx x 
	WHERE
		x.djsj >= '{start}}' 
		AND x.djsj < '{end}' 
		AND x.djjglbdm IN ( '0000', '0100', '0200', '0300', '1000', '1100', '1200', '1300', '1400' ) 
		AND x.xfrs >= 1 
		AND x.xfrs <= 9999 
		AND x.xfxsdm IN ( '100', '200', '300', '303' ) 
	) t ON r.region_code = concat( t.wtsddm, '000000' ) 
WHERE
	r.region_code LIKE '44____000000%%'
GROUP BY
	r.region_code,
	xfxs)"""
