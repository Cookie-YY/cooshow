sql_1_1_all = """(SELECT
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
		substr( ( CASE WHEN x.zjqxdm LIKE '44%%' THEN x.zjqxdm ELSE x.wtsddm END ), 1, 4 ) AS wtsddm,
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
		AND x.sfssbz = 0
	) t ON r.region_code = concat( t.wtsddm, '00000000' ) 
WHERE
	r.region_code LIKE '44__00000000%%' 
GROUP BY
	r.region_code)"""

sql_1_1_xfxs = """(SELECT
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
CASE
		WHEN (t.xfxsmc = '来信' OR t.xfxsmc = '来访' ) THEN
		t.xfxsmc 
		WHEN t.xfxsmc IS NULL THEN
		NULL ELSE '网信' 
	END xfxs,
	count( t.xfjbh ) AS zjc,
	count( CASE WHEN t.check_flag = 0 THEN t.xfjbh END ) AS cjc,
	count( CASE WHEN t.check_flag <> 0 THEN t.xfjbh END ) AS cfjc 
FROM
	rpt_region r
	LEFT JOIN (
	SELECT DISTINCT
		( x.xfjbh ) AS xfjbh,
		x.xfxsmc AS xfxsmc,
		substr( ( CASE WHEN x.zjqxdm LIKE '44%%' THEN x.zjqxdm ELSE x.wtsddm END ), 1, 4 ) AS wtsddm,
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
		AND x.sfssbz = 0
	) t ON r.region_code = concat( t.wtsddm, '00000000' ) 
WHERE
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
		substr( ( CASE WHEN x.zjqxdm LIKE '44%%' THEN x.zjqxdm ELSE x.wtsddm END ), 1, 6 ) AS wtsddm,
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
		AND x.sfssbz = 0
	) t ON r.region_code = concat( t.wtsddm, '000000' ) 
WHERE
	r.region_code LIKE '44____000000%%' 
	AND substr( r.region_code, 1, 4 ) = ( SELECT substr( region_code, 1, 4 ) FROM rpt_region WHERE region_name = '{Cqh}' ) 
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
CASE
		
		WHEN ( t.xfxsmc = '来信' OR t.xfxsmc = '来访' ) THEN
		t.xfxsmc 
		WHEN t.xfxsmc IS NULL THEN
		NULL ELSE '网信' 
	END xfxs,
	count( t.xfjbh ) AS zjc,
	count( CASE WHEN t.check_flag = 0 THEN t.xfjbh END ) AS cjc,
	count( CASE WHEN t.check_flag <> 0 THEN t.xfjbh END ) AS cfjc 
FROM
	rpt_region r
	LEFT JOIN (
	SELECT DISTINCT
		( x.xfjbh ) AS xfjbh,
		x.xfxsmc AS xfxsmc,
		substr( ( CASE WHEN x.zjqxdm LIKE '44%%' THEN x.zjqxdm ELSE x.wtsddm END ), 1, 6 ) AS wtsddm,
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
		AND x.sfssbz = 0
	) t ON r.region_code = concat( t.wtsddm, '000000' ) 
WHERE
	r.region_code LIKE '44____000000%%' 
	AND substr( r.region_code, 1, 4 ) = ( SELECT substr( region_code, 1, 4 ) FROM rpt_region WHERE region_name = '{Cqh}' ) 
GROUP BY
	r.region_code,
	xfxs)"""
