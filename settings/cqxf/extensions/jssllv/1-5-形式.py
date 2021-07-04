def getter():
    return {"1-5-形式": """(select 
       r.region_name,
       case when instr(r.region_code,'0000000000')>0 then '省级'
            when instr(r.region_code,'00000000')>0 then '市级'
            when instr(r.region_code,'000000')>0 then '县级'
       end bmjb,
       r.region_code,
       r.company_name,
       t.xfxs,
       -- 总数
       count(distinct(t.xfjbh)) as zs,
       -- 已受理
       count(distinct(case 
              when (t.sjslsj is not null or t.shijslsj is not null or t.xjslsj is not null)
              then t.xfjbh
          end)) as ysl,
       -- 及时受理
       count(distinct(case
              when least(ifnull(t.sjslsj,SYSDATE()),ifnull(t.shijslsj,SYSDATE()),ifnull(t.xjslsj,SYSDATE())) <= DATE_ADD( t.djsj, INTERVAL 15 DAY )
              and least(ifnull(t.sjslsj,SYSDATE()),ifnull(t.shijslsj,SYSDATE()),ifnull(t.xjslsj,SYSDATE())) <> SYSDATE()
              then t.xfjbh
          end)) as jssl,
       -- 超期受理
       count(distinct(case
              when least(ifnull(t.sjslsj,SYSDATE()),ifnull(t.shijslsj,SYSDATE()),ifnull(t.xjslsj,SYSDATE())) > DATE_ADD( t.djsj, INTERVAL 15 DAY )
              and least(ifnull(t.sjslsj,SYSDATE()),ifnull(t.shijslsj,SYSDATE()),ifnull(t.xjslsj,SYSDATE())) <> SYSDATE()
              then t.xfjbh
          end)) as cqsl,
       -- 超期未受理
       count(distinct(case
              when (t.sjslsj is null and t.shijslsj is null and t.xjslsj is null)
              and SYSDATE() > DATE_ADD( t.djsj, INTERVAL 15 DAY )
              then t.xfjbh
          end)) as cqwsl
  from (select company_name,org_code,b.region_code,b.region_name from xf_org a,rpt_region b where a.region_code=b.region_code and a.is_petition=1) r
  left join
  (select 
      distinct x.xfjbh,
      case when x.xfxsmc='来信' then '来信' when x.xfxsmc='来访' then '来访' else '网信' end xfxs,
      substr(IFNULL(IFNULL(e.qxjgdm,y.zjbljgdm),x.wtsddm), 1, 4) as wtsddm,
      x.sjslsj,
      x.shijslsj,
      x.xjslsj,
      x.ddzrdwsj,
      x.djsj
    from rpt_xfjxx x
    LEFT JOIN xf_dbxx e ON e.xfjbh = x.xfjbh
    LEFT JOIN xf_ybinfo y ON x.xfjbh = y.xfjbh
    where 1=1
      and DATE_ADD( x.djsj, INTERVAL 15 DAY ) >= {start}
      and DATE_ADD( x.djsj, INTERVAL 15 DAY ) <= {end}
      and (case x.xfxsmc when '来信' then '来信' when '来访' then '来访' else '网信' end)='网信'
      and x.check_flag = 0
      and x.djjglbdm in ('0000','0100','0200','0300')
      and x.xfrs >= 1 and x.xfrs <= 9999
      and x.sfnrtj = 1
      and x.xfxsdm in ('100','200','300','303','600')
  ) t
  on r.region_code = concat(t.wtsddm,'00000000')
 where  r.region_code like '44__00000000%%'
  group by r.region_code,r.company_name,t.xfxs)"""}