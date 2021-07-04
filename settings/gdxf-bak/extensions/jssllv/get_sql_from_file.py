sql_1_2_all = """(SELECT
	r.region_name,
CASE
		
		WHEN instr( r.region_code, '0000000000' ) > 0 THEN
		'省级' 
		WHEN instr( r.region_code, '00000000' ) > 0 THEN
		'市级' 
		WHEN instr( r.region_code, '000000' ) > 0 THEN
		'县级' 
	END bmjb,
	r.region_code,
	count( DISTINCT ( t.xfjbh ) ) AS zs,
	count(
		DISTINCT (
		CASE
				
				WHEN ( t.sjslsj IS NOT NULL OR t.shijslsj IS NOT NULL OR t.xjslsj IS NOT NULL ) THEN
				t.xfjbh 
			END 
			) 
		) AS ysl,
		count(
			DISTINCT (
			CASE
					
					WHEN least(
						ifnull( t.sjslsj, SYSDATE( ) ),
						ifnull( t.shijslsj, SYSDATE( ) ),
						ifnull( t.xjslsj, SYSDATE( ) ) 
					) <= DATE_ADD( t.djsj, INTERVAL 15 DAY ) 
					AND least(
						ifnull( t.sjslsj, SYSDATE( ) ),
						ifnull( t.shijslsj, SYSDATE( ) ),
						ifnull( t.xjslsj, SYSDATE( ) ) 
						) <> SYSDATE( ) THEN
						t.xfjbh 
					END 
					) 
				) AS jssl,
				count(
					DISTINCT (
					CASE
							
							WHEN least(
								ifnull( t.sjslsj, SYSDATE( ) ),
								ifnull( t.shijslsj, SYSDATE( ) ),
								ifnull( t.xjslsj, SYSDATE( ) ) 
							) > DATE_ADD( t.djsj, INTERVAL 15 DAY ) 
							AND least(
								ifnull( t.sjslsj, SYSDATE( ) ),
								ifnull( t.shijslsj, SYSDATE( ) ),
								ifnull( t.xjslsj, SYSDATE( ) ) 
								) <> SYSDATE( ) THEN
								t.xfjbh 
							END 
							) 
						) AS cqsl,
						count(
							DISTINCT (
							CASE
									
									WHEN ( t.sjslsj IS NULL AND t.shijslsj IS NULL AND t.xjslsj IS NULL ) 
									AND SYSDATE( ) > DATE_ADD( t.djsj, INTERVAL 15 DAY ) THEN
										t.xfjbh 
									END 
									) 
								) AS cqwsl 
							FROM
								rpt_region r
								LEFT JOIN (
								SELECT DISTINCT
									x.xfjbh,
								CASE
										
										WHEN x.xfxsmc = '来信' THEN
										'来信' 
										WHEN x.xfxsmc = '来访' THEN
										'来访' ELSE '网信' 
									END xfxs,
					substr( IFNULL( x.zjqxdm, x.wtsddm ), 1, 4 ) AS wtsddm,
					x.sjslsj,
					x.shijslsj,
					x.xjslsj,
					x.ddzrdwsj,
					x.djsj 
				FROM
					rpt_xfjxx x
					LEFT JOIN xf_dbxx e ON e.xfjbh = x.xfjbh
					LEFT JOIN xf_ybinfo y ON x.xfjbh = y.xfjbh 
				WHERE
					1 = 1 
					AND DATE_ADD( x.djsj, INTERVAL 15 DAY ) >= '{start}' 
					AND DATE_ADD( x.djsj, INTERVAL 15 DAY ) <= '{end}' 
					AND x.check_flag = 0 
					AND x.djjglbdm IN ( '0000', '0100', '0200', '0300' ) 
					AND x.xfrs >= 1 
					AND x.xfrs <= 9999 
					AND x.sfnrtj = 1 
					AND x.xfxsdm IN ( '100', '200', '300', '303' ) 
					AND x.sfssbz = 0 
				) t ON r.region_code = concat( t.wtsddm, '00000000' ) 
			WHERE
				r.region_code LIKE '44__00000000%%' 
			GROUP BY
			r.region_code)"""

sql_1_2_xfxs = """(SELECT
	r.region_name,
CASE

		WHEN instr( r.region_code, '0000000000' ) > 0 THEN
		'省级' 
		WHEN instr( r.region_code, '00000000' ) > 0 THEN
		'市级' 
		WHEN instr( r.region_code, '000000' ) > 0 THEN
		'县级' 
	END bmjb,
	r.region_code,
	t.xfxs,
	count( DISTINCT ( t.xfjbh ) ) AS zs,
	count(
		DISTINCT (
		CASE

				WHEN ( t.sjslsj IS NOT NULL OR t.shijslsj IS NOT NULL OR t.xjslsj IS NOT NULL ) THEN
				t.xfjbh 
			END 
			) 
		) AS ysl,
		count(
			DISTINCT (
			CASE

					WHEN least(
						ifnull( t.sjslsj, SYSDATE( ) ),
						ifnull( t.shijslsj, SYSDATE( ) ),
						ifnull( t.xjslsj, SYSDATE( ) ) 
					) <= DATE_ADD( t.djsj, INTERVAL 15 DAY ) 
					AND least(
						ifnull( t.sjslsj, SYSDATE( ) ),
						ifnull( t.shijslsj, SYSDATE( ) ),
						ifnull( t.xjslsj, SYSDATE( ) ) 
						) <> SYSDATE( ) THEN
						t.xfjbh 
					END 
					) 
				) AS jssl,
				count(
					DISTINCT (
					CASE

							WHEN least(
								ifnull( t.sjslsj, SYSDATE( ) ),
								ifnull( t.shijslsj, SYSDATE( ) ),
								ifnull( t.xjslsj, SYSDATE( ) ) 
							) > DATE_ADD( t.djsj, INTERVAL 15 DAY ) 
							AND least(
								ifnull( t.sjslsj, SYSDATE( ) ),
								ifnull( t.shijslsj, SYSDATE( ) ),
								ifnull( t.xjslsj, SYSDATE( ) ) 
								) <> SYSDATE( ) THEN
								t.xfjbh 
							END 
							) 
						) AS cqsl,
						count(
							DISTINCT (
							CASE

									WHEN ( t.sjslsj IS NULL AND t.shijslsj IS NULL AND t.xjslsj IS NULL ) 
									AND SYSDATE( ) > DATE_ADD( t.djsj, INTERVAL 15 DAY ) THEN
										t.xfjbh 
									END 
									) 
								) AS cqwsl 
							FROM
								rpt_region r
								LEFT JOIN (
								SELECT DISTINCT
									x.xfjbh,
								CASE

										WHEN x.xfxsmc = '来信' THEN
										'来信' 
										WHEN x.xfxsmc = '来访' THEN
										'来访' ELSE '网信' 
									END xfxs,
					substr( IFNULL( x.zjqxdm, x.wtsddm ), 1, 4 ) AS wtsddm,
					x.sjslsj,
					x.shijslsj,
					x.xjslsj,
					x.ddzrdwsj,
					x.djsj 
				FROM
					rpt_xfjxx x
					LEFT JOIN xf_dbxx e ON e.xfjbh = x.xfjbh
					LEFT JOIN xf_ybinfo y ON x.xfjbh = y.xfjbh 
				WHERE
					1 = 1 
					AND DATE_ADD( x.djsj, INTERVAL 15 DAY ) >= '{start}' 
					AND DATE_ADD( x.djsj, INTERVAL 15 DAY ) <= '{end}' 
					AND ( CASE x.xfxsmc WHEN '来信' THEN '来信' WHEN '来访' THEN '来访' ELSE '网信' END ) = '{xfxs}' 
					AND x.check_flag = 0 
					AND x.djjglbdm IN ( '0000', '0100', '0200', '0300' ) 
					AND x.xfrs >= 1 
					AND x.xfrs <= 9999 
					AND x.sfnrtj = 1 
					AND x.xfxsdm IN ( '100', '200', '300', '303' ) 
					AND x.sfssbz = 0 
				) t ON r.region_code = concat( t.wtsddm, '00000000' ) 
			WHERE
				r.region_code LIKE '44__00000000%%' 
			GROUP BY
			r.region_code,
	t.xfxs)"""

sql_1_4_all = """(SELECT
	r.region_name,
CASE
		
		WHEN instr( r.region_code, '0000000000' ) > 0 THEN
		'省级' 
		WHEN instr( r.region_code, '00000000' ) > 0 THEN
		'市级' 
		WHEN instr( r.region_code, '000000' ) > 0 THEN
		'县级' 
	END bmjb,
	r.region_code,
	count( DISTINCT ( t.xfjbh ) ) AS zs,-- 已受理
	count(
		DISTINCT (
		CASE
				
				WHEN ( t.sjslsj IS NOT NULL OR t.shijslsj IS NOT NULL OR t.xjslsj IS NOT NULL ) THEN
				t.xfjbh 
			END 
			) 
		) AS ysl,-- 及时受理
		count(
			DISTINCT (
			CASE
					
					WHEN least(
						ifnull( t.sjslsj, SYSDATE( ) ),
						ifnull( t.shijslsj, SYSDATE( ) ),
						ifnull( t.xjslsj, SYSDATE( ) ) 
					) <= DATE_ADD( t.djsj, INTERVAL 15 DAY ) 
					AND least(
						ifnull( t.sjslsj, SYSDATE( ) ),
						ifnull( t.shijslsj, SYSDATE( ) ),
						ifnull( t.xjslsj, SYSDATE( ) ) 
						) <> SYSDATE( ) THEN
						t.xfjbh 
					END 
					) 
				) AS jssl,-- 超期受理
				count(
					DISTINCT (
					CASE
							
							WHEN least(
								ifnull( t.sjslsj, SYSDATE( ) ),
								ifnull( t.shijslsj, SYSDATE( ) ),
								ifnull( t.xjslsj, SYSDATE( ) ) 
							) > DATE_ADD( t.djsj, INTERVAL 15 DAY ) 
							AND least(
								ifnull( t.sjslsj, SYSDATE( ) ),
								ifnull( t.shijslsj, SYSDATE( ) ),
								ifnull( t.xjslsj, SYSDATE( ) ) 
								) <> SYSDATE( ) THEN
								t.xfjbh 
							END 
							) 
						) AS cqsl,-- 超期未受理
						count(
							DISTINCT (
							CASE
									
									WHEN ( t.sjslsj IS NULL AND t.shijslsj IS NULL AND t.xjslsj IS NULL ) 
									AND SYSDATE( ) > DATE_ADD( t.djsj, INTERVAL 15 DAY ) THEN
										t.xfjbh 
									END 
									) 
								) AS cqwsl 
							FROM
								rpt_region r
								LEFT JOIN (
								SELECT DISTINCT
									x.xfjbh,
								CASE
										
										WHEN x.xfxsmc = '来信' THEN
										'来信' 
										WHEN x.xfxsmc = '来访' THEN
										'来访' ELSE '网信' 
									END xfxs,
					substr( IFNULL( x.zjqxdm, x.wtsddm ), 1, 6 ) AS wtsddm,
					x.sjslsj,
					x.shijslsj,
					x.xjslsj,
					x.ddzrdwsj,
					x.djsj 
				FROM
					rpt_xfjxx x
					LEFT JOIN xf_dbxx e ON e.xfjbh = x.xfjbh
					LEFT JOIN xf_ybinfo y ON x.xfjbh = y.xfjbh 
				WHERE
					1 = 1 
					AND DATE_ADD( x.djsj, INTERVAL 15 DAY ) >= '{start}' 
					AND DATE_ADD( x.djsj, INTERVAL 15 DAY ) <= '{end}' 
					AND x.check_flag = 0 
					AND x.djjglbdm IN ( '0000', '0100', '0200', '0300' ) 
					AND x.xfrs >= 1 
					AND x.xfrs <= 9999 
					AND x.sfnrtj = 1 
					AND x.xfxsdm IN ( '100', '200', '300', '303' ) 
					AND x.sfssbz = 0 
				) t ON r.region_code = concat( t.wtsddm, '000000' ) 
			WHERE
				r.region_code LIKE '44____000000%%' 
				AND r.region_code <> '440000000000' 
			GROUP BY
			r.region_code
)"""

sql_1_4_xfxs = """(SELECT
	r.region_name,
CASE
		
		WHEN instr( r.region_code, '0000000000' ) > 0 THEN
		'省级' 
		WHEN instr( r.region_code, '00000000' ) > 0 THEN
		'市级' 
		WHEN instr( r.region_code, '000000' ) > 0 THEN
		'县级' 
	END bmjb,
	r.region_code,
	t.xfxs,-- 总数
	count( DISTINCT ( t.xfjbh ) ) AS zs,-- 已受理
	count(
		DISTINCT (
		CASE
				
				WHEN ( t.sjslsj IS NOT NULL OR t.shijslsj IS NOT NULL OR t.xjslsj IS NOT NULL ) THEN
				t.xfjbh 
			END 
			) 
		) AS ysl,-- 及时受理
		count(
			DISTINCT (
			CASE
					
					WHEN least(
						ifnull( t.sjslsj, SYSDATE( ) ),
						ifnull( t.shijslsj, SYSDATE( ) ),
						ifnull( t.xjslsj, SYSDATE( ) ) 
					) <= DATE_ADD( t.djsj, INTERVAL 15 DAY ) 
					AND least(
						ifnull( t.sjslsj, SYSDATE( ) ),
						ifnull( t.shijslsj, SYSDATE( ) ),
						ifnull( t.xjslsj, SYSDATE( ) ) 
						) <> SYSDATE( ) THEN
						t.xfjbh 
					END 
					) 
				) AS jssl,-- 超期受理
				count(
					DISTINCT (
					CASE
							
							WHEN least(
								ifnull( t.sjslsj, SYSDATE( ) ),
								ifnull( t.shijslsj, SYSDATE( ) ),
								ifnull( t.xjslsj, SYSDATE( ) ) 
							) > DATE_ADD( t.djsj, INTERVAL 15 DAY ) 
							AND least(
								ifnull( t.sjslsj, SYSDATE( ) ),
								ifnull( t.shijslsj, SYSDATE( ) ),
								ifnull( t.xjslsj, SYSDATE( ) ) 
								) <> SYSDATE( ) THEN
								t.xfjbh 
							END 
							) 
						) AS cqsl,-- 超期未受理
						count(
							DISTINCT (
							CASE
									
									WHEN ( t.sjslsj IS NULL AND t.shijslsj IS NULL AND t.xjslsj IS NULL ) 
									AND SYSDATE( ) > DATE_ADD( t.djsj, INTERVAL 15 DAY ) THEN
										t.xfjbh 
									END 
									) 
								) AS cqwsl 
							FROM
								rpt_region r
								LEFT JOIN (
								SELECT DISTINCT
									x.xfjbh,
								CASE
										
										WHEN x.xfxsmc = '来信' THEN
										'来信' 
										WHEN x.xfxsmc = '来访' THEN
										'来访' ELSE '网信' 
									END xfxs,
					substr( IFNULL( x.zjqxdm, x.wtsddm ), 1, 6 ) AS wtsddm,
					x.sjslsj,
					x.shijslsj,
					x.xjslsj,
					x.ddzrdwsj,
					x.djsj 
				FROM
					rpt_xfjxx x
					LEFT JOIN xf_dbxx e ON e.xfjbh = x.xfjbh
					LEFT JOIN xf_ybinfo y ON x.xfjbh = y.xfjbh 
				WHERE
					1 = 1 
					AND DATE_ADD( x.djsj, INTERVAL 15 DAY ) >= '{start}' 
					AND DATE_ADD( x.djsj, INTERVAL 15 DAY ) <= '{end}' 
					AND ( CASE x.xfxsmc WHEN '来信' THEN '来信' WHEN '来访' THEN '来访' ELSE '网信' END ) = '{xfxs}' 
					AND x.check_flag = 0 
					AND x.djjglbdm IN ( '0000', '0100', '0200', '0300' ) 
					AND x.xfrs >= 1 
					AND x.xfrs <= 9999 
					AND x.sfnrtj = 1 
					AND x.xfxsdm IN ( '100', '200', '300', '303' ) 
					AND x.sfssbz = 0 
				) t ON r.region_code = concat( t.wtsddm, '000000' ) 
			WHERE
				r.region_code LIKE '44____000000%%' 
				AND r.region_code <> '440000000000' 
				AND substr( r.region_code, 1, 4 ) = ( SELECT substr( region_code, 1, 4 ) FROM rpt_region WHERE region_name = '{Cqh}' ) 
			GROUP BY
			r.region_code,
	t.xfxs
)"""

sql_1_5_all = """(SELECT
	r.region_name,
CASE
		
		WHEN instr( r.region_code, '0000000000' ) > 0 THEN
		'省级' 
		WHEN instr( r.region_code, '00000000' ) > 0 THEN
		'市级' 
		WHEN instr( r.region_code, '000000' ) > 0 THEN
		'县级' 
	END bmjb,
	r.region_code,
	r.company_name,
	count( DISTINCT ( t.xfjbh ) ) AS zs,-- 已受理
	count(
		DISTINCT (
		CASE
				
				WHEN ( t.sjslsj IS NOT NULL OR t.shijslsj IS NOT NULL OR t.xjslsj IS NOT NULL ) THEN
				t.xfjbh 
			END 
			) 
		) AS ysl,-- 及时受理
		count(
			DISTINCT (
			CASE
					
					WHEN least(
						ifnull( t.sjslsj, SYSDATE( ) ),
						ifnull( t.shijslsj, SYSDATE( ) ),
						ifnull( t.xjslsj, SYSDATE( ) ) 
					) <= DATE_ADD( t.djsj, INTERVAL 15 DAY ) 
					AND least(
						ifnull( t.sjslsj, SYSDATE( ) ),
						ifnull( t.shijslsj, SYSDATE( ) ),
						ifnull( t.xjslsj, SYSDATE( ) ) 
						) <> SYSDATE( ) THEN
						t.xfjbh 
					END 
					) 
				) AS jssl,-- 超期受理
				count(
					DISTINCT (
					CASE
							
							WHEN least(
								ifnull( t.sjslsj, SYSDATE( ) ),
								ifnull( t.shijslsj, SYSDATE( ) ),
								ifnull( t.xjslsj, SYSDATE( ) ) 
							) > DATE_ADD( t.djsj, INTERVAL 15 DAY ) 
							AND least(
								ifnull( t.sjslsj, SYSDATE( ) ),
								ifnull( t.shijslsj, SYSDATE( ) ),
								ifnull( t.xjslsj, SYSDATE( ) ) 
								) <> SYSDATE( ) THEN
								t.xfjbh 
							END 
							) 
						) AS cqsl,-- 超期未受理
						count(
							DISTINCT (
							CASE
									
									WHEN ( t.sjslsj IS NULL AND t.shijslsj IS NULL AND t.xjslsj IS NULL ) 
									AND SYSDATE( ) > DATE_ADD( t.djsj, INTERVAL 15 DAY ) THEN
										t.xfjbh 
									END 
									) 
								) AS cqwsl 
							FROM
								(
								SELECT
									company_name,
									org_code,
									b.region_code,
									b.region_name 
								FROM
									xf_org a,
									rpt_region b 
								WHERE
									a.region_code = b.region_code 
									AND a.is_petition = 1 
								) r
								LEFT JOIN (
								SELECT DISTINCT
									x.xfjbh,
								CASE
										
										WHEN x.xfxsmc = '来信' THEN
										'来信' 
										WHEN x.xfxsmc = '来访' THEN
										'来访' ELSE '网信' 
									END xfxs,
					substr( IFNULL( x.zjqxdm, x.wtsddm ), 1, 6 ) AS wtsddm,
					x.sjslsj,
					x.shijslsj,
					x.xjslsj,
					x.ddzrdwsj,
					x.djsj 
				FROM
					rpt_xfjxx x
					LEFT JOIN xf_dbxx e ON e.xfjbh = x.xfjbh
					LEFT JOIN xf_ybinfo y ON x.xfjbh = y.xfjbh 
				WHERE
					1 = 1 
					AND DATE_ADD( x.djsj, INTERVAL 15 DAY ) >= '{start}' 
					AND DATE_ADD( x.djsj, INTERVAL 15 DAY ) <= '{end}'
					
					AND x.check_flag = 0 
					AND x.djjglbdm IN ( '0000', '0100', '0200', '0300' ) 
					AND x.xfrs >= 1 
					AND x.xfrs <= 9999 
					AND x.sfnrtj = 1 
					AND x.xfxsdm IN ( '100', '200', '300', '303' ) 
					AND x.sfssbz = 0 
				) t ON r.region_code = concat( t.wtsddm, '00000000' ) 
			WHERE
				r.region_code LIKE '44__00000000%%' 
			GROUP BY
				r.region_code,
			r.company_name
)"""

sql_1_5_xfxs = """(SELECT
	r.region_name,
CASE
		
		WHEN instr( r.region_code, '0000000000' ) > 0 THEN
		'省级' 
		WHEN instr( r.region_code, '00000000' ) > 0 THEN
		'市级' 
		WHEN instr( r.region_code, '000000' ) > 0 THEN
		'县级' 
	END bmjb,
	r.region_code,
	r.company_name,
	t.xfxs,-- 总数
	count( DISTINCT ( t.xfjbh ) ) AS zs,-- 已受理
	count(
		DISTINCT (
		CASE
				
				WHEN ( t.sjslsj IS NOT NULL OR t.shijslsj IS NOT NULL OR t.xjslsj IS NOT NULL ) THEN
				t.xfjbh 
			END 
			) 
		) AS ysl,-- 及时受理
		count(
			DISTINCT (
			CASE
					
					WHEN least(
						ifnull( t.sjslsj, SYSDATE( ) ),
						ifnull( t.shijslsj, SYSDATE( ) ),
						ifnull( t.xjslsj, SYSDATE( ) ) 
					) <= DATE_ADD( t.djsj, INTERVAL 15 DAY ) 
					AND least(
						ifnull( t.sjslsj, SYSDATE( ) ),
						ifnull( t.shijslsj, SYSDATE( ) ),
						ifnull( t.xjslsj, SYSDATE( ) ) 
						) <> SYSDATE( ) THEN
						t.xfjbh 
					END 
					) 
				) AS jssl,-- 超期受理
				count(
					DISTINCT (
					CASE
							
							WHEN least(
								ifnull( t.sjslsj, SYSDATE( ) ),
								ifnull( t.shijslsj, SYSDATE( ) ),
								ifnull( t.xjslsj, SYSDATE( ) ) 
							) > DATE_ADD( t.djsj, INTERVAL 15 DAY ) 
							AND least(
								ifnull( t.sjslsj, SYSDATE( ) ),
								ifnull( t.shijslsj, SYSDATE( ) ),
								ifnull( t.xjslsj, SYSDATE( ) ) 
								) <> SYSDATE( ) THEN
								t.xfjbh 
							END 
							) 
						) AS cqsl,-- 超期未受理
						count(
							DISTINCT (
							CASE
									
									WHEN ( t.sjslsj IS NULL AND t.shijslsj IS NULL AND t.xjslsj IS NULL ) 
									AND SYSDATE( ) > DATE_ADD( t.djsj, INTERVAL 15 DAY ) THEN
										t.xfjbh 
									END 
									) 
								) AS cqwsl 
							FROM
								(
								SELECT
									company_name,
									org_code,
									b.region_code,
									b.region_name 
								FROM
									xf_org a,
									rpt_region b 
								WHERE
									a.region_code = b.region_code 
									AND a.is_petition = 1 
								) r
								LEFT JOIN (
								SELECT DISTINCT
									x.xfjbh,
								CASE
										
										WHEN x.xfxsmc = '来信' THEN
										'来信' 
										WHEN x.xfxsmc = '来访' THEN
										'来访' ELSE '网信' 
									END xfxs,
					substr( IFNULL( x.zjqxdm, x.wtsddm ), 1, 6 ) AS wtsddm,
					x.sjslsj,
					x.shijslsj,
					x.xjslsj,
					x.ddzrdwsj,
					x.djsj 
				FROM
					rpt_xfjxx x
					LEFT JOIN xf_dbxx e ON e.xfjbh = x.xfjbh
					LEFT JOIN xf_ybinfo y ON x.xfjbh = y.xfjbh 
				WHERE
					1 = 1 
					AND DATE_ADD( x.djsj, INTERVAL 15 DAY ) >= '{start}' 
					AND DATE_ADD( x.djsj, INTERVAL 15 DAY ) <= '{end}' 
					#and (case x.xfxsmc when '来信' then '来信' when '来访' then '来访' else '网信' end)='{xfxs}'
			
					AND x.check_flag = 0 
					AND x.djjglbdm IN ( '0000', '0100', '0200', '0300' ) 
					AND x.xfrs >= 1 
					AND x.xfrs <= 9999 
					AND x.sfnrtj = 1 
					AND x.xfxsdm IN ( '100', '200', '300', '303' ) 
					AND x.sfssbz = 0 
				) t ON r.region_code = concat( t.wtsddm, '00000000' ) 
			WHERE
				r.region_code LIKE '44__00000000%%' 
			GROUP BY
				r.region_code,
			r.company_name,
	t.xfxs;)"""

sql_1_6_all = """(SELECT
	r.region_name,
CASE
		
		WHEN instr( r.region_code, '0000000000' ) > 0 THEN
		'省级' 
		WHEN instr( r.region_code, '00000000' ) > 0 THEN
		'市级' 
		WHEN instr( r.region_code, '000000' ) > 0 THEN
		'县级' 
	END bmjb,
	r.region_code,
	r.company_name,
	count( DISTINCT ( t.xfjbh ) ) AS zs,-- 已受理
	count(
		DISTINCT (
		CASE
				
				WHEN ( t.sjslsj IS NOT NULL OR t.shijslsj IS NOT NULL OR t.xjslsj IS NOT NULL ) THEN
				t.xfjbh 
			END 
			) 
		) AS ysl,-- 及时受理
		count(
			DISTINCT (
			CASE
					
					WHEN least(
						ifnull( t.sjslsj, SYSDATE( ) ),
						ifnull( t.shijslsj, SYSDATE( ) ),
						ifnull( t.xjslsj, SYSDATE( ) ) 
					) <= DATE_ADD( t.djsj, INTERVAL 15 DAY ) 
					AND least(
						ifnull( t.sjslsj, SYSDATE( ) ),
						ifnull( t.shijslsj, SYSDATE( ) ),
						ifnull( t.xjslsj, SYSDATE( ) ) 
						) <> SYSDATE( ) THEN
						t.xfjbh 
					END 
					) 
				) AS jssl,-- 超期受理
				count(
					DISTINCT (
					CASE
							
							WHEN least(
								ifnull( t.sjslsj, SYSDATE( ) ),
								ifnull( t.shijslsj, SYSDATE( ) ),
								ifnull( t.xjslsj, SYSDATE( ) ) 
							) > DATE_ADD( t.djsj, INTERVAL 15 DAY ) 
							AND least(
								ifnull( t.sjslsj, SYSDATE( ) ),
								ifnull( t.shijslsj, SYSDATE( ) ),
								ifnull( t.xjslsj, SYSDATE( ) ) 
								) <> SYSDATE( ) THEN
								t.xfjbh 
							END 
							) 
						) AS cqsl,-- 超期未受理
						count(
							DISTINCT (
							CASE
									
									WHEN ( t.sjslsj IS NULL AND t.shijslsj IS NULL AND t.xjslsj IS NULL ) 
									AND SYSDATE( ) > DATE_ADD( t.djsj, INTERVAL 15 DAY ) THEN
										t.xfjbh 
									END 
									) 
								) AS cqwsl 
							FROM
								(
								SELECT
									company_name,
									org_code,
									b.region_code,
									b.region_name 
								FROM
									xf_org a,
									rpt_region b 
								WHERE
									a.region_code = b.region_code 
									AND a.is_petition = 1 
								) r
								LEFT JOIN (
								SELECT DISTINCT
									x.xfjbh,
								CASE
										
										WHEN x.xfxsmc = '来信' THEN
										'来信' 
										WHEN x.xfxsmc = '来访' THEN
										'来访' ELSE '网信' 
									END xfxs,
					substr( IFNULL( x.zjqxdm, x.wtsddm ), 1, 6 ) AS wtsddm,
					x.sjslsj,
					x.shijslsj,
					x.xjslsj,
					x.ddzrdwsj,
					x.djsj 
				FROM
					rpt_xfjxx x
					LEFT JOIN xf_dbxx e ON e.xfjbh = x.xfjbh
					LEFT JOIN xf_ybinfo y ON x.xfjbh = y.xfjbh 
				WHERE
					1 = 1 
					AND DATE_ADD( x.djsj, INTERVAL 15 DAY ) >= '{start}' 
					AND DATE_ADD( x.djsj, INTERVAL 15 DAY ) <= '{end}' 
					AND x.check_flag = 0 
					AND x.djjglbdm IN ( '0000', '0100', '0200', '0300' ) 
					AND x.xfrs >= 1 
					AND x.xfrs <= 9999 
					AND x.sfnrtj = 1 
					AND x.xfxsdm IN ( '100', '200', '300', '303' ) 
					AND x.sfssbz = 0 
				) t ON r.region_code = concat( t.wtsddm, '000000' ) 
			WHERE
				r.region_code LIKE '44____000000%%' 
				AND r.region_code <> '440000000000' 
				AND substr( r.region_code, 1, 4 ) = ( SELECT substr( region_code, 1, 4 ) FROM rpt_region WHERE region_name = '{Cqh}' ) 
			GROUP BY
				r.region_code,
			r.company_name
)"""

sql_1_6_xfxs = """(SELECT
	r.region_name,
CASE
		
		WHEN instr( r.region_code, '0000000000' ) > 0 THEN
		'省级' 
		WHEN instr( r.region_code, '00000000' ) > 0 THEN
		'市级' 
		WHEN instr( r.region_code, '000000' ) > 0 THEN
		'县级' 
	END bmjb,
	r.region_code,
	r.company_name,
	t.xfxs,-- 总数
	count( DISTINCT ( t.xfjbh ) ) AS zs,-- 已受理
	count(
		DISTINCT (
		CASE
				
				WHEN ( t.sjslsj IS NOT NULL OR t.shijslsj IS NOT NULL OR t.xjslsj IS NOT NULL ) THEN
				t.xfjbh 
			END 
			) 
		) AS ysl,-- 及时受理
		count(
			DISTINCT (
			CASE
					
					WHEN least(
						ifnull( t.sjslsj, SYSDATE( ) ),
						ifnull( t.shijslsj, SYSDATE( ) ),
						ifnull( t.xjslsj, SYSDATE( ) ) 
					) <= DATE_ADD( t.djsj, INTERVAL 15 DAY ) 
					AND least(
						ifnull( t.sjslsj, SYSDATE( ) ),
						ifnull( t.shijslsj, SYSDATE( ) ),
						ifnull( t.xjslsj, SYSDATE( ) ) 
						) <> SYSDATE( ) THEN
						t.xfjbh 
					END 
					) 
				) AS jssl,-- 超期受理
				count(
					DISTINCT (
					CASE
							
							WHEN least(
								ifnull( t.sjslsj, SYSDATE( ) ),
								ifnull( t.shijslsj, SYSDATE( ) ),
								ifnull( t.xjslsj, SYSDATE( ) ) 
							) > DATE_ADD( t.djsj, INTERVAL 15 DAY ) 
							AND least(
								ifnull( t.sjslsj, SYSDATE( ) ),
								ifnull( t.shijslsj, SYSDATE( ) ),
								ifnull( t.xjslsj, SYSDATE( ) ) 
								) <> SYSDATE( ) THEN
								t.xfjbh 
							END 
							) 
						) AS cqsl,-- 超期未受理
						count(
							DISTINCT (
							CASE
									
									WHEN ( t.sjslsj IS NULL AND t.shijslsj IS NULL AND t.xjslsj IS NULL ) 
									AND SYSDATE( ) > DATE_ADD( t.djsj, INTERVAL 15 DAY ) THEN
										t.xfjbh 
									END 
									) 
								) AS cqwsl 
							FROM
								(
								SELECT
									company_name,
									org_code,
									b.region_code,
									b.region_name 
								FROM
									xf_org a,
									rpt_region b 
								WHERE
									a.region_code = b.region_code 
									AND a.is_petition = 1 
								) r
								LEFT JOIN (
								SELECT DISTINCT
									x.xfjbh,
								CASE
										
										WHEN x.xfxsmc = '来信' THEN
										'来信' 
										WHEN x.xfxsmc = '来访' THEN
										'来访' ELSE '网信' 
									END xfxs,
					substr( IFNULL( x.zjqxdm, x.wtsddm ), 1, 6 ) AS wtsddm,
					x.sjslsj,
					x.shijslsj,
					x.xjslsj,
					x.ddzrdwsj,
					x.djsj 
				FROM
					rpt_xfjxx x
					LEFT JOIN xf_dbxx e ON e.xfjbh = x.xfjbh
					LEFT JOIN xf_ybinfo y ON x.xfjbh = y.xfjbh 
				WHERE
					1 = 1 
					AND DATE_ADD( x.djsj, INTERVAL 15 DAY ) >= '{start}' 
					AND DATE_ADD( x.djsj, INTERVAL 15 DAY ) <= '{end}' 
					AND ( CASE x.xfxsmc WHEN '来信' THEN '来信' WHEN '来访' THEN '来访' ELSE '网信' END ) = '{xfxs}' 
					AND x.check_flag = 0 
					AND x.djjglbdm IN ( '0000', '0100', '0200', '0300' ) 
					AND x.xfrs >= 1 
					AND x.xfrs <= 9999 
					AND x.sfnrtj = 1 
					AND x.xfxsdm IN ( '100', '200', '300', '303' ) 
					AND x.sfssbz = 0 
				) t ON r.region_code = concat( t.wtsddm, '000000' ) 
			WHERE
				r.region_code LIKE '44____000000%%' 
				AND r.region_code <> '440000000000' 
				AND substr( r.region_code, 1, 4 ) = ( SELECT substr( region_code, 1, 4 ) FROM rpt_region WHERE region_name = '{Cqh}' ) 
			GROUP BY
				r.region_code,
			r.company_name,
	t.xfxs;)"""

sql_2_2_all = """(SELECT
	r.region_name,
CASE
		
		WHEN instr( r.region_code, '0000000000' ) > 0 THEN
		'省级' 
		WHEN instr( r.region_code, '00000000' ) > 0 THEN
		'市级' 
		WHEN instr( r.region_code, '000000' ) > 0 THEN
		'县级' 
	END bmjb,
	r.region_code,
	count( DISTINCT ( t.xfjbh ) ) AS zs,#已受理
	count( DISTINCT ( CASE WHEN t.zrdwslsj IS NOT NULL THEN t.xfjbh END ) ) AS ysl,#及时受理
	count(
		DISTINCT (
		CASE
				
				WHEN ( t.zrdwslsj IS NOT NULL AND t.zrdwslsj <= DATE_ADD( t.djsj, INTERVAL 30 DAY ) ) THEN
				t.xfjbh 
			END 
			) 
		) AS jssl,#超期受理
		count(
			DISTINCT (
			CASE
					
					WHEN ( t.zrdwslsj IS NOT NULL AND t.zrdwslsj > DATE_ADD( t.djsj, INTERVAL 30 DAY ) ) THEN
					t.xfjbh 
				END 
				) 
			) AS cqsl,#超期未受理
			count(
				DISTINCT (
				CASE
						
						WHEN t.zrdwslsj IS NULL 
						AND SYSDATE( ) > DATE_ADD( t.djsj, INTERVAL 30 DAY ) THEN
							t.xfjbh 
						END 
						) 
					) AS cqwsl 
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
		x.zrdwslsj,
		x.djsj 
	FROM
		rpt_xfjxx x
		LEFT JOIN xf_dbxx e ON e.xfjbh = x.xfjbh
		LEFT JOIN xf_ybinfo y ON x.xfjbh = y.xfjbh 
	WHERE
		1 = 1 
		AND x.check_flag = 0 
		AND DATE_ADD( x.djsj, INTERVAL 30 DAY ) >= '{start}' 
		AND DATE_ADD( x.djsj, INTERVAL 30 DAY ) <= '{end}'  
		AND x.djjglbdm IN ( '0000', '0100', '0200', '0300', '1000', '1100', '1200', '1300', '1400' ) 
		AND x.xfrs >= 1 
		AND x.xfrs <= 9999 
		AND x.qxsfzrdw = 1 
		AND x.sfnrtj = 1 
		AND x.xfxsdm IN ( '100', '200', '300', '303' ) 
		AND x.sfssbz = 0 
	) t ON r.region_code = concat( t.wtsddm, '00000000' ) 
WHERE
	r.region_code LIKE '44__00000000%%' 
GROUP BY
	r.region_code
)"""

sql_2_2_xfxs = """(SELECT
	r.region_name,
CASE
		
		WHEN instr( r.region_code, '0000000000' ) > 0 THEN
		'省级' 
		WHEN instr( r.region_code, '00000000' ) > 0 THEN
		'市级' 
		WHEN instr( r.region_code, '000000' ) > 0 THEN
		'县级' 
	END bmjb,
	r.region_code,
	xfxs,#总数
	count( DISTINCT ( t.xfjbh ) ) AS zs,#已受理
	count( DISTINCT ( CASE WHEN t.zrdwslsj IS NOT NULL THEN t.xfjbh END ) ) AS ysl,#及时受理
	count(
		DISTINCT (
		CASE
				
				WHEN ( t.zrdwslsj IS NOT NULL AND t.zrdwslsj <= DATE_ADD( t.djsj, INTERVAL 30 DAY ) ) THEN
				t.xfjbh 
			END 
			) 
		) AS jssl,#超期受理
		count(
			DISTINCT (
			CASE
					
					WHEN ( t.zrdwslsj IS NOT NULL AND t.zrdwslsj > DATE_ADD( t.djsj, INTERVAL 30 DAY ) ) THEN
					t.xfjbh 
				END 
				) 
			) AS cqsl,#超期未受理
			count(
				DISTINCT (
				CASE
						
						WHEN t.zrdwslsj IS NULL 
						AND SYSDATE( ) > DATE_ADD( t.djsj, INTERVAL 30 DAY ) THEN
							t.xfjbh 
						END 
						) 
					) AS cqwsl 
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
		x.zrdwslsj,
		x.djsj 
	FROM
		rpt_xfjxx x
		LEFT JOIN xf_dbxx e ON e.xfjbh = x.xfjbh
		LEFT JOIN xf_ybinfo y ON x.xfjbh = y.xfjbh 
	WHERE
		1 = 1 
		AND x.check_flag = 0 
		AND DATE_ADD( x.djsj, INTERVAL 30 DAY ) >= '{start}' 
		AND DATE_ADD( x.djsj, INTERVAL 30 DAY ) <= '{end}' 
		AND ( CASE x.xfxsmc WHEN '来信' THEN '来信' WHEN '来访' THEN '来访' ELSE '网信' END ) = '{xfxs}' 
		AND x.djjglbdm IN ( '0000', '0100', '0200', '0300', '1000', '1100', '1200', '1300', '1400' ) 
		AND x.xfrs >= 1 
		AND x.xfrs <= 9999 
		AND x.qxsfzrdw = 1 
		AND x.sfnrtj = 1 
		AND x.xfxsdm IN ( '100', '200', '300', '303' ) 
		AND x.sfssbz = 0 
	) t ON r.region_code = concat( t.wtsddm, '00000000' ) 
WHERE
	r.region_code LIKE '44__00000000%%' 
GROUP BY
	r.region_code,
	xfxs)"""

sql_2_4_all = """(SELECT
	r.region_name,
CASE
		
		WHEN instr( r.region_code, '0000000000' ) > 0 THEN
		'省级' 
		WHEN instr( r.region_code, '00000000' ) > 0 THEN
		'市级' 
		WHEN instr( r.region_code, '000000' ) > 0 THEN
		'县级' 
	END bmjb,
	r.region_code,
	count( DISTINCT ( t.xfjbh ) ) AS zs,#已受理
	count( DISTINCT ( CASE WHEN t.zrdwslsj IS NOT NULL THEN t.xfjbh END ) ) AS ysl,#及时受理
	count(
		DISTINCT (
		CASE
				
				WHEN ( t.zrdwslsj IS NOT NULL AND t.zrdwslsj <= DATE_ADD( t.djsj, INTERVAL 30 DAY ) ) THEN
				t.xfjbh 
			END 
			) 
		) AS jssl,#超期受理
		count(
			DISTINCT (
			CASE
					
					WHEN ( t.zrdwslsj IS NOT NULL AND t.zrdwslsj > DATE_ADD( t.djsj, INTERVAL 30 DAY ) ) THEN
					t.xfjbh 
				END 
				) 
			) AS cqsl,#超期未受理
			count(
				DISTINCT (
				CASE
						
						WHEN t.zrdwslsj IS NULL 
						AND SYSDATE( ) > DATE_ADD( t.djsj, INTERVAL 30 DAY ) THEN
							t.xfjbh 
						END 
						) 
					) AS cqwsl 
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
		x.zrdwslsj,
		x.djsj 
	FROM
		rpt_xfjxx x
		LEFT JOIN xf_dbxx e ON e.xfjbh = x.xfjbh
		LEFT JOIN xf_ybinfo y ON x.xfjbh = y.xfjbh 
	WHERE
		1 = 1 
		AND x.check_flag = 0 
		AND DATE_ADD( x.djsj, INTERVAL 30 DAY ) >= '{start}' 
		AND DATE_ADD( x.djsj, INTERVAL 30 DAY ) <= '{end}' 
		AND x.djjglbdm IN ( '0000', '0100', '0200', '0300', '1000', '1100', '1200', '1300', '1400' ) 
		AND x.xfrs >= 1 
		AND x.xfrs <= 9999 
		AND x.qxsfzrdw = 1 
		AND x.sfnrtj = 1 
		AND x.xfxsdm IN ( '100', '200', '300', '303' ) 
		AND x.sfssbz = 0 
	) t ON r.region_code = concat( t.wtsddm, '000000' ) 
WHERE
	r.region_code LIKE '44____000000%%' 
	AND r.region_code <> '440000000000' 
	AND substr( r.region_code, 1, 4 ) = ( SELECT substr( region_code, 1, 4 ) FROM rpt_region WHERE region_name = '{Cqh}' ) 
GROUP BY
	r.region_code
)"""

sql_2_4_xfxs = """(SELECT
	r.region_name,
CASE
		
		WHEN instr( r.region_code, '0000000000' ) > 0 THEN
		'省级' 
		WHEN instr( r.region_code, '00000000' ) > 0 THEN
		'市级' 
		WHEN instr( r.region_code, '000000' ) > 0 THEN
		'县级' 
	END bmjb,
	r.region_code,
	xfxs,#总数
	count( DISTINCT ( t.xfjbh ) ) AS zs,#已受理
	count( DISTINCT ( CASE WHEN t.zrdwslsj IS NOT NULL THEN t.xfjbh END ) ) AS ysl,#及时受理
	count(
		DISTINCT (
		CASE
				
				WHEN ( t.zrdwslsj IS NOT NULL AND t.zrdwslsj <= DATE_ADD( t.djsj, INTERVAL 30 DAY ) ) THEN
				t.xfjbh 
			END 
			) 
		) AS jssl,#超期受理
		count(
			DISTINCT (
			CASE
					
					WHEN ( t.zrdwslsj IS NOT NULL AND t.zrdwslsj > DATE_ADD( t.djsj, INTERVAL 30 DAY ) ) THEN
					t.xfjbh 
				END 
				) 
			) AS cqsl,#超期未受理
			count(
				DISTINCT (
				CASE
						
						WHEN t.zrdwslsj IS NULL 
						AND SYSDATE( ) > DATE_ADD( t.djsj, INTERVAL 30 DAY ) THEN
							t.xfjbh 
						END 
						) 
					) AS cqwsl 
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
		x.zrdwslsj,
		x.djsj 
	FROM
		rpt_xfjxx x
		LEFT JOIN xf_dbxx e ON e.xfjbh = x.xfjbh
		LEFT JOIN xf_ybinfo y ON x.xfjbh = y.xfjbh 
	WHERE
		1 = 1 
		AND x.check_flag = 0 
		AND DATE_ADD( x.djsj, INTERVAL 30 DAY ) >= '{start}' 
		AND DATE_ADD( x.djsj, INTERVAL 30 DAY ) <= '{end}' 
		AND ( CASE x.xfxsmc WHEN '来信' THEN '来信' WHEN '来访' THEN '来访' ELSE '网信' END ) = '{xfxs}' 
		AND x.djjglbdm IN ( '0000', '0100', '0200', '0300', '1000', '1100', '1200', '1300', '1400' ) 
		AND x.xfrs >= 1 
		AND x.xfrs <= 9999 
		AND x.qxsfzrdw = 1 
		AND x.sfnrtj = 1 
		AND x.xfxsdm IN ( '100', '200', '300', '303' ) 
		AND x.sfssbz = 0 
	) t ON r.region_code = concat( t.wtsddm, '000000' ) 
WHERE
	r.region_code LIKE '44____000000%%' 
	AND r.region_code <> '440000000000' 
	AND substr( r.region_code, 1, 4 ) = ( SELECT substr( region_code, 1, 4 ) FROM rpt_region WHERE region_name = '{Cqh}' ) 
GROUP BY
	r.region_code,
	xfxs)"""

sql_2_5_all = """(SELECT
	r.region_name,
	r.company_name,
	r.org_code,
	count( DISTINCT ( t.xfjbh ) ) AS zs,#已受理
	count( DISTINCT ( CASE WHEN t.zrdwslsj IS NOT NULL THEN t.xfjbh END ) ) AS ysl,#及时受理
	count(
		DISTINCT (
		CASE
				
				WHEN ( t.zrdwslsj IS NOT NULL AND t.zrdwslsj <= DATE_ADD( t.djsj, INTERVAL 30 DAY ) ) THEN
				t.xfjbh 
			END 
			) 
		) AS jssl,#超期受理
		count(
			DISTINCT (
			CASE
					
					WHEN ( t.zrdwslsj IS NOT NULL AND t.zrdwslsj > DATE_ADD( t.djsj, INTERVAL 30 DAY ) ) THEN
					t.xfjbh 
				END 
				) 
			) AS cqsl,#超期未受理
			count(
				DISTINCT (
				CASE
						
						WHEN t.zrdwslsj IS NULL 
						AND SYSDATE( ) > DATE_ADD( t.djsj, INTERVAL 30 DAY ) THEN
							t.xfjbh 
						END 
						) 
					) AS cqwsl 
				FROM
					(
					SELECT
						company_name,
						org_code,
						b.region_code,
						b.region_name 
					FROM
						xf_org a,
						xf_region b 
					WHERE
						a.region_code = b.region_code 
						AND a.is_petition = 0 
					) r
					LEFT JOIN (
					SELECT DISTINCT
						( x.xfjbh ) AS xfjbh,
					CASE
							
							WHEN x.xfxsmc = '来信' THEN
							'来信' 
							WHEN x.xfxsmc = '来访' THEN
							'来访' ELSE '网信' 
						END xfxs,
		x.wtsddm,
		x.zrdwslsj,
		x.djsj,
		x.zjqxdm,
		x.djjgdm,
		b.qxmcdm 
	FROM
		rpt_xfjxx x
		LEFT JOIN rpt_blfsxx b ON x.xfjbh = b.xfjbh 
	WHERE
		1 = 1 
		AND DATE_ADD( x.djsj, INTERVAL 30 DAY ) >= '{start}' 
		AND DATE_ADD( x.djsj, INTERVAL 30 DAY ) <= '{end}' 
		AND x.check_flag = 0 
		AND x.djjglbdm IN ( '0000', '0100', '0200', '0300', '1100', '1200', '1300', '1400' ) 
		AND x.xfrs >= 1 
		AND x.xfrs <= 9999 
		AND x.qxsfzrdw = 1 
		AND x.sfnrtj = 1 
		AND x.xfxsdm IN ( '100', '200', '300', '303' ) 
		AND x.sfssbz = 0 
	) t ON ( t.qxmcdm = r.org_code OR t.djjgdm = r.org_code ) 
WHERE
	r.region_name = '{Cqh}' 
GROUP BY
	r.region_name,
	r.org_code
)"""

sql_2_5_xfxs = """(SELECT
	r.region_name,
	r.company_name,
	r.org_code,
	xfxs,#总数
	count( DISTINCT ( t.xfjbh ) ) AS zs,#已受理
	count( DISTINCT ( CASE WHEN t.zrdwslsj IS NOT NULL THEN t.xfjbh END ) ) AS ysl,#及时受理
	count(
		DISTINCT (
		CASE
				
				WHEN ( t.zrdwslsj IS NOT NULL AND t.zrdwslsj <= DATE_ADD( t.djsj, INTERVAL 30 DAY ) ) THEN
				t.xfjbh 
			END 
			) 
		) AS jssl,#超期受理
		count(
			DISTINCT (
			CASE
					
					WHEN ( t.zrdwslsj IS NOT NULL AND t.zrdwslsj > DATE_ADD( t.djsj, INTERVAL 30 DAY ) ) THEN
					t.xfjbh 
				END 
				) 
			) AS cqsl,#超期未受理
			count(
				DISTINCT (
				CASE
						
						WHEN t.zrdwslsj IS NULL 
						AND SYSDATE( ) > DATE_ADD( t.djsj, INTERVAL 30 DAY ) THEN
							t.xfjbh 
						END 
						) 
					) AS cqwsl 
				FROM
					(
					SELECT
						company_name,
						org_code,
						b.region_code,
						b.region_name 
					FROM
						xf_org a,
						xf_region b 
					WHERE
						a.region_code = b.region_code 
						AND a.is_petition = 0 
					) r
					LEFT JOIN (
					SELECT DISTINCT
						( x.xfjbh ) AS xfjbh,
					CASE
							
							WHEN x.xfxsmc = '来信' THEN
							'来信' 
							WHEN x.xfxsmc = '来访' THEN
							'来访' ELSE '网信' 
						END xfxs,
		x.wtsddm,
		x.zrdwslsj,
		x.djsj,
		x.zjqxdm,
		x.djjgdm,
		b.qxmcdm 
	FROM
		rpt_xfjxx x
		LEFT JOIN rpt_blfsxx b ON x.xfjbh = b.xfjbh 
	WHERE
		1 = 1 
		AND DATE_ADD( x.djsj, INTERVAL 30 DAY ) >= '{start}' 
		AND DATE_ADD( x.djsj, INTERVAL 30 DAY ) <= '{end}' 
		AND ( CASE x.xfxsmc WHEN '来信' THEN '来信' WHEN '来访' THEN '来访' ELSE '网信' END ) = '{xfxs}' 
		AND x.check_flag = 0 
		AND x.djjglbdm IN ( '0000', '0100', '0200', '0300', '1100', '1200', '1300', '1400' ) 
		AND x.xfrs >= 1 
		AND x.xfrs <= 9999 
		AND x.qxsfzrdw = 1 
		AND x.sfnrtj = 1 
		AND x.xfxsdm IN ( '100', '200', '300', '303' ) 
		AND x.sfssbz = 0 
	) t ON ( t.qxmcdm = r.org_code OR t.djjgdm = r.org_code ) 
WHERE
	r.region_name = '{Cqh}' 
GROUP BY
	r.region_name,
	r.org_code,
	xfxs
)"""
sql_2_6_all = """(SELECT
	r.company_name,
	count( DISTINCT ( t.xfjbh ) ) AS zs,
	count(
		DISTINCT (
		CASE
				
				WHEN ( t.zrdwslsj IS NOT NULL AND t.zrdwslsj <= DATE_ADD( t.djsj, INTERVAL 30 DAY ) ) THEN
				t.xfjbh 
			END 
			) 
		) AS jssl 
	FROM
		xf_org r
		INNER JOIN (
		SELECT DISTINCT
			( x.xfjbh ) AS xfjbh,
			x.wtsddm,
			x.zrdwslsj,
			x.djsj,
			x.zjqxdm,
			x.djjgdm,
			b.qxmcdm 
		FROM
			rpt_xfjxx x
			LEFT JOIN rpt_blfsxx b ON x.xfjbh = b.xfjbh 
		WHERE
			(
				b.qxmcdm IN (
					'4400000000000840299',
					'4400000000001110299',
					'4400000000000580299',
					'4400000000001050211',
					'4400000000000870299',
					'4400000000000900299',
					'4400000000001080299',
					'4400000000001640299',
					'4400000000000920299',
					'4400000000001020299',
					'4400000000000940299',
					'4400000000000970299',
					'4400000000001300207',
					'4400000000001070299',
					'4400000000000850299',
					'4400000000001140299',
					'4400000000001350299',
					'4400000000001310299',
					'4400000000001810299' 
				) 
				OR x.djjgdm IN (
					'4400000000000840299',
					'4400000000001110299',
					'4400000000000580299',
					'4400000000001050211',
					'4400000000000870299',
					'4400000000000900299',
					'4400000000001080299',
					'4400000000001640299',
					'4400000000000920299',
					'4400000000001020299',
					'4400000000000940299',
					'4400000000000970299',
					'4400000000001300207',
					'4400000000001070299',
					'4400000000000850299',
					'4400000000001140299',
					'4400000000001350299',
					'4400000000001310299',
					'4400000000001810299' 
				) 
			) 
			AND DATE_ADD( x.djsj, INTERVAL 30 DAY ) >= '2020-01-01 00:00:00' 
			AND DATE_ADD( x.djsj, INTERVAL 30 DAY ) <= '2020-10-31 23:59:59' 
			AND x.check_flag = 0 #参数3 登记机构类别
			
			AND x.djjglbdm IN ( '0000', '0100', '0200', '0300' ) #参数4 信访形式
			
			AND x.xfxsdm IN ( '100', '200', '300', '303' ) #参数5,6 信访人数
			
			AND x.xfrs >= 1 
			AND x.xfrs <= 9999 -- 去向为责任单位
			
			AND x.qxsfzrdw = 1 -- 查询国家局转交督省内+省内全部
			
			AND x.sfnrtj = 1 
			AND x.xfxsdm IN ( '100', '200', '300', '303' ) 
			AND x.sfssbz = 0 
		) t ON ( t.qxmcdm = r.org_code OR t.djjgdm = r.org_code ) 
	WHERE
		r.region_code = '440000000000' 
		AND r.is_choose = '1' 
		AND r.is_petition = 0 
GROUP BY
	r.org_code
)"""
sql_2_6_xfxs = """(SELECT
	r.company_name,
	t.xfxs xfxs,
	count( DISTINCT ( t.xfjbh ) ) AS zs,
	count(
		DISTINCT (
		CASE
				
				WHEN ( t.zrdwslsj IS NOT NULL AND t.zrdwslsj <= DATE_ADD( t.djsj, INTERVAL 30 DAY ) ) THEN
				t.xfjbh 
			END 
			) 
		) AS jssl 
	FROM
		xf_org r
		INNER JOIN (
		SELECT DISTINCT
			( x.xfjbh ) AS xfjbh,
			x.wtsddm,
			x.xfxsmc xfxs,
			x.zrdwslsj,
			x.djsj,
			x.zjqxdm,
			x.djjgdm,
			b.qxmcdm 
		FROM
			rpt_xfjxx x
			LEFT JOIN rpt_blfsxx b ON x.xfjbh = b.xfjbh 
		WHERE
			(
				b.qxmcdm IN (
					'4400000000000840299',
					'4400000000001110299',
					'4400000000000580299',
					'4400000000001050211',
					'4400000000000870299',
					'4400000000000900299',
					'4400000000001080299',
					'4400000000001640299',
					'4400000000000920299',
					'4400000000001020299',
					'4400000000000940299',
					'4400000000000970299',
					'4400000000001300207',
					'4400000000001070299',
					'4400000000000850299',
					'4400000000001140299',
					'4400000000001350299',
					'4400000000001310299',
					'4400000000001810299' 
				) 
				OR x.djjgdm IN (
					'4400000000000840299',
					'4400000000001110299',
					'4400000000000580299',
					'4400000000001050211',
					'4400000000000870299',
					'4400000000000900299',
					'4400000000001080299',
					'4400000000001640299',
					'4400000000000920299',
					'4400000000001020299',
					'4400000000000940299',
					'4400000000000970299',
					'4400000000001300207',
					'4400000000001070299',
					'4400000000000850299',
					'4400000000001140299',
					'4400000000001350299',
					'4400000000001310299',
					'4400000000001810299' 
				) 
			) 
			AND DATE_ADD( x.djsj, INTERVAL 30 DAY ) >= '2020-01-01 00:00:00' 
			AND DATE_ADD( x.djsj, INTERVAL 30 DAY ) <= '2020-10-31 23:59:59' 
			AND x.check_flag = 0 #参数3 登记机构类别
			
			AND x.djjglbdm IN ( '0000', '0100', '0200', '0300' ) #参数4 信访形式
			
			AND x.xfxsdm IN ( '100', '200', '300', '303' ) #参数5,6 信访人数
			
			AND x.xfrs >= 1 
			AND x.xfrs <= 9999 -- 去向为责任单位
			
			AND x.qxsfzrdw = 1 -- 查询国家局转交督省内+省内全部
			
			AND x.sfnrtj = 1 
			AND x.xfxsdm IN ( '100', '200', '300', '303' ) 
			AND x.sfssbz = 0 
		) t ON ( t.qxmcdm = r.org_code OR t.djjgdm = r.org_code ) 
	WHERE
		r.region_code = '440000000000' 
		AND r.is_choose = '1' 
		AND r.is_petition = 0 
GROUP BY
	r.org_code,
	t.xfxs
)"""