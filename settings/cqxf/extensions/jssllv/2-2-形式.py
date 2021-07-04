def getter():
    return {"2-2-形式": """(select 
       r.region_name,
       case when instr(r.region_code,'0000000000')>0 then '省级'
            when instr(r.region_code,'00000000')>0 then '市级'
            when instr(r.region_code,'000000')>0 then '县级'
       end bmjb,
       r.region_code,
       xfxs,
       #总数
       count(distinct(t.xfjbh)) as zs,
       #已受理
       count(distinct(case
              when t.zrdwslsj is not null then t.xfjbh
          end)) as ysl,
       #及时受理
       count(distinct(case
              when (t.zrdwslsj is not null and t.zrdwslsj <= DATE_ADD( t.djsj, INTERVAL 30 DAY )) 
              then t.xfjbh
          end)) as jssl,
       #超期受理
       count(distinct(case
              when (t.zrdwslsj is not null and t.zrdwslsj > DATE_ADD( t.djsj, INTERVAL 30 DAY )) 
              then t.xfjbh
          end)) as cqsl,
       #超期未受理
       count(distinct(case
              when t.zrdwslsj is null and SYSDATE() > DATE_ADD( t.djsj, INTERVAL 30 DAY )
              then t.xfjbh
          end)) as cqwsl
  from rpt_region r
  left join
  (select 
      distinct(x.xfjbh) as xfjbh,
      case when x.xfxsmc='来信' then '来信' when x.xfxsmc='来访' then '来访' else '网信' end xfxs,
      substr(IFNULL(IFNULL(e.qxjgdm,y.zjbljgdm),x.wtsddm), 1, 4) as wtsddm,
      x.zrdwslsj,
      x.djsj
    from rpt_xfjxx x
    left JOIN xf_dbxx e ON e.xfjbh = x.xfjbh
    LEFT JOIN xf_ybinfo y ON x.xfjbh = y.xfjbh
    where 1=1
      and x.check_flag = 0
      and DATE_ADD( x.djsj, INTERVAL 30 DAY ) >= {start}
      and DATE_ADD( x.djsj, INTERVAL 30 DAY ) <= {end}  
      and (case x.xfxsmc when '来信' then '来信' when '来访' then '来访' else '网信' end)='网信'
      and x.djjglbdm in ('0000','0100','0200','0300','1000','1100','1200','1300','1400')
      and x.xfrs >= 1 and x.xfrs <= 9999
      and x.qxsfzrdw = 1
      and x.sfnrtj = 1
      and x.xfxsdm in ('100','200','300','303','600')
  ) t
  on r.region_code = concat(t.wtsddm,'00000000')
 where
  r.region_code like '44__00000000%%'
  group by r.region_code,xfxs)"""}