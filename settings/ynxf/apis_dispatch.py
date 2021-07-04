# apis分发-云南
"""
   云南大屏问题分类地图
   目前的模块：信访工作形势研判、信访态势统计分析
"""
URL_DISPATCH_MAP = {
    # 一. 信访工作形势研判
    # 1.1、信访工作形势研判_信访部门
    "信访工作形势研判_信访部门_区域年度受理量排行": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfjg_cy_shij_dwjc&name=shij_02&value=dwjc&order=-dwjc&full=true&year=2020",
    "信访工作形势研判_信访部门_办理方式": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfjg_cy_shej_blfs_bmjc&name=blfs&value=bmjc&transformer=@groupby&full=true&year=2020",
    "信访工作形势研判_信访部门_信访形式": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfjg_cy_shej_xfxs_bmjc_zb&name=xfxs&value=bmjc&transformer=@groupby&full=true&year=2020",
    "信访工作形势研判_信访部门_投诉问题分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfjg_cy_shej_yjnr_bmjc_zb&name=yjnr&value=bmjc&transformer=@groupby&full=true&year=2020",
    "信访工作形势研判_信访部门_受理量走势_年度": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfjg_cy_shej_blfs_bmjc&name=year&value=bmjc&transformer=@groupby",
    "信访工作形势研判_信访部门_受理量走势_月度": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfjg_cm_shej_bmsljc&name=month&value=bmsljc&transformer=@groupby",
    "信访工作形势研判_信访部门_信访评价_年度": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfjg_cy_shej_bmjssllv&value=bmjssllv&name=year&stack=year&extra_index=table@to:xf_xfjg_cy_shej_bmcplv;value@to:bmcplv,table@to:xf_xfjg_cy_shej_bmmylv;value@to:bmmylv&main_name=及时受理率,参评率,满意率",
    "信访工作形势研判_信访部门_信访评价_月度": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfjg_cm_shej_bmjssllv&value=bmjssllv&name=month&stack=month&extra_index=table@to:xf_xfjg_cm_shej_bmcplv;value@to:bmcplv,table@to:xf_xfjg_cm_shej_bmmylv;value@to:bmmylv&main_name=及时受理率,参评率,满意率",
    # 1.2、信访工作形势研判_责任单位
    "信访工作形势研判_责任单位_区域年度受理排行": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfjg_cy_shij_dwjc&name=shij_02&value=dwjc&order=-dwjc&full=true&year=2020",
    "信访工作形势研判_责任单位_办理方式": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfjg_cy_shej_blfs_dwjc&name=blfs&value=dwjc&transformer=@groupby&full=true&year=2020",
    "信访工作形势研判_责任单位_信访来源": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfjg_cy_shej_xfly_dwjc&name=xfly&value=dwjc&transformer=@groupby&full=true&year=2020",
    "信访工作形势研判_责任单位_投诉问题分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfjg_cy_shej_yjnr_dwjc_zb&name=yjnr&value=dwjc&transformer=@groupby&full=true&year=2020",
    "信访工作形势研判_责任单位_受理量走势_年度": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfjg_cy_shej_dwbljc&name=year&value=dwbljc&transformer=@groupby",
    "信访工作形势研判_责任单位_受理量走势_月度": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfjg_cm_shej_dwbljc&name=month&value=dwbljc&transformer=@groupby",
    "信访工作形势研判_责任单位_信访评价_年度": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfjg_cy_shej_dwjssllv&value=dwjssllv&name=year&stack=year&extra_index=table@to:xf_xfjg_cy_shej_dwcplv;value@to:dwcplv,table@to:xf_xfjg_cy_shej_dwmylv;value@to:dwmylv&main_name=及时受理率,参评率,满意率",
    "信访工作形势研判_责任单位_信访评价_月度": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfjg_cm_shej_dwjssllv&value=dwjssllv&name=month&stack=month&extra_index=table@to:xf_xfjg_cm_shej_dwcplv;value@to:dwcplv,table@to:xf_xfjg_cm_shej_dwmylv;value@to:dwmylv&main_name=及时受理率,参评率,满意率",

    # 二. 信访态势统计分析
    # 1.总量分析
    "信访态势统计分析_总量分析_区域年度信访量排行?": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shij_xfjc&name=shij_02&value=xfjc&stack=shij_02&year=2020&order=-xfjc&full=true&extra_index=transformer@to:@tb;order@drop;month@to:now&main_name=信访件次,同比",
    "信访态势统计分析_总量分析_全省信访量": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shej_xfjc&value=xfjc&shej_02=1&main_name=%E5%85%A8%E7%9C%81%E4%BF%A1%E8%AE%BF%E9%87%8F&full=true&year=2020",
    "信访态势统计分析_总量分析_各市信访量?": "http://39.107.240.28:3391/api/xf/?table=xf_xfj_cy_shij_xfjc&name=shij_02&value=xfjc&stack=shij_02&year=2020&extra_index=table@to:&full=true",
    "信访态势统计分析_总量分析_信访量月度走势": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cm_xfjc&name=month&value=xfjc&stack=month&extra_index=year@math:-1&main_name=今年,去年&year=2020",
    "信访态势统计分析_总量分析_年度三率指数": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfjg_cy_bmjssllv&value=bmjssllv&full=true&extra_index=table@to:xf_xfjg_cy_bmcplv;value@to:bmcplv,table@to:xf_xfjg_cy_bmmylv;value@to:bmmylv&main_name=部门受理率,部门参评率,满意率&year=2020",
    # 2.内容分类
    # a.地域分布
    "信访态势统计分析_内容分类_地域分布_一级内容分类信访量": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shej_yjnr_xfjc&name=shej_02&value=xfjc&transformer=@groupby&full=true&day=[2020-10-01,2020-10-20]",
    "信访态势统计分析_内容分类_地域分布_三类指数": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shej_yjnr_xfjc&name=yjnr&value=xfjc&stack=yjnr&transformer=@groupby&extra_index=transformer@to:@zb,table@to:xf_xfj_cd_shej_yjnr_xfrc;value@to:xfrc,transformer@to:@zb&main_name=信访件次,件次占比,信访人次,人次占比&day=[2019-01-01,2020-12-10]&full=true",
    "信访态势统计分析_内容分类_地域分布_饼图": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shej_yjnr_xfjc&name=yjnr&value=xfjc&stack=yjnr&transformer=@groupby&full=true&day=[2019-01-01,2020-12-10]",
    "信访态势统计分析_内容分类_地域分布_信访量分布?": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shij_yjnr_xfjc&name=shij_02&value=xfjc&stack=shij_02&transformer=@groupby&extra_index=table@to:xf_xfj_cd_shij_yjnr_xfrc;value@to:xfrc&main_name=件次,人次,&day=[2019-01-01,2020-12-10]&full=true&yjnr=卫生计生",
    # b.问题分类
    "信访态势统计分析_内容分类_问题分类_二级内容分类信访量?": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shej_ejnr_xfjc&name=shej_02&value=xfjc&stack=shej_02&transformer=@groupby&year=2020&order=-xfjc&extra_index=transformer@to:@tb;order@drop;month@to:now&main_name=件次,同比&full=true",
    "信访态势统计分析_内容分类_问题分类_各级内容分类占比分布": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shej_yjnr_ejnr_sjnr_xfjc&name=yjnr,ejnr,sjnr&order=desc&limit=4&full=none&day=[2020-01-01,2020-12-30]",
    # 3.信访形式
    # a.来信
    "信访态势统计分析_信访形式_来信_区域来信信访量排行(来信)": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shij_xfxs_xfjc&name=shij_02&value=xfjc&xfxs=来信&day=[2019-01-01,2020-12-10]&order=-xfjc&full=true",
    "信访态势统计分析_信访形式_来信_来信信访量信访初件重件联名件分布_全省来信信访量": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shej_xfxs_xfjc&value=xfjc&xfxs=来信&day=[2019-01-01,2020-12-10]&full=true",
    "信访态势统计分析_信访形式_来信_来信信访量信访初件重件联名件分布_初件重件联名件数量和比例": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_xfxs_cfxfbz_xfjc&name=xfxs&value=xfjc&stack=xfxs&transformer=@groupby&extra_index=transformer@to:@zb,table@to:xf_xfj_cd_xfxs_cfxfbz_xfrc;value@to:xfrc,transformer@to:@zb&main_name=信访件次,件次占比,信访人次,人次占比&day=[2019-01-01,2020-12-10]&full=true",
    "信访态势统计分析_信访形式_来信_来信信访量信访初件重件联名件分布_联名件非联名件圆环图": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_xfxs_lmj_xfjc&name=lmj&value=xfjc&stack=lmj&full=true&transformer=@groupby&extra_index=transformer@to:@zb&main_name=件次,占比&full=true&day=[2019-01-01,2020-12-10]&xfxs=来信",
    "信访态势统计分析_信访形式_来信_来信信访量信访初件重件联名件分布_初件重件圆环图": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_xfxs_cfxfbz_xfjc&name=cfxfbz&value=xfjc&stack=cfxfbz&full=true&transformer=@groupby&extra_index=transformer@to:@zb&main_name=件次,占比&full=true&day=[2019-01-01,2020-12-10]&xfxs=来信",
    # "信访态势统计分析_信访形式_来信_来信信访量信访初件重件联名件走势_年度?":"http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_xfxs_cfxfbz_xfjc&name=xfxs&value=xfjc&stack=xfxs&transformer=@groupby&extra_index=transformer@to:@zb,table@to:xf_xfj_cd_xfxs_cfxfbz_xfrc;value@to:xfrc,transformer@to:@zb&main_name=信访件次,件次占比,信访人次,人次占比&day=[2019-01-01,2020-12-10]&full=true",
    # "信访态势统计分析_信访形式_来信_来信信访量信访初件重件联名件走势_月度?":"http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_xfxs_cfxfbz_xfjc&name=xfxs&value=xfjc&stack=xfxs&transformer=@groupby&extra_index=transformer@to:@zb,table@to:xf_xfj_cd_xfxs_cfxfbz_xfrc;value@to:xfrc,transformer@to:@zb&main_name=信访件次,件次占比,信访人次,人次占比&day=[2019-01-01,2020-12-10]&full=true",
    # b.来访?
    # c.网信?
    # 4.信访目的
    "信访态势统计分析_信访目的_信访目的分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shej_xfmd_xfjc&name=xfmd&value=xfjc&&transformer=@groupby&year=2020&full=true",
    "信访态势统计分析_信访目的_信访目的分布趋势_年度": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shej_xfmd_xfjc&name=year&value=xfjc&stack=year&year=[now-5,now]&xfmd=求决&extra_index=xfmd@to:意见建议,xfmd@to:揭发控告,xfmd@to:申诉,xfmd@to:其他&main_name=求决,意见建议,揭发控告,申诉,其他&full=true",
    "信访态势统计分析_信访目的_信访目的分布趋势_月度": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cm_shej_xfmd_xfjc&name=month&value=xfjc&stack=month&xfmd=求决&extra_index=xfmd@to:意见建议,xfmd@to:揭发控告,xfmd@to:申诉,xfmd@to:其他&main_name=求决,意见建议,揭发控告,申诉,其他&full=true",
    "信访态势统计分析_信访目的_信访量四级登记机构-信访目的分布_全国": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shej_djjg_xfmd_xfjc&name=xfmd&value=xfjc&&transformer=@groupby&year=2020&djjg=全国&full=true",
    "信访态势统计分析_信访目的_信访量四级登记机构-信访目的分布_省级": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shej_djjg_xfmd_xfjc&name=xfmd&value=xfjc&&transformer=@groupby&year=2020&djjg=省级&full=true",
    "信访态势统计分析_信访目的_信访量四级登记机构-信访目的分布_市级": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shej_djjg_xfmd_xfjc&name=xfmd&value=xfjc&&transformer=@groupby&year=2020&djjg=市级&full=true",
    "信访态势统计分析_信访目的_信访量四级登记机构-信访目的分布_县级": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shej_djjg_xfmd_xfjc&name=xfmd&value=xfjc&&transformer=@groupby&year=2020&djjg=县级&full=true",
    # 2.5、信访态势统计分析_初件重件
    "信访态势统计分析_初件重件_信访量初件重件分布_总数": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_cfxfbz_xfjc&value=xfjc&year=2020",
    "信访态势统计分析_初件重件_信访量初件重件分布_件次/人次占比": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_cfxfbz_xfjc&name=cfxfbz&stack=cfxfbz&value=xfjc&transformer=@groupby&extra_index=transformer@to:@zb,value@to:xfrc;table@to:xf_xfj_cy_cfxfbz_xfrc;transformer@to:@groupby,transformer@to:@zb&main_name=信访件次,件次占比,信访人次,人次占比&full=true&year=2020",
    "信访工作形势研判_初件重件_初件_信访量地区分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shij_cfxfbz_xfjc&name=shij_02&value=xfjc&transformer=@groupby&full=true&year=2020&cfxfbz=初件",
    "信访工作形势研判_初件重件_初件_ 信访量信访次数分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shij_xfcsrange_cfxfbz_xfjc&name=xfcsrange&value=xfjc&transformer=@groupby&full=true&year=2020&cfxfbz=初件",
    "信访工作形势研判_初件重件_初件_地区信访人群年龄分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shij_nlrange_cfxfbz_xfrc&name=nlrange&value=xfrc&transformer=@groupby&full=true&year=2020&cfxfbz=初件&shij_02=昆明市",
    "信访工作形势研判_初件重件_初件_地区信访量信访目的分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shij_xfmd_cfxfbz_xfjc&name=xfmd&value=xfjc&transformer=@groupby&full=true&year=2020&cfxfbz=初件&shij_02=昆明市",
    "信访工作形势研判_初件重件_初件_地区信访量投诉问题分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shij_yjnr_cfxfbz_xfjc&name=yjnr&value=xfjc&transformer=@groupby&full=true&year=2020&cfxfbz=初件&shij_02=昆明市",
    "信访工作形势研判_初件重件_初件_地区信访量信访次数分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shij_xfcsrange_cfxfbz_xfjc&name=xfcsrange&value=xfjc&transformer=@groupby&full=true&year=2020&cfxfbz=初件&shij_02=昆明市",
    "信访工作形势研判_初件重件_重件_信访量地区分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shij_cfxfbz_xfjc&name=shij_02&value=xfjc&transformer=@groupby&full=true&year=2020&cfxfbz=重件",
    "信访工作形势研判_初件重件_重件_ 信访量信访次数分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shij_xfcsrange_cfxfbz_xfjc&name=xfcsrange&value=xfjc&transformer=@groupby&full=true&year=2020&cfxfbz=重件",
    "信访工作形势研判_初件重件_重件_地区信访人群年龄分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shij_nlrange_cfxfbz_xfrc&name=nlrange&value=xfrc&transformer=@groupby&full=true&year=2020&cfxfbz=重件&shij_02=昆明市",
    "信访工作形势研判_初件重件_重件_地区信访量信访目的分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shij_xfmd_cfxfbz_xfjc&name=xfmd&value=xfjc&transformer=@groupby&full=true&year=2020&cfxfbz=重件&shij_02=昆明市",
    "信访工作形势研判_初件重件_重件_地区信访量投诉问题分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shij_yjnr_cfxfbz_xfjc&name=yjnr&value=xfjc&transformer=@groupby&full=true&year=2020&cfxfbz=重件&shij_02=昆明市",
    "信访工作形势研判_初件重件_重件_地区信访量信访次数分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shij_xfcsrange_cfxfbz_xfjc&name=xfcsrange&value=xfjc&transformer=@groupby&full=true&year=2020&cfxfbz=重件&shij_02=昆明市",

    # 三. 热点模型分析
    # 数据反查
    "热点模型分析_进京访_重复访次数分布_列表": "http://127.0.0.1:3389/api/xf/?gd_id=yn_rdmxfx_datalist&query=1次&day=[2020-01-01,2020-12-31]&query_level=jjf",
    "热点模型分析_进京访_人数规模分布_列表": "http://127.0.0.1:3389/api/xf/?gd_id=yn_rdmxfx_datalist&query=1次&day=[2020-01-01,2020-12-31]&query_level=jjf",
    "热点模型分析_到省访_重复访次数分布_列表": "http://127.0.0.1:3389/api/xf/?gd_id=yn_rdmxfx_datalist&query=1次&day=[2020-01-01,2020-12-31]&query_level=fsf",
    "热点模型分析_到省访_人数规模分布_列表": "http://127.0.0.1:3389/api/xf/?gd_id=yn_rdmxfx_datalist&query=1次&day=[2020-01-01,2020-12-31]&query_level=fsf",
    # 1.进京访
    "热点模型分析_进京访_区划排名": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shij_xfxs_jjf_xfjc&name=shij_02&value=xfjc&full=true&day=[2019-01-01,2020-12-10]",
    "热点模型分析_进京访_进京访信访量人数规模分布走势": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cm_shej_jtf_jjf_xfjc&name=month&value=xfjc&jjf=个访&stack=month&full=true&transformer=@groupby&extra_index=jjf@to:集体访&main_name=个访,集体访&year=2020",
    "热点模型分析_进京访_重复访次数分布": "127.0.0.1:3389/api/xf/?gd_id=yn_rdmxfx_cfcspie&query_level=jjf&day=[2019-01-01,2020-01-01]",
    "热点模型分析_进京访_人数规模分布": "127.0.0.1:3389/api/xf/?gd_id=yn_rdmxfx_rspie&query_level=jjf&day=[2019-01-01,2020-01-01]",
    "热点模型分析_进京访_信访群体年龄分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shej_nlrange_xfxs_jjf_xfrc&name=nlrange&value=xfrc&full=true&day=[2019-01-01,2020-12-10]",
    "热点模型分析_进京访_信访诉求_信访问题分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shej_xfmd_xfxs_jjf_xfjc&name=xfmd&value=xfjc&full=true&day=[2019-01-01,2020-12-10]",
    "热点模型分析_进京访_信访诉求_投诉问题分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shej_yjnr_xfxs_jjf_xfjc&name=yjnr&value=xfjc&full=true&day=[2019-01-01,2020-12-10]",
    # 2.到省访
    "热点模型分析_到省访_区划排名": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shij_xfxs_fsf_xfjc&name=shij_02&value=xfjc&full=true&day=[2019-01-01,2020-12-10]",
    "热点模型分析_到省访_进京访信访量人数规模分布走势": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cm_shej_jtf_fsf_xfjc&name=month&value=xfjc&fsf=个访&stack=month&full=true&transformer=@groupby&extra_index=fsf@to:集体访&main_name=个访,集体访&year=2020",
    "热点模型分析_到省访_重复访次数分布": "127.0.0.1:3389/api/xf/?gd_id=yn_rdmxfx_cfcspie&query_level=fsf&day=[2019-01-01,2020-01-01]",
    "热点模型分析_到省访_人数规模分布": "127.0.0.1:3389/api/xf/?gd_id=yn_rdmxfx_rspie&query_level=fsf&day=[2019-01-01,2020-01-01]",
    "热点模型分析_到省访_信访群体年龄分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shej_nlrange_xfxs_fsf_xfrc&name=nlrange&value=xfrc&full=true&day=[2019-01-01,2020-12-10]",
    "热点模型分析_到省访_信访诉求_信访问题分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shej_xfmd_xfxs_fsf_xfjc&name=xfmd&value=xfjc&full=true&day=[2019-01-01,2020-12-10]",
    "热点模型分析_到省访_信访诉求_投诉问题分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shej_yjnr_xfxs_fsf_xfjc&name=yjnr&value=xfjc&full=true&day=[2019-01-01,2020-12-10]",
    # 3.集体访
    "热点模型分析_集体访_区划排名": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shij_xfxs_jtf_xfjc&name=shij_02&value=xfjc&full=true&day=[2019-01-01,2020-12-10]",
    "热点模型分析_集体访_集体访信访量走势": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cm_shej_jtf_xfjc&name=month&value=xfjc&year=2020",
    "热点模型分析_集体访_人数规模分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shej_rsrange_xfxs_jtf_xfjc&name=rsrange&value=xfjc&full=true&day=[2019-01-01,2020-12-10]",
    "热点模型分析_集体访_信访群体年龄分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shej_nlrange_xfxs_jtf_xfrc&name=nlrange&value=xfrc&full=true&day=[2019-01-01,2020-12-10]",
    "热点模型分析_集体访_信访诉求_信访问题分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shej_xfmd_xfxs_jtf_xfjc&name=xfmd&value=xfjc&full=true&day=[2019-01-01,2020-12-10]",
    "热点模型分析_集体访_信访诉求_投诉问题分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shej_yjnr_xfxs_jtf_xfjc&name=yjnr&value=xfjc&full=true&day=[2019-01-01,2020-12-10]",
    # 4.其他
    "热点模型分析_其它_进京访_登记类型分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shej_jjxfdd_djlx_xfjc&name=djlx&jjxfdd=天安门&year=2020",
    "热点模型分析_其它_进京访_倒流件次": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shej_jjxfdd_dlbz_xfjc&name=dlbz&jjxfdd=天安门&year=2020",
    "热点模型分析_其它_进京访_信访量地区分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shij_jjxfdd_xfjc&name=shij_02&jjxfdd=天安门&year=2020",
    "热点模型分析_其它_到省访_总数": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shej_fsxfdd_djlx_xfjc&year=2020",
    "热点模型分析_其它_到省访_登记类型分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shej_fsxfdd_djlx_xfjc&name=djlx&fsxfdd=天安门&year=2020",
    "热点模型分析_其它_到省访_倒流件次": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shej_fsxfdd_dlbz_xfjc&name=dlbz&fsxfdd=天安门&year=2020",
    "热点模型分析_其它_到省访_信访量地区分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cy_shij_fsxfdd_xfjc&name=shij_02&fsxfdd=天安门&year=2020",

    # 四. 政策关联分析
    # 1.涉件分析(缺)
    # 2.政策统计
    "政策关联分析_政策统计_一级内容分类政策分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfzc_cy_shej_yjnr_zcsl&name=yjnr&value=zcsl&stack=yjnr&transformer=@groupby&extra_index=table@to:xf_xfj_cy_shej_yjnr_xfjc;value@to:xfjc&main_name=政策数量,信访量件次&year=2020",
    "政策关联分析_政策统计_信访量月度走势": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfzc_cm_shej_yjnr_xfjc&name=month&value=xfjc&year=2020&full=true",
    "政策关联分析_政策统计_政策分类分布": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfzc_cy_shej_yjnr_zcfl_zcsl&name=zcfl&value=zcsl&year=2020",

    # 重点人员
    "信访人分析_重点人员_(.*)": "http://www.fuyaofy.com:3391/api/xf/?gd_id=yn_xfrfx_xfrlb&query={gd_id3}&LIKE-xm='%%'",

    # "信访人分析_重点人员_全部": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfr_cy_zjhm_xm_xfjc&name=xm&value=zjhm&direct_order=-xfjc&direct_limit=100&full=none",
    # "信访人分析_重点人员_扬言": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfr_cy_zjhm_xm_yy_xfjc&name=xm&value=zjhm&direct_order=-xfjc&direct_limit=100&full=none",
    # "信访人分析_重点人员_专项": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfr_cy_zjhm_xm_zxbz_xfjc&name=xm&value=zjhm&direct_order=-xfjc&direct_limit=100&full=none",

    "矛盾分析预警预判_预警形式_地图": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shij_xfjc&name=shij_02&transformer=yjzt&day=[now-7,now]",
    "矛盾分析预警预判_预警形式_预警状态条目-信访量": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shij_xfjc&extra_index=transformer@to:tb,transformer@to:hb,transformer@to:yjzt&day=[now-7,now]&main_name=信访件次,件次同比,件次环比,指数状态&shij_02=昆明市",
    "矛盾分析预警预判_预警形式_预警状态条目-进京访": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shij_jjf_xfjc&extra_index=transformer@to:tb,transformer@to:hb,transformer@to:yjzt&jjf=进京访&day=[now-7,now]&main_name=信访件次,件次同比,件次环比,指数状态&shij_02=昆明市",
    "矛盾分析预警预判_预警形式_预警状态条目-赴省访": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shij_fsf_xfjc&extra_index=transformer@to:tb,transformer@to:hb,transformer@to:yjzt&fsf=赴省访&day=[now-7,now]&main_name=信访件次,件次同比,件次环比,指数状态&shij_02=昆明市",
    "矛盾分析预警预判_预警形式_预警状态条目-集体访": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shij_jtf_xfjc&extra_index=transformer@to:tb,transformer@to:hb,transformer@to:yjzt&jtf=集体访&day=[now-7,now]&main_name=信访件次,件次同比,件次环比,指数状态&shij_02=昆明市",

    "矛盾分析预警预判_预警预测_预警地图$": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shij_xfjc&day=[now-200,now]&transformer=predict(7d+p=1+d=1+q=0)&Cqh=云南省&extra_index=transformer@to:yctb(7d),transformer@to:ychb(7d),transformer@to:ycyjzt&main_name=a,b,c,d&reindex=4&param_trans=qh_godown",
    "矛盾分析预警预判_预警预测_预警状态$": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shij_xfjc&day=[now-200,now]&transformer=predict(7d+p=1+d=1+q=0)&Cqh=云南省&extra_index=transformer@to:yctb(7d),transformer@to:ychb(7d),transformer@to:ycyjzt&main_name=未来一周,同比,环比,预警状态&reindex=4,1,2,3",
    "矛盾分析预警预判_预警预测_走势$": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfj_cd_shij_xfjc&name=day&stack=day&day=[now-50,now]&extra_index=transformer@to:predict(7d+p=1+d=1+q=0);day@to:[now-200,now]&main_name=真实,预测&Cqh=云南省&param_trans=qh2sheshixj",

    # 五. 行为分析预警
    # 前端传证件号码 zjhm
# xf_xfjg_cy_shij_bmjssllv
# xf_xfjg_cy_shij_bmcplv
# xf_xfjg_cy_shij_bmmylv
    "信访行为分析预警_行为转化预警_行为转化漏斗": "http://www.fuyaofy.com:3391/api/xf/?gd_id=yn_xwzhyj_xwzhld&year=2020&shij_02=昆明市",
    "信访行为分析预警_行为转化预警_年度三率": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfjg_cy_shij_bmjssllv&extra_index=table@to:xf_xfjg_cy_shij_bmcplv,table@to:xf_xfjg_cy_shij_bmmylv&main_name=部门及时受理率,部门参评率,部门满意率&shij_02=昆明市&year=2020",
    "信访行为分析预警_行为转化预警_重点人列表": "http://www.fuyaofy.com:3391/api/xf/?gd_id=yn_xwzhyj_zdxfrlb&year=2020&limit=10",

    "信访行为分析预警_行为轨迹预警_行为分析指数走势":"http://www.fuyaofy.com:3391/api/xf/?table=xf_xfr_cm_zjhm_xm_xfxwzs&name=month&zjhm=100000000&year=2020",
    # "信访行为分析预警_行为轨迹预警_行为统计": "http://www.fuyaofy.com:3391/api/xf/?table=xf_xfr_cd_zjhm_xm_xfxw&name=day&zjhm=100000000&year=2021&param_trans=year2day&full=none&black_list(year)",
    # "信访行为分析预警_行为轨迹预警_行为统计": {"data": [{"name": "2020-01-14", "value": "扬言"},{"name": "2020-09-01", "value": "扬言"},{"name": "2020-09-10", "value": "扬言"}]},
    "信访行为分析预警_行为轨迹预警_行为统计": "http://www.fuyaofy.com:3391/api/xf/?gd_id=yn_xwgjyj_xwsjz&zjhm=100000000",
    "信访行为分析预警_行为轨迹预警_重点人员摘要": "http://www.fuyaofy.com:3391/api/xf/?gd_id=yn_xwgjyj_zdryzy&year=2020&month=1&zjhm=100000000",
}
