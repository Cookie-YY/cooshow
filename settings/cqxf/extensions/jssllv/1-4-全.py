def getter():
    return {"1-4-全": """(select 
      r.region_name,
      case when instr(r.region_code,'0000000000')>0 then '省级'
           when instr(r.region_code,'00000000')>0 then '市级'
           when instr(r.region_code,'000000')>0 then '县级'
      end bmjb,
      r.region_code,
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
 from rpt_region r
 left join
 (select 
     distinct x.xfjbh,
     substr(IFNULL(IFNULL(e.qxjgdm,y.zjbljgdm),x.wtsddm), 1, 6) as wtsddm,
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
     and x.check_flag = 0
     and x.djjglbdm in ('0000','0100','0200','0300')
     and x.xfrs >= 1 and x.xfrs <= 9999
     and x.sfnrtj = 1
     and x.xfxsdm in ('100','200','300','303','600')
 ) t
 on r.region_code = concat(t.wtsddm,'000000')
where
 r.region_code like '44____000000%%'
 and r.region_code<>'440000000000'
 and substr(r.region_code,1,4) =(select substr(region_code,1,4) from rpt_region where region_name='广州市') 
group by r.region_code)"""}