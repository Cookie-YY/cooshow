sql_1_2_all = """(select 
       r.region_name,       
       case when instr(r.region_code,'0000000000')>0 then '省级'
            when instr(r.region_code,'00000000')>0 then '市级'
            when instr(r.region_code,'000000')>0 then '县级'
       end bmjb,
       r.region_code,
       count(distinct(t.xfjbh)) as zs,
       count(distinct(case 
              when (t.sjslsj is not null or t.shijslsj is not null or t.xjslsj is not null)
              then t.xfjbh
          end)) as ysl,
       count(distinct(case
              when least(ifnull(t.sjslsj,SYSDATE()),ifnull(t.shijslsj,SYSDATE()),ifnull(t.xjslsj,SYSDATE())) <= DATE_ADD( t.djsj, INTERVAL 15 DAY )
              and least(ifnull(t.sjslsj,SYSDATE()),ifnull(t.shijslsj,SYSDATE()),ifnull(t.xjslsj,SYSDATE())) <> SYSDATE()
              then t.xfjbh
          end)) as jssl,
       count(distinct(case
              when least(ifnull(t.sjslsj,SYSDATE()),ifnull(t.shijslsj,SYSDATE()),ifnull(t.xjslsj,SYSDATE())) > DATE_ADD( t.djsj, INTERVAL 15 DAY )
              and least(ifnull(t.sjslsj,SYSDATE()),ifnull(t.shijslsj,SYSDATE()),ifnull(t.xjslsj,SYSDATE())) <> SYSDATE()
              then t.xfjbh
          end)) as cqsl,
       count(distinct(case
              when (t.sjslsj is null and t.shijslsj is null and t.xjslsj is null)
              and SYSDATE() > DATE_ADD( t.djsj, INTERVAL 15 DAY )
              then t.xfjbh
          end)) as cqwsl
  from rpt_region r
  left join
  (select 
      distinct x.xfjbh,
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
      and DATE_ADD( x.djsj, INTERVAL 15 DAY ) >= '{start}'
      and DATE_ADD( x.djsj, INTERVAL 15 DAY ) <= '{end}'
      and x.check_flag = 0
      and x.djjglbdm in ('0000','0100','0200','0300')
      and x.xfrs >= 1 and x.xfrs <= 9999
      and x.sfnrtj = 1
      and x.xfxsdm in ('100','200','300','303','600')
  ) t
  on r.region_code = concat(t.wtsddm,'00000000')
 where
  r.region_code like '44__00000000%%'
 group by r.region_code)"""

sql_1_2_xfxs = """(select 
       r.region_name,       
       case when instr(r.region_code,'0000000000')>0 then '省级'
            when instr(r.region_code,'00000000')>0 then '市级'
            when instr(r.region_code,'000000')>0 then '县级'
       end bmjb,
       r.region_code,
       t.xfxs,
       count(distinct(t.xfjbh)) as zs,
       count(distinct(case 
              when (t.sjslsj is not null or t.shijslsj is not null or t.xjslsj is not null)
              then t.xfjbh
          end)) as ysl,
       count(distinct(case
              when least(ifnull(t.sjslsj,SYSDATE()),ifnull(t.shijslsj,SYSDATE()),ifnull(t.xjslsj,SYSDATE())) <= DATE_ADD( t.djsj, INTERVAL 15 DAY )
              and least(ifnull(t.sjslsj,SYSDATE()),ifnull(t.shijslsj,SYSDATE()),ifnull(t.xjslsj,SYSDATE())) <> SYSDATE()
              then t.xfjbh
          end)) as jssl,
       count(distinct(case
              when least(ifnull(t.sjslsj,SYSDATE()),ifnull(t.shijslsj,SYSDATE()),ifnull(t.xjslsj,SYSDATE())) > DATE_ADD( t.djsj, INTERVAL 15 DAY )
              and least(ifnull(t.sjslsj,SYSDATE()),ifnull(t.shijslsj,SYSDATE()),ifnull(t.xjslsj,SYSDATE())) <> SYSDATE()
              then t.xfjbh
          end)) as cqsl,
       count(distinct(case
              when (t.sjslsj is null and t.shijslsj is null and t.xjslsj is null)
              and SYSDATE() > DATE_ADD( t.djsj, INTERVAL 15 DAY )
              then t.xfjbh
          end)) as cqwsl
  from rpt_region r
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
      and DATE_ADD( x.djsj, INTERVAL 15 DAY ) >= '{start}'
      and DATE_ADD( x.djsj, INTERVAL 15 DAY ) <= '{end}' 
      and (case x.xfxsmc when '来信' then '来信' when '来访' then '来访' else '网信' end)='网信'
      and x.check_flag = 0
      and x.djjglbdm in ('0000','0100','0200','0300')
      and x.xfrs >= 1 and x.xfrs <= 9999
      and x.sfnrtj = 1
      and x.xfxsdm in ('100','200','300','303','600')
  ) t
  on r.region_code = concat(t.wtsddm,'00000000')
 where
  r.region_code like '44__00000000%%'
 group by r.region_code,t.xfxs)"""

sql_1_4_all = """(select 
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
     and DATE_ADD( x.djsj, INTERVAL 15 DAY ) >= '{start}'
     and DATE_ADD( x.djsj, INTERVAL 15 DAY ) <= '{end}'
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
group by r.region_code)"""

sql_1_4_xfxs = """(select 
      r.region_name,
      case when instr(r.region_code,'0000000000')>0 then '省级'
           when instr(r.region_code,'00000000')>0 then '市级'
           when instr(r.region_code,'000000')>0 then '县级'
      end bmjb,
      r.region_code,
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
 from rpt_region r
 left join
 (select 
     distinct x.xfjbh,
     case when x.xfxsmc='来信' then '来信' when x.xfxsmc='来访' then '来访' else '网信' end xfxs,
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
     and DATE_ADD( x.djsj, INTERVAL 15 DAY ) >= '{start}'
     and DATE_ADD( x.djsj, INTERVAL 15 DAY ) <= '{end}'
     and (case x.xfxsmc when '来信' then '来信' when '来访' then '来访' else '网信' end)='网信'
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
group by r.region_code,t.xfxs)"""

sql_1_5_all = """(select 
       r.region_name,
       case when instr(r.region_code,'0000000000')>0 then '省级'
            when instr(r.region_code,'00000000')>0 then '市级'
            when instr(r.region_code,'000000')>0 then '县级'
       end bmjb,
       r.region_code,
       r.company_name,
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
      and DATE_ADD( x.djsj, INTERVAL 15 DAY ) >= '{start}'
      and DATE_ADD( x.djsj, INTERVAL 15 DAY ) <= '{end}'
      and x.check_flag = 0
      and x.djjglbdm in ('0000','0100','0200','0300')
      and x.xfrs >= 1 and x.xfrs <= 9999
      and x.sfnrtj = 1
      and x.xfxsdm in ('100','200','300','303','600')
  ) t
  on r.region_code = concat(t.wtsddm,'00000000')
 where  r.region_code like '44__00000000%%'
  group by r.region_code,r.company_name)"""

sql_1_5_xfxs = """(select 
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
      and DATE_ADD( x.djsj, INTERVAL 15 DAY ) >= '{start}'
      and DATE_ADD( x.djsj, INTERVAL 15 DAY ) <= '{end}'
      and (case x.xfxsmc when '来信' then '来信' when '来访' then '来访' else '网信' end)='网信'
      and x.check_flag = 0
      and x.djjglbdm in ('0000','0100','0200','0300')
      and x.xfrs >= 1 and x.xfrs <= 9999
      and x.sfnrtj = 1
      and x.xfxsdm in ('100','200','300','303','600')
  ) t
  on r.region_code = concat(t.wtsddm,'00000000')
 where  r.region_code like '44__00000000%%'
  group by r.region_code,r.company_name,t.xfxs)"""

sql_1_6_all = """(select 
       r.region_name,
       case when instr(r.region_code,'0000000000')>0 then '省级'
            when instr(r.region_code,'00000000')>0 then '市级'
            when instr(r.region_code,'000000')>0 then '县级'
       end bmjb,
       r.region_code,
       r.company_name,
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
      and DATE_ADD( x.djsj, INTERVAL 15 DAY ) >= '{start}'
      and DATE_ADD( x.djsj, INTERVAL 15 DAY ) <= '{end}' 
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
 group by r.region_code,r.company_name)"""

sql_1_6_xfxs = """(select 
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
     and DATE_ADD( x.djsj, INTERVAL 15 DAY ) >= '{start}'
     and DATE_ADD( x.djsj, INTERVAL 15 DAY ) <= '{end}'
     and (case x.xfxsmc when '来信' then '来信' when '来访' then '来访' else '网信' end)='网信'
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
group by r.region_code,r.company_name,t.xfxs)"""

sql_2_2_all = """(select 
      r.region_name,
      case when instr(r.region_code,'0000000000')>0 then '省级'
           when instr(r.region_code,'00000000')>0 then '市级'
           when instr(r.region_code,'000000')>0 then '县级'
      end bmjb,
      r.region_code,
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
     substr(IFNULL(IFNULL(e.qxjgdm,y.zjbljgdm),x.wtsddm), 1, 4) as wtsddm,
     x.zrdwslsj,
     x.djsj
   from rpt_xfjxx x
   left JOIN xf_dbxx e ON e.xfjbh = x.xfjbh
   LEFT JOIN xf_ybinfo y ON x.xfjbh = y.xfjbh
   where 1=1
     and x.check_flag = 0
     and DATE_ADD( x.djsj, INTERVAL 30 DAY ) >= '{start}'
     and DATE_ADD( x.djsj, INTERVAL 30 DAY ) <= '{end}'  
     and x.djjglbdm in ('0000','0100','0200','0300','1000','1100','1200','1300','1400')
     and x.xfrs >= 1 and x.xfrs <= 9999
     and x.qxsfzrdw = 1
     and x.sfnrtj = 1
     and x.xfxsdm in ('100','200','300','303','600')
 ) t
 on r.region_code = concat(t.wtsddm,'00000000')
where
 r.region_code like '44__00000000%%'
 group by r.region_code)"""

sql_2_2_xfxs = """(select 
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
      and DATE_ADD( x.djsj, INTERVAL 30 DAY ) >= '{start}'
      and DATE_ADD( x.djsj, INTERVAL 30 DAY ) <= '{end}'  
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
  group by r.region_code,xfxs)"""

sql_2_4_all = """(select 
       r.region_name,
       case when instr(r.region_code,'0000000000')>0 then '省级'
            when instr(r.region_code,'00000000')>0 then '市级'
            when instr(r.region_code,'000000')>0 then '县级'
       end bmjb,
       r.region_code,
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
      substr(IFNULL(IFNULL(e.qxjgdm,y.zjbljgdm),x.wtsddm), 1, 6) as wtsddm,
      x.zrdwslsj,
      x.djsj
    from rpt_xfjxx x
    left JOIN xf_dbxx e ON e.xfjbh = x.xfjbh
    LEFT JOIN xf_ybinfo y ON x.xfjbh = y.xfjbh
    where 1=1
      and x.check_flag = 0
      and DATE_ADD( x.djsj, INTERVAL 30 DAY ) >= '{start}'
      and DATE_ADD( x.djsj, INTERVAL 30 DAY ) <= '{end}'
      and x.djjglbdm in ('0000','0100','0200','0300','1000','1100','1200','1300','1400')
      and x.xfrs >= 1 and x.xfrs <= 9999
      and x.qxsfzrdw = 1
      and x.sfnrtj = 1
      and x.xfxsdm in ('100','200','300','303','600')
  ) t
  on r.region_code = concat(t.wtsddm,'000000')
 where
  r.region_code like '44____000000%%'
  and r.region_code<>'440000000000'
  and substr(r.region_code,1,4) =(select substr(region_code,1,4) from rpt_region where region_name='广州市') 
  group by r.region_code)"""

sql_2_4_xfxs = """(select 
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
     substr(IFNULL(IFNULL(e.qxjgdm,y.zjbljgdm),x.wtsddm), 1, 6) as wtsddm,
     x.zrdwslsj,
     x.djsj
   from rpt_xfjxx x
   left JOIN xf_dbxx e ON e.xfjbh = x.xfjbh
   LEFT JOIN xf_ybinfo y ON x.xfjbh = y.xfjbh
   where 1=1
     and x.check_flag = 0
     and DATE_ADD( x.djsj, INTERVAL 30 DAY ) >= '{start}'
     and DATE_ADD( x.djsj, INTERVAL 30 DAY ) <= '{end}' 
     and (case x.xfxsmc when '来信' then '来信' when '来访' then '来访' else '网信' end)='网信'
     and x.djjglbdm in ('0000','0100','0200','0300','1000','1100','1200','1300','1400')
     and x.xfrs >= 1 and x.xfrs <= 9999
     and x.qxsfzrdw = 1
     and x.sfnrtj = 1
     and x.xfxsdm in ('100','200','300','303','600')
 ) t
 on r.region_code = concat(t.wtsddm,'000000')
where
 r.region_code like '44____000000%%'
 and r.region_code<>'440000000000'
 and substr(r.region_code,1,4) =(select substr(region_code,1,4) from rpt_region where region_name='广州市') 
 group by r.region_code,xfxs)"""

sql_2_5_all = """(select 
       r.region_name,
       r.company_name,
       r.org_code,
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
  from (select company_name,org_code,b.region_code,b.region_name from xf_org a,xf_region b where a.region_code=b.region_code and a.is_petition=0) r
  left join
  (select 
      distinct(x.xfjbh) as xfjbh,
      x.wtsddm,
      x.zrdwslsj,
      x.djsj,
      x.zjqxdm,
      x.djjgdm,
      b.qxmcdm
    from rpt_xfjxx x
    left join rpt_blfsxx b on x.xfjbh = b.xfjbh
    where 1=1
      and DATE_ADD( x.djsj, INTERVAL 30 DAY ) >= '{start}'
      and DATE_ADD( x.djsj, INTERVAL 30 DAY ) <= '{end}'
      and x.check_flag = 0
      and x.djjglbdm in ('0000','0100','0200','0300','1100','1200','1300','1400')
      and x.xfrs >= 1 and x.xfrs <= 9999
      and x.qxsfzrdw = 1
      and x.sfnrtj = 1
      and x.xfxsdm in ('100','200','300','303','600')
  ) t
  on (t.qxmcdm = r.org_code or t.djjgdm = r.org_code)
where r.region_name={Cqh}  
group by r.region_name,r.org_code)"""

sql_2_5_xfxs = """(select 
       r.region_name,
       r.company_name,
       r.org_code,
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
  from (select company_name,org_code,b.region_code,b.region_name from xf_org a,xf_region b where a.region_code=b.region_code and a.is_petition=0) r
  left join
  (select 
      distinct(x.xfjbh) as xfjbh,
      case when x.xfxsmc='来信' then '来信' when x.xfxsmc='来访' then '来访' else '网信' end xfxs,
      x.wtsddm,
      x.zrdwslsj,
      x.djsj,
      x.zjqxdm,
      x.djjgdm,
      b.qxmcdm
    from rpt_xfjxx x
    left join rpt_blfsxx b on x.xfjbh = b.xfjbh
    where 1=1
      and DATE_ADD( x.djsj, INTERVAL 30 DAY ) >= '{start}'
      and DATE_ADD( x.djsj, INTERVAL 30 DAY ) <= '{end}'
      and (case x.xfxsmc when '来信' then '来信' when '来访' then '来访' else '网信' end)='网信' 
      and x.check_flag = 0
      and x.djjglbdm in ('0000','0100','0200','0300','1100','1200','1300','1400')
      and x.xfrs >= 1 and x.xfrs <= 9999
      and x.qxsfzrdw = 1
      and x.sfnrtj = 1
      and x.xfxsdm in ('100','200','300','303','600')
  ) t
  on (t.qxmcdm = r.org_code or t.djjgdm = r.org_code)
where r.region_name={Cqh}  
group by r.region_name,r.org_code,xfxs)"""