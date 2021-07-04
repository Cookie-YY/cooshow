def getter():
    return {'2-5-形式': """(select 
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
      and DATE_ADD( x.djsj, INTERVAL 30 DAY ) >= {start}
      and DATE_ADD( x.djsj, INTERVAL 30 DAY ) <= {end}
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
group by r.region_name,r.org_code,xfxs)"""}