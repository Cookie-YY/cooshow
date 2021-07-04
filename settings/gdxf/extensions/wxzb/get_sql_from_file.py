sql_1_1_all = """
(SELECT r.region_name,
       r.region_code,
       case when instr(r.region_code,'0000000000')>0 then '省级'
            when instr(r.region_code,'00000000')>0 then '市级'
            when instr(r.region_code,'000000')>0 then '县级'
       end bmjb,
       count( t.xfjbh ) as zs, 
       count( case when t.xfxsdm in ('300','303')
          then t.xfjbh 
       end) as wxsl from rpt_region r
  left join
  (select 
      distinct(x.xfjbh) as xfjbh,
      substr(IFNULL(x.zjqxdm,x.wtsddm), 1, 4) as wtsddm,
      x.xfxsdm
    from rpt_xfjxx x
    where 1=1
       AND x.djsj>= '{start}'
       AND x.djsj <= '{end}' 
       and x.djjglbdm in ('0100','0200','0300')
       and x.xfrs >= 1 and x.xfrs <= 9999
       and x.xfxsdm in ('100','200','300','303')
       and x.sfssbz=0
  ) t
  on r.region_code = concat(t.wtsddm,'00000000')
 where
  r.region_code like '44__00000000%%'
 group by r.region_code)
"""
sql_1_2_all = """(SELECT r.region_name,
       r.region_code,
       case when instr(r.region_code,'0000000000')>0 then '省级'
            when instr(r.region_code,'00000000')>0 then '市级'
            when instr(r.region_code,'000000')>0 then '县级'
       end bmjb,
       count( t.xfjbh ) as zs, 
       count( case when t.xfxsdm in ('300','303')
          then t.xfjbh 
       end) as wxsl from rpt_region r
  left join
  (select 
      distinct(x.xfjbh) as xfjbh,
      substr(IFNULL(x.zjqxdm,x.wtsddm), 1, 6) as wtsddm,
      x.xfxsdm
    from rpt_xfjxx x
    where 1=1
       AND x.djsj>= '{start}'
       AND x.djsj <= '{end}' 
       and x.djjglbdm in ('0100','0200','0300')
       and x.xfrs >= 1 and x.xfrs <= 9999
       and x.xfxsdm in ('100','200','300','303')
       and x.sfssbz=0
  ) t
  on r.region_code = concat(t.wtsddm,'000000')
 where
  r.region_code like '44____000000%%'
  and substr(r.region_code,1,4) =(select substr(region_code,1,4) from rpt_region where region_name='{Cqh}') 
 group by r.region_code)"""