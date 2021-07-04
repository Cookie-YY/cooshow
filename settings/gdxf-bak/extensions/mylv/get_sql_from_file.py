# 信访部门 省级带市
sql_1_1_all = """
(select 
       r.region_name,
       case when instr(r.region_code,'0000000000')>0 then '省级'
            when instr(r.region_code,'00000000')>0 then '市级'
            when instr(r.region_code,'000000')>0 then '县级'
       end bmjb,
       r.region_code,
       #总数
       count(distinct(t.xfjbh)) as zs,
       #已评价
       count(distinct(case
              when t.xfbmpjzt = 2 then t.xfjbh
          end)) as ypj,
       #已评价满意
       count(distinct(case
              when (t.xfbmpjzt = 2 and t.xfbmmyz = 0) 
              then t.xfjbh
          end)) as my,
       #已评价基本满意
       count(distinct(case
              when (t.xfbmpjzt = 2 and t.xfbmmyz = 1) 
              then t.xfjbh
          end)) as jbmy,
       #已评价不满意
       count(distinct(case
              when (t.xfbmpjzt = 2 and t.xfbmmyz = 3) 
              then t.xfjbh
          end)) as bmy,
       #超期未评价
       count(distinct(case
              when t.xfbmpjzt = 3
              then t.xfjbh
          end)) as cqwpj,
       #待评价
       count(distinct(case
              when t.xfbmpjzt = 0 or t.xfbmpjzt is null
              then t.xfjbh
          end)) as dpj,
       #未评价
       count(distinct(case
              when t.xfbmpjzt = 1
              then t.xfjbh
          end)) as wpj
  from rpt_region r
  left join
  (select 
      distinct(x.xfjbh) as xfjbh,
      substr(IFNULL(x.zjqxdm,x.wtsddm), 1, 4) as wtsddm,
      x.xfbmpjzt,
      x.xfbmpjsj,
      x.xfbmmyz,
      x.pjjzsj
    from rpt_xfjxx x
    inner join rpt_blfsxx b on x.xfjbh = b.xfjbh and b.blfsdm in ('010000','020000','030000')
    where 1=1
      AND x.xfbmpjsj>= '{start}'
      AND x.xfbmpjsj <= '{end}'  
      and x.djjglbdm in  ( '0000', '0100', '0200', '0300', '1000', '1100', '1200', '1300', '1400' )
      and x.xfrs >= 1 and x.xfrs <= 9999
      and x.sfnrtj = 1
      and x.xfxsdm in ('100','200','300','303')
      and x.sfssbz=0
  ) t
  on r.region_code = concat(t.wtsddm,'00000000')
 where
  r.region_code like '44__00000000%%'
  group by r.region_code)
"""
sql_1_1_xfxs = """
(select 
       r.region_name,
       case when instr(r.region_code,'0000000000')>0 then '省级'
            when instr(r.region_code,'00000000')>0 then '市级'
            when instr(r.region_code,'000000')>0 then '县级'
       end bmjb,
       r.region_code,
       t.xfxs,
       #总数
       count(distinct(t.xfjbh)) as zs,
       #已评价
       count(distinct(case
              when t.xfbmpjzt = 2 then t.xfjbh
          end)) as ypj,
       #已评价满意
       count(distinct(case
              when (t.xfbmpjzt = 2 and t.xfbmmyz = 0) 
              then t.xfjbh
          end)) as my,
       #已评价基本满意
       count(distinct(case
              when (t.xfbmpjzt = 2 and t.xfbmmyz = 1) 
              then t.xfjbh
          end)) as jbmy,
       #已评价不满意
       count(distinct(case
              when (t.xfbmpjzt = 2 and t.xfbmmyz = 3) 
              then t.xfjbh
          end)) as bmy,
       #超期未评价
       count(distinct(case
              when t.xfbmpjzt = 3
              then t.xfjbh
          end)) as cqwpj,
       #待评价
       count(distinct(case
              when t.xfbmpjzt = 0 or t.xfbmpjzt is null
              then t.xfjbh
          end)) as dpj,
       #未评价
       count(distinct(case
              when t.xfbmpjzt = 1
              then t.xfjbh
          end)) as wpj
  from rpt_region r
  left join
  (select 
      distinct(x.xfjbh) as xfjbh,
      substr(IFNULL(x.zjqxdm,x.wtsddm), 1, 4) as wtsddm,
			CASE										
				WHEN x.xfxsmc = '来信' THEN
				'来信' 
				WHEN x.xfxsmc = '来访' THEN
				'来访' ELSE '网信' 
			END xfxs,
      x.xfbmpjzt,
      x.xfbmpjsj,
      x.xfbmmyz,
      x.pjjzsj
    from rpt_xfjxx x
    inner join rpt_blfsxx b on x.xfjbh = b.xfjbh and b.blfsdm in ('010000','020000','030000')
    where 1=1
      AND x.xfbmpjsj>= '{start}'
      AND x.xfbmpjsj <= '{end}'  
      AND ( CASE x.xfxsmc WHEN '来信' THEN '来信' WHEN '来访' THEN '来访' ELSE '网信' END ) = '{xfxs}' 
      and x.djjglbdm in  ( '0000', '0100', '0200', '0300', '1000', '1100', '1200', '1300', '1400' )
      and x.xfrs >= 1 and x.xfrs <= 9999
      and x.sfnrtj = 1
      and x.xfxsdm in ('100','200','300','303')
      and x.sfssbz=0
  ) t
  on r.region_code = concat(t.wtsddm,'00000000')
 where
  r.region_code like '44__00000000%%'
  group by r.region_code,t.xfxs
)
"""
# 责任单位 省级带市
sql_1_2_all = """
(select 
       r.region_name,
			 case when instr(r.region_code,'0000000000')>0 then '省级'
            when instr(r.region_code,'00000000')>0 then '市级'
            when instr(r.region_code,'000000')>0 then '县级'
       end bmjb,
       r.region_code,
       #总数
       count(distinct(t.xfjbh)) as zs,
       #应评价
       count(distinct(case
              when t.zrdwpjzt = 2 or t.zrdwpjzt = 3 then t.xfjbh
          end)) as yingpj,
       #已评价
       count(distinct(case
              when t.zrdwpjzt = 2 then t.xfjbh
          end)) as ypj,
       #已评价满意
       count(distinct(case
              when (t.zrdwpjzt = 2 and t.zrdwmyz = 0) 
              then t.xfjbh
          end)) as my,
       #已评价基本满意
       count(distinct(case
              when (t.zrdwpjzt = 2 and t.zrdwmyz = 1) 
              then t.xfjbh
          end)) as jbmy,
       #已评价不满意
       count(distinct(case
              when (t.zrdwpjzt = 2 and t.zrdwmyz = 3) 
              then t.xfjbh
          end)) as bmy,
       #超期未评价
       count(distinct(case
              when t.zrdwpjzt = 3
              then t.xfjbh
          end)) as cqwpj,
       #待评价
       count(distinct(case
              when t.zrdwpjzt = 0 or t.zrdwpjzt is null
              then t.xfjbh
          end)) as dpj,
       #未评价
       count(distinct(case
              when t.zrdwpjzt = 1
              then t.xfjbh
          end)) as wpj
  from rpt_region r
  left join
  (select 
      distinct(x.xfjbh) as xfjbh,
      substr(IFNULL(x.zjqxdm,x.wtsddm), 1, 4) as wtsddm,
      x.zrdwpjzt,
      x.zrdwpjsj,
      x.zrdwmyz,
      x.pjjzsj
    from rpt_xfjxx x
    inner join rpt_blfsxx b on x.xfjbh = b.xfjbh and b.blfsdm in ('010000','020000','030000')
    where 1=1
      and x.zrdwpjsj >= '{start}'
      and x.zrdwpjsj < '{end}'  
      and x.djjglbdm in ( '0000', '0100', '0200', '0300', '1000', '1100', '1200', '1300', '1400' )
      and x.xfrs >= 1 and x.xfrs <= 9999
      and x.sfnrtj = 1
      and x.xfxsdm in ('100','200','300','303')
      and x.sfssbz=0
  ) t
  on r.region_code = concat(t.wtsddm,'00000000')
 where
   r.region_code like '44__00000000%%'
 group by r.region_code)
"""
sql_1_2_xfxs = """
(select 
       r.region_name,
			 case when instr(r.region_code,'0000000000')>0 then '省级'
            when instr(r.region_code,'00000000')>0 then '市级'
            when instr(r.region_code,'000000')>0 then '县级'
       end bmjb,
       r.region_code,
       t.xfxs,
       #总数
       count(distinct(t.xfjbh)) as zs,
       #应评价
       count(distinct(case
              when t.zrdwpjzt = 2 or t.zrdwpjzt = 3 then t.xfjbh
          end)) as yingpj,
       #已评价
       count(distinct(case
              when t.zrdwpjzt = 2 then t.xfjbh
          end)) as ypj,
       #已评价满意
       count(distinct(case
              when (t.zrdwpjzt = 2 and t.zrdwmyz = 0) 
              then t.xfjbh
          end)) as my,
       #已评价基本满意
       count(distinct(case
              when (t.zrdwpjzt = 2 and t.zrdwmyz = 1) 
              then t.xfjbh
          end)) as jbmy,
       #已评价不满意
       count(distinct(case
              when (t.zrdwpjzt = 2 and t.zrdwmyz = 3) 
              then t.xfjbh
          end)) as bmy,
       #超期未评价
       count(distinct(case
              when t.zrdwpjzt = 3
              then t.xfjbh
          end)) as cqwpj,
       #待评价
       count(distinct(case
              when t.zrdwpjzt = 0 or t.zrdwpjzt is null
              then t.xfjbh
          end)) as dpj,
       #未评价
       count(distinct(case
              when t.zrdwpjzt = 1
              then t.xfjbh
          end)) as wpj
  from rpt_region r
  left join
  (select 
      distinct(x.xfjbh) as xfjbh,
			CASE										
				WHEN x.xfxsmc = '来信' THEN
				'来信' 
				WHEN x.xfxsmc = '来访' THEN
				'来访' ELSE '网信' 
			END xfxs,
      substr(IFNULL(x.zjqxdm,x.wtsddm), 1, 4) as wtsddm,
      x.zrdwpjzt,
      x.zrdwpjsj,
      x.zrdwmyz,
      x.pjjzsj
    from rpt_xfjxx x
    inner join rpt_blfsxx b on x.xfjbh = b.xfjbh and b.blfsdm in ('010000','020000','030000')
    where 1=1
      and x.zrdwpjsj >= '{start}'
      and x.zrdwpjsj < '{end}'  
      AND ( CASE x.xfxsmc WHEN '来信' THEN '来信' WHEN '来访' THEN '来访' ELSE '网信' END ) = '{xfxs}' 
      and x.djjglbdm in ( '0000', '0100', '0200', '0300', '1000', '1100', '1200', '1300', '1400' )
      and x.xfrs >= 1 and x.xfrs <= 9999
      and x.sfnrtj = 1
      and x.xfxsdm in ('100','200','300','303')
      and x.sfssbz=0
  ) t
  on r.region_code = concat(t.wtsddm,'00000000')
 where
   r.region_code like '44__00000000%%'
 group by r.region_code,t.xfxs)
"""
# 责任单位 19个
sql_1_3_all = """(SELECT
	r.company_name,
	r.org_code,
	count( DISTINCT ( t.xfjbh ) ) AS zs,#总数
	count( DISTINCT ( CASE WHEN t.zrdwpjzt = 2 OR t.zrdwpjzt = 3 THEN t.xfjbh END ) ) AS yingpj,#应评价
	count( DISTINCT ( CASE WHEN t.zrdwpjzt = 2 THEN t.xfjbh END ) ) AS ypj,#已评价
	count( DISTINCT ( CASE WHEN ( t.zrdwpjzt = 2 AND t.zrdwmyz = 0 ) THEN t.xfjbh END ) ) AS my,#已评价满意
	count( DISTINCT ( CASE WHEN ( t.zrdwpjzt = 2 AND t.zrdwmyz = 1 ) THEN t.xfjbh END ) ) AS jbmy,#已评价基本满意
	count( DISTINCT ( CASE WHEN ( t.zrdwpjzt = 2 AND t.zrdwmyz = 3 ) THEN t.xfjbh END ) ) AS bmy,#已评价不满意
	count( DISTINCT ( CASE WHEN t.zrdwpjzt = 3 THEN t.xfjbh END ) ) AS cqwpj,#超期未评价
	count( DISTINCT ( CASE WHEN t.zrdwpjzt = 0 OR t.zrdwpjzt IS NULL THEN t.xfjbh END ) ) AS dpj,#待评价
	count( DISTINCT ( CASE WHEN t.zrdwpjzt = 1 THEN t.xfjbh END ) ) AS wpj #未评价
FROM
	xf_org r
	INNER JOIN (
	SELECT DISTINCT
		( x.xfjbh ) AS xfjbh,
		x.wtsddm,
		x.zrdwpjzt,
		x.zrdwpjsj,
		x.zrdwmyz,
		x.pjjzsj,
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
		) #参数3 开始时间begin
		
		AND x.zrdwpjsj >= '{start}' #参数4 终了时间end
		
		AND x.zrdwpjsj < '{end}' #参数3 查询7月28之后登记的数据
#参数5
		
		AND x.djjglbdm IN ( '0000', '0100', '0200', '0300' ) #参数6 信访形式
		
		AND x.xfxsdm IN ( '100', '200', '300', '303' ) #统计范围(是否本机构)
#参数7,8 信访人数
		
		AND x.xfrs >= 1 
		AND x.xfrs <= 9999 -- 查询国家局转交督省内+省内全部
		
		AND x.sfnrtj = 1 
		AND x.xfxsdm IN ( '100', '200', '300', '303' ) 
		AND x.sfssbz = 0 
	) t ON ( t.qxmcdm = r.org_code OR t.djjgdm = r.org_code ) 
WHERE
	r.region_code = '440000000000' 
	AND r.is_choose = '1' 
	AND r.is_petition = 0 
GROUP BY
	r.org_code)"""
sql_1_3_xfxs = """(SELECT
	r.company_name,
	r.org_code,
	t.xfxs,
	count( DISTINCT ( t.xfjbh ) ) AS zs,#总数
	count( DISTINCT ( CASE WHEN t.zrdwpjzt = 2 OR t.zrdwpjzt = 3 THEN t.xfjbh END ) ) AS yingpj,#应评价
	count( DISTINCT ( CASE WHEN t.zrdwpjzt = 2 THEN t.xfjbh END ) ) AS ypj,#已评价
	count( DISTINCT ( CASE WHEN ( t.zrdwpjzt = 2 AND t.zrdwmyz = 0 ) THEN t.xfjbh END ) ) AS my,#已评价满意
	count( DISTINCT ( CASE WHEN ( t.zrdwpjzt = 2 AND t.zrdwmyz = 1 ) THEN t.xfjbh END ) ) AS jbmy,#已评价基本满意
	count( DISTINCT ( CASE WHEN ( t.zrdwpjzt = 2 AND t.zrdwmyz = 3 ) THEN t.xfjbh END ) ) AS bmy,#已评价不满意
	count( DISTINCT ( CASE WHEN t.zrdwpjzt = 3 THEN t.xfjbh END ) ) AS cqwpj,#超期未评价
	count( DISTINCT ( CASE WHEN t.zrdwpjzt = 0 OR t.zrdwpjzt IS NULL THEN t.xfjbh END ) ) AS dpj,#待评价
	count( DISTINCT ( CASE WHEN t.zrdwpjzt = 1 THEN t.xfjbh END ) ) AS wpj #未评价
FROM
	xf_org r
	INNER JOIN (
	SELECT DISTINCT
		( x.xfjbh ) AS xfjbh,
		x.xfxsmc AS xfxs,
		x.wtsddm,
		x.zrdwpjzt,
		x.zrdwpjsj,
		x.zrdwmyz,
		x.pjjzsj,
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
		) #参数3 开始时间begin
		
		AND x.zrdwpjsj >= '{start}' #参数4 终了时间end
		
		AND x.zrdwpjsj < '{end}' #参数3 查询7月28之后登记的数据
#参数5
		
		AND x.djjglbdm IN ( '0000', '0100', '0200', '0300' ) #参数6 信访形式
		
		AND x.xfxsdm IN ( '100', '200', '300', '303' ) #统计范围(是否本机构)
#参数7,8 信访人数
		
		AND x.xfrs >= 1 
		AND x.xfrs <= 9999 -- 查询国家局转交督省内+省内全部
		
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
	t.xfxs)"""

# 2-1 信访部门 市级带县
sql_2_1_all ="""(select 
       r.region_name,
       case when instr(r.region_code,'0000000000')>0 then '省级'
            when instr(r.region_code,'00000000')>0 then '市级'
            when instr(r.region_code,'000000')>0 then '县级'
       end bmjb,
       r.region_code,
       #总数
       count(distinct(t.xfjbh)) as zs,
       #已评价
       count(distinct(case
              when t.xfbmpjzt = 2 then t.xfjbh
          end)) as ypj,
       #已评价满意
       count(distinct(case
              when (t.xfbmpjzt = 2 and t.xfbmmyz = 0) 
              then t.xfjbh
          end)) as my,
       #已评价基本满意
       count(distinct(case
              when (t.xfbmpjzt = 2 and t.xfbmmyz = 1) 
              then t.xfjbh
          end)) as jbmy,
       #已评价不满意
       count(distinct(case
              when (t.xfbmpjzt = 2 and t.xfbmmyz = 3) 
              then t.xfjbh
          end)) as bmy,
       #超期未评价
       count(distinct(case
              when t.xfbmpjzt = 3
              then t.xfjbh
          end)) as cqwpj,
       #待评价
       count(distinct(case
              when t.xfbmpjzt = 0 or t.xfbmpjzt is null
              then t.xfjbh
          end)) as dpj,
       #未评价
       count(distinct(case
              when t.xfbmpjzt = 1
              then t.xfjbh
          end)) as wpj
  from rpt_region r
  left join
  (select 
      distinct(x.xfjbh) as xfjbh,
      substr(IFNULL(x.zjqxdm,x.wtsddm), 1, 6) as wtsddm,
      x.xfbmpjzt,
      x.xfbmpjsj,
      x.xfbmmyz,
      x.pjjzsj
    from rpt_xfjxx x
    inner join rpt_blfsxx b on x.xfjbh = b.xfjbh and b.blfsdm in ('010000','020000','030000')
    where 1=1
      AND x.xfbmpjsj>= '{start}'
      AND x.xfbmpjsj <= '{end}'  
      and x.djjglbdm in  ( '0000', '0100', '0200', '0300', '1000', '1100', '1200', '1300', '1400' )
      and x.xfrs >= 1 and x.xfrs <= 9999
      and x.sfnrtj = 1
      and x.xfxsdm in ('100','200','300','303')
      and x.sfssbz=0
  ) t
  on r.region_code = concat(t.wtsddm,'000000')
 where
  r.region_code like '44____000000%%'
  and substr(r.region_code,1,4) =(select substr(region_code,1,4) from rpt_region where region_name='{Cqh}') 
  group by r.region_code)"""
sql_2_1_xfxs ="""(select 
       r.region_name,
       case when instr(r.region_code,'0000000000')>0 then '省级'
            when instr(r.region_code,'00000000')>0 then '市级'
            when instr(r.region_code,'000000')>0 then '县级'
       end bmjb,
       r.region_code,
       t.xfxs,
       #总数
       count(distinct(t.xfjbh)) as zs,
       #已评价
       count(distinct(case
              when t.xfbmpjzt = 2 then t.xfjbh
          end)) as ypj,
       #已评价满意
       count(distinct(case
              when (t.xfbmpjzt = 2 and t.xfbmmyz = 0) 
              then t.xfjbh
          end)) as my,
       #已评价基本满意
       count(distinct(case
              when (t.xfbmpjzt = 2 and t.xfbmmyz = 1) 
              then t.xfjbh
          end)) as jbmy,
       #已评价不满意
       count(distinct(case
              when (t.xfbmpjzt = 2 and t.xfbmmyz = 3) 
              then t.xfjbh
          end)) as bmy,
       #超期未评价
       count(distinct(case
              when t.xfbmpjzt = 3
              then t.xfjbh
          end)) as cqwpj,
       #待评价
       count(distinct(case
              when t.xfbmpjzt = 0 or t.xfbmpjzt is null
              then t.xfjbh
          end)) as dpj,
       #未评价
       count(distinct(case
              when t.xfbmpjzt = 1
              then t.xfjbh
          end)) as wpj
  from rpt_region r
  left join
  (select 
      distinct(x.xfjbh) as xfjbh,
      substr(IFNULL(x.zjqxdm,x.wtsddm), 1, 6) as wtsddm,
			CASE										
				WHEN x.xfxsmc = '来信' THEN
				'来信' 
				WHEN x.xfxsmc = '来访' THEN
				'来访' ELSE '网信' 
			END xfxs,
      x.xfbmpjzt,
      x.xfbmpjsj,
      x.xfbmmyz,
      x.pjjzsj
    from rpt_xfjxx x
    inner join rpt_blfsxx b on x.xfjbh = b.xfjbh and b.blfsdm in ('010000','020000','030000')
    where 1=1
      AND x.xfbmpjsj>= '{start}'
      AND x.xfbmpjsj <= '{end}'  
      AND ( CASE x.xfxsmc WHEN '来信' THEN '来信' WHEN '来访' THEN '来访' ELSE '网信' END ) = '{xfxs}' 
      and x.djjglbdm in  ( '0000', '0100', '0200', '0300', '1000', '1100', '1200', '1300', '1400' )
      and x.xfrs >= 1 and x.xfrs <= 9999
      and x.sfnrtj = 1
      and x.xfxsdm in ('100','200','300','303')
      and x.sfssbz=0
  ) t
  on r.region_code = concat(t.wtsddm,'000000')
 where
  r.region_code like '44____000000%%'
  and substr(r.region_code,1,4) =(select substr(region_code,1,4) from rpt_region where region_name='{Cqh}') 
  group by r.region_code,t.xfxs)"""

# 2-2 责任单位 市级带县

sql_2_2_all ="""(select 
       r.region_name,
			 case when instr(r.region_code,'0000000000')>0 then '省级'
            when instr(r.region_code,'00000000')>0 then '市级'
            when instr(r.region_code,'000000')>0 then '县级'
       end bmjb,
       r.region_code,
       #总数
       count(distinct(t.xfjbh)) as zs,
       #应评价
       count(distinct(case
              when t.zrdwpjzt = 2 or t.zrdwpjzt = 3 then t.xfjbh
          end)) as yingpj,
       #已评价
       count(distinct(case
              when t.zrdwpjzt = 2 then t.xfjbh
          end)) as ypj,
       #已评价满意
       count(distinct(case
              when (t.zrdwpjzt = 2 and t.zrdwmyz = 0) 
              then t.xfjbh
          end)) as my,
       #已评价基本满意
       count(distinct(case
              when (t.zrdwpjzt = 2 and t.zrdwmyz = 1) 
              then t.xfjbh
          end)) as jbmy,
       #已评价不满意
       count(distinct(case
              when (t.zrdwpjzt = 2 and t.zrdwmyz = 3) 
              then t.xfjbh
          end)) as bmy,
       #超期未评价
       count(distinct(case
              when t.zrdwpjzt = 3
              then t.xfjbh
          end)) as cqwpj,
       #待评价
       count(distinct(case
              when t.zrdwpjzt = 0 or t.zrdwpjzt is null
              then t.xfjbh
          end)) as dpj,
       #未评价
       count(distinct(case
              when t.zrdwpjzt = 1
              then t.xfjbh
          end)) as wpj
  from rpt_region r
  left join
  (select 
      distinct(x.xfjbh) as xfjbh,
      substr(IFNULL(x.zjqxdm,x.wtsddm), 1, 6) as wtsddm,
      x.zrdwpjzt,
      x.zrdwpjsj,
      x.zrdwmyz,
      x.pjjzsj
    from rpt_xfjxx x
    inner join rpt_blfsxx b on x.xfjbh = b.xfjbh and b.blfsdm in ('010000','020000','030000')
    where 1=1
      and x.zrdwpjsj >= '{start}'
      and x.zrdwpjsj < '{end}'  
      and x.djjglbdm in ( '0000', '0100', '0200', '0300', '1000', '1100', '1200', '1300', '1400' )
      and x.xfrs >= 1 and x.xfrs <= 9999
      and x.sfnrtj = 1
      and x.xfxsdm in ('100','200','300','303')
      and x.sfssbz=0
  ) t
  on r.region_code = concat(t.wtsddm,'000000')
 where
   r.region_code like '44____000000%%'
   and substr(r.region_code,1,4) =(select substr(region_code,1,4) from rpt_region where region_name='{Cqh}') 
 group by r.region_code
)"""
sql_2_2_xfxs ="""(select 
       r.region_name,
			 case when instr(r.region_code,'0000000000')>0 then '省级'
            when instr(r.region_code,'00000000')>0 then '市级'
            when instr(r.region_code,'000000')>0 then '县级'
       end bmjb,
       r.region_code,
       t.xfxs,
       #总数
       count(distinct(t.xfjbh)) as zs,
       #应评价
       count(distinct(case
              when t.zrdwpjzt = 2 or t.zrdwpjzt = 3 then t.xfjbh
          end)) as yingpj,
       #已评价
       count(distinct(case
              when t.zrdwpjzt = 2 then t.xfjbh
          end)) as ypj,
       #已评价满意
       count(distinct(case
              when (t.zrdwpjzt = 2 and t.zrdwmyz = 0) 
              then t.xfjbh
          end)) as my,
       #已评价基本满意
       count(distinct(case
              when (t.zrdwpjzt = 2 and t.zrdwmyz = 1) 
              then t.xfjbh
          end)) as jbmy,
       #已评价不满意
       count(distinct(case
              when (t.zrdwpjzt = 2 and t.zrdwmyz = 3) 
              then t.xfjbh
          end)) as bmy,
       #超期未评价
       count(distinct(case
              when t.zrdwpjzt = 3
              then t.xfjbh
          end)) as cqwpj,
       #待评价
       count(distinct(case
              when t.zrdwpjzt = 0 or t.zrdwpjzt is null
              then t.xfjbh
          end)) as dpj,
       #未评价
       count(distinct(case
              when t.zrdwpjzt = 1
              then t.xfjbh
          end)) as wpj
  from rpt_region r
  left join
  (select 
      distinct(x.xfjbh) as xfjbh,
			CASE										
				WHEN x.xfxsmc = '来信' THEN
				'来信' 
				WHEN x.xfxsmc = '来访' THEN
				'来访' ELSE '网信' 
			END xfxs,
      substr(IFNULL(x.zjqxdm,x.wtsddm), 1, 6) as wtsddm,
      x.zrdwpjzt,
      x.zrdwpjsj,
      x.zrdwmyz,
      x.pjjzsj
    from rpt_xfjxx x
    inner join rpt_blfsxx b on x.xfjbh = b.xfjbh and b.blfsdm in ('010000','020000','030000')
    where 1=1
      and x.zrdwpjsj >= '{start}'
      and x.zrdwpjsj < '{end}'  
      AND ( CASE x.xfxsmc WHEN '来信' THEN '来信' WHEN '来访' THEN '来访' ELSE '网信' END ) = '{xfxs}' 
      and x.djjglbdm in ( '0000', '0100', '0200', '0300', '1000', '1100', '1200', '1300', '1400' )
      and x.xfrs >= 1 and x.xfrs <= 9999
      and x.sfnrtj = 1
      and x.xfxsdm in ('100','200','300','303')
      and x.sfssbz=0
  ) t
  on r.region_code = concat(t.wtsddm,'000000')
 where
   r.region_code like '44____000000%%'
   and substr(r.region_code,1,4) =(select substr(region_code,1,4) from rpt_region where region_name='{Cqh}') 
 group by r.region_code,t.xfxs)"""

