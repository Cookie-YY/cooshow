def getter():
    return """(select 
       r.region_name,
       r.region_code,
       count(distinct(t.xfjbh)) as ydfzs,
       count(distinct(case
              when t.bjbz = 1 then t.xfjbh
          end)) as ydf,
       count(distinct(case
              when (t.bjbz = 1 and t.bjsj <= t.xbjzsj) 
              then t.xfjbh
          end)) as aqdf,
       count(distinct(case
              when (t.bjbz = 1 and t.bjsj > t.xbjzsj) 
              then t.xfjbh
          end)) as cqdf,
       count(distinct(case
              when t.bjbz = 0 and SYSDATE() <= t.xbjzsj
              then t.xfjbh
          end)) as wdf,
       count(distinct(case
              when t.bjbz = 0 and SYSDATE() > t.xbjzsj
              then t.xfjbh
          end)) as cqwdf
  from rpt_region r
  left join
  (select 
      distinct(x.xfjbh) as xfjbh,
      substr(IFNULL(IFNULL(e.qxjgdm,y.zjbljgdm),x.wtsddm), 1, 4) as wtsddm,
      x.ddzrdwsj,
      x.zrdwslsj,
      x.bjbz,
      x.xbjzsj,
      x.bjsj,
      x.dfsj
    from rpt_xfjxx x
    LEFT JOIN xf_dbxx e ON e.xfjbh = x.xfjbh
    LEFT JOIN xf_ybinfo y ON x.xfjbh = y.xfjbh
    where 1=1
      and x.xbjzsj >= {start}
      and x.xbjzsj <= {end}
      and x.djjglbdm in ('0000','0100','0200','0300','1000','1100','1200','1300','1400')
      and x.xfrs >= 1 and x.xfrs <= 9999
      and x.check_flag = 0
      and x.sfnrtj = 1
      and x.xfxsdm in ('100','200','300','303','600')
  ) t
  on r.region_code = concat(t.wtsddm,'00000000')
 where
  r.region_code like '44__00000000%%'
  group by r.region_code)"""