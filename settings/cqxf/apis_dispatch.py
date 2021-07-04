# apis分发-重庆
URL_DISPATCH_MAP = {
    ################################ 日常统计分析 ################################
    # 日常统计分析-总量分析 year=2020
    # 前端动态参数 "参数=默认值": year=2020
    "日常统计分析_总量分析_区域信访量动态": "127.0.0.1:3389/api/xf/?table=xf_xfj_cy_xj_xfjc&name=xj_02&order=desc&year=2020",
    "日常统计分析_总量分析_全省信访量$": "127.0.0.1:3389/api/xf/?table=xf_xfj_cy_shij_xfjc&year=2020",
    "日常统计分析_总量分析_全省信访量-信访形式": "127.0.0.1:3389/api/xf/?table=xf_xfj_cy_xj_xfxs_xfjc&name=xfxs&year=2020",
    "日常统计分析_总量分析_地图": "127.0.0.1:3389/api/xf/?table=xf_xfj_cy_xj_xfjc&name=xj_02&stack=xj_02&extra_index=table@to:xf_xfj_cy_xj_xfxs_xfjc;stack@to:xfxs&main_name=总数,&year=2020",
    "日常统计分析_总量分析_信访量走势": "127.0.0.1:3389/api/xf/?table=xf_xfj_cm_shij_xfjc&name=month&stack=month&extra_index=year@math:-1&main_name=今年,去年&year=2020",
    "日常统计分析_总量分析_年度初重件占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cy_shij_cfxfbz_xfjc_zb&name=cfxfbz&year=2020",
    "日常统计分析_总量分析_年度信访形式": "127.0.0.1:3389/api/xf/?table=xf_xfj_cy_shij_xfxs_xfjc_zb&name=xfxs&year=2020",

    # 日常统计分析-信访形式-来信-总体 day=[2019-01-01,2020-02-02]&xfxs=来信
    # 前端动态参数 "参数=默认值": day=[2019-01-01,2020-02-02]
    "日常统计分析_信访形式_来信_总体_区域信访量动态": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_xfxs_xfjc&name=xj_02&order=desc&day=[2020-01-01,2020-10-10]&xfxs=来信",
    "日常统计分析_信访形式_来信_总体_初重件列表": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_xfxs_cfxfbz_xfjc_zb&name=cfxfbz&stack=cfxfbz&extra_index=transformer@to:@zb,table@to:xf_xfj_cd_shij_xfxs_cfxfbz_xfrc,table@to:xf_xfj_cd_shij_xfxs_cfxfbz_xfrc;transformer@to:@zb&main_name=信访件次,件次占比,信访人次,人次占比&day=[2019-01-01,2020-02-02]&xfxs=来信",
    "日常统计分析_信访形式_来信_总体_初重件占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_xfxs_cfxfbz_xfjc_zb&name=cfxfbz&xfxs=来信",
    "日常统计分析_信访形式_来信_总体_件次": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_xfxs_cfxfbz_xfjc_zb&xfxs=来信",
    "日常统计分析_信访形式_来信_总体_联名件圆环": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_xfxs_lmj_xfjc_zb&name=lmj&stack=lmj&extra_index=transformer@to:@zb&main_name=value,precent&day=[2019-01-01,2020-02-02]&xfxs=来信",
    "日常统计分析_信访形式_来信_总体_登记机构列表": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_xfxs_djjg_xfjc&name=djjg&stack=djjg&extra_index=transformer@to:@zb,table@to:xf_xfj_cd_shij_xfxs_djjg_xfrc_zb,table@to:xf_xfj_cd_shij_xfxs_djjg_xfrc_zb;transformer@to:@zb&main_name=信访件次,件次占比,信访人次,人次占比&day=[2019-01-01,2020-02-02]&xfxs=来信",
    "日常统计分析_信访形式_来信_总体_登记机构占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_xfxs_djjg_xfjc&name=djjg&day=[2019-01-01,2020-02-02]&xfxs=来信",
    "日常统计分析_信访形式_来信_总体_初重件走势": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_xfxs_cfxfbz_xfjc_zb&name=day&stack=cfxfbz&day=[2019-01-01,2020-02-02]&xfxs=来信",

    # 日常统计分析-信访形式-来信-受信人-(左侧列表) day=[2019-01-01,2020-02-02]&xfxs=来信 【左侧列表需要一个排序字段】
    # 前端动态参数 "参数=默认值": day=[2019-01-01,2020-02-02]
    "日常统计分析_信访形式_来信_受信人_受信人名单": "127.0.0.1:3389/api/xf/?gd_id=cq_xfxs_sxrmd&day=[2019-01-01,2020-02-02]",  # 暂时解决
    # 日常统计分析-信访形式-来信-受信人-(非列表) day=[2019-01-01,2020-02-02]&sxr=习近平  【不用传xfxs=来信，有受信人就是来信】
    # 前端动态参数 "参数=默认值": day=[2019-01-01,2020-02-02], sxr=习近平
    "日常统计分析_信访形式_来信_受信人_初重件走势": "127.0.0.1:3389/api/xf/?table=xf_sxr_cd_shij_cfxfbz_xfjc_zb&name=day&stack=cfxfbz&day=[2019-01-01,2020-02-02]&sxr=习近平",
    "日常统计分析_信访形式_来信_受信人_初重件占比": "127.0.0.1:3389/api/xf/?table=xf_sxr_cd_shij_cfxfbz_xfjc_zb&name=cfxfbz&day=[2019-01-01,2020-02-02]&sxr=习近平",
    "日常统计分析_信访形式_来信_受信人_联名件圆环": "127.0.0.1:3389/api/xf/?table=xf_sxr_cd_shij_lmj_xfjc_zb&name=lmj&stack=lmj&extra_index=transformer@to:@zb&main_name=value,precent&day=[2019-01-01,2020-02-02]&sxr=习近平",
    "日常统计分析_信访形式_来信_受信人_地区分布": "127.0.0.1:3389/api/xf/?table=xf_sxr_cd_xj_xfjc_zb&name=xj_02&day=[2019-01-01,2020-02-02]&sxr=习近平",
    "日常统计分析_信访形式_来信_受信人_年龄统计": "127.0.0.1:3389/api/xf/?table=xf_sxr_cd_shij_nlrange_xfrc&name=nlrange&day=[2019-01-01,2020-02-02]&sxr=习近平",
    "日常统计分析_信访形式_来信_受信人_信访目的占比": "127.0.0.1:3389/api/xf/?table=xf_sxr_cd_shij_xfmd_xfjc_zb&name=xfmd&day=[2019-01-01,2020-02-02]&sxr=习近平",
    "日常统计分析_信访形式_来信_受信人_投诉问题占比": "127.0.0.1:3389/api/xf/?table=xf_sxr_cd_shij_yjnr_xfjc_zb&name=yjnr&day=[2019-01-01,2020-02-02]&sxr=习近平",

    # 日常统计分析-信访形式-来访-总体 day=[2019-01-01,2020-02-02]&xfxs=来访
    # 前端动态参数 "参数=默认值": day=[2019-01-01,2020-02-02]
    "日常统计分析_信访形式_来访_总体_区域信访量动态": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_xfxs_xfjc&name=xj_02&order=desc&day=[2020-01-01,2020-10-10]&xfxs=来访",
    "日常统计分析_信访形式_来访_总体_件次": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_xfxs_cfxfbz_xfjc_zb&xfxs=来访",
    "日常统计分析_信访形式_来访_总体_初重件列表": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_xfxs_cfxfbz_xfjc_zb&name=cfxfbz&stack=cfxfbz&extra_index=transformer@to:@zb,table@to:xf_xfj_cd_shij_xfxs_cfxfbz_xfrc,table@to:xf_xfj_cd_shij_xfxs_cfxfbz_xfrc;transformer@to:@zb&main_name=信访件次,件次占比,信访人次,人次占比&day=[2019-01-01,2020-02-02]&xfxs=来访",
    "日常统计分析_信访形式_来访_总体_登记机构占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_xfxs_djjg_xfjc&name=djjg&day=[2019-01-01,2020-02-02]&xfxs=来访",
    "日常统计分析_信访形式_来访_总体_登记机构走势": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_xfxs_djjg_xfjc&name=day&stack=djjg&day=[2019-01-01,2020-02-02]&xfxs=来访",

    # 日常统计分析-信访形式-来访-进京访 day=[2019-01-01,2020-02-02]&jjf=进京访 【进京访的表只有一张带xfxs，其余都不带默认 进京访只能是来访】
    # 前端动态参数 "参数=默认值": day=[2019-01-01,2020-02-02]
    "日常统计分析_信访形式_来访_进京访_区划分布": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_xfxs_jjf_xfjc_zb&name=xj_02&day=[2019-01-01,2020-02-02]&jjf=进京访",
    "日常统计分析_信访形式_来访_进京访_人数规模走势": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_jjf_jtf_xfjc_zb&name=day&stack=jtf&day=[2019-01-01,2020-02-02]&jjf=进京访",
    "日常统计分析_信访形式_来访_进京访_重复访次数占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_jjf_cfcsrange_xfjc_zb&name=cfcsrange&day=[2019-01-01,2020-02-02]&jjf=进京访",
    "日常统计分析_信访形式_来访_进京访_人数规模占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_jjf_rsrange_xfjc_zb&name=rsrange&day=[2019-01-01,2020-02-02]&jjf=进京访",
    "日常统计分析_信访形式_来访_进京访_年龄统计": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_jjf_nlrange_xfrc&name=nlrange&day=[2019-01-01,2020-02-02]&jjf=进京访",
    "日常统计分析_信访形式_来访_进京访_信访目的占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_jjf_xfmd_xfjc_zb&name=xfmd&day=[2019-01-01,2020-02-02]&jjf=进京访",
    "日常统计分析_信访形式_来访_进京访_投诉问题占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_jjf_yjnr_xfjc_zb&name=yjnr&day=[2019-01-01,2020-02-02]&jjf=进京访",

    "日常统计分析_信访形式_来访_越级访_区划分布": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_yjf_xfjc_zb&name=xj_02&day=[2019-01-01,2020-02-02]&yjf=越级访",
    "日常统计分析_信访形式_来访_越级访_人数规模走势": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_yjf_jtf_xfjc_zb&name=day&stack=jtf&day=[2019-01-01,2020-02-02]&yjf=越级访",
    "日常统计分析_信访形式_来访_越级访_重复访次数占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_yjf_cfcsrange_xfjc_zb&name=cfcsrange&day=[2019-01-01,2020-02-02]&yjf=越级访",
    "日常统计分析_信访形式_来访_越级访_人数规模占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_yjf_rsrange_xfjc_zb&name=rsrange&day=[2019-01-01,2020-02-02]&yjf=越级访",
    "日常统计分析_信访形式_来访_越级访_年龄统计": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_yjf_nlrange_xfrc&name=nlrange&day=[2019-01-01,2020-02-02]&yjf=越级访",
    "日常统计分析_信访形式_来访_越级访_信访目的占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_yjf_xfmd_xfjc_zb&name=xfmd&day=[2019-01-01,2020-02-02]&yjf=越级访",
    "日常统计分析_信访形式_来访_越级访_投诉问题占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_yjf_yjnr_xfjc_zb&name=yjnr&day=[2019-01-01,2020-02-02]&yjf=越级访",

    "日常统计分析_信访形式_来访_重复访_区划分布": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_cff_xfjc_zb&name=xj_02&day=[2019-01-01,2020-02-02]&cff=重复访",
    "日常统计分析_信访形式_来访_重复访_人数规模走势": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_cff_jtf_xfjc_zb&name=day&stack=jtf&day=[2019-01-01,2020-02-02]&cff=重复访",
    "日常统计分析_信访形式_来访_重复访_重复访次数占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_cff_cfcsrange_xfjc_zb&name=cfcsrange&day=[2019-01-01,2020-02-02]&cff=重复访",
    "日常统计分析_信访形式_来访_重复访_人数规模占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_cff_rsrange_xfjc_zb&name=rsrange&day=[2019-01-01,2020-02-02]&cff=重复访",
    "日常统计分析_信访形式_来访_重复访_年龄统计": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_cff_nlrange_xfrc&name=nlrange&day=[2019-01-01,2020-02-02]&cff=重复访",
    "日常统计分析_信访形式_来访_重复访_信访目的占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_cff_xfmd_xfjc_zb&name=xfmd&day=[2019-01-01,2020-02-02]&cff=重复访",
    "日常统计分析_信访形式_来访_重复访_投诉问题占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_cff_yjnr_xfjc_zb&name=yjnr&day=[2019-01-01,2020-02-02]&cff=重复访",

    "日常统计分析_信访形式_来访_集体访_区划分布": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_jtf_xfjc_zb&name=xj_02&day=[2019-01-01,2020-02-02]&jtf=集体访",
    "日常统计分析_信访形式_来访_集体访_人数规模走势": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_jtf_jtf_xfjc_zb&name=day&stack=jtf&day=[2019-01-01,2020-02-02]&jtf=集体访",
    "日常统计分析_信访形式_来访_集体访_重复访次数占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_jtf_cfcsrange_xfjc_zb&name=cfcsrange&day=[2019-01-01,2020-02-02]&jtf=集体访",
    "日常统计分析_信访形式_来访_集体访_人数规模占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_jtf_rsrange_xfjc_zb&name=rsrange&day=[2019-01-01,2020-02-02]&jtf=集体访",
    "日常统计分析_信访形式_来访_集体访_年龄统计": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_jtf_nlrange_xfrc&name=nlrange&day=[2019-01-01,2020-02-02]&jtf=集体访",
    "日常统计分析_信访形式_来访_集体访_信访目的占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_jtf_xfmd_xfjc_zb&name=xfmd&day=[2019-01-01,2020-02-02]&jtf=集体访",
    "日常统计分析_信访形式_来访_集体访_投诉问题占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_jtf_yjnr_xfjc_zb&name=yjnr&day=[2019-01-01,2020-02-02]&jtf=集体访",

    # 日常统计分析-信访形式-网信 day=[2019-01-01,2020-02-02]&xfxs=网信
    # 前端动态参数 "参数=默认值": day=[2019-01-01,2020-02-02]
    "日常统计分析_信访形式_网信_区域信访量动态": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_xfxs_xfjc&name=xj_02&order=desc&day=[2020-01-01,2020-10-10]&xfxs=网信",
    "日常统计分析_信访形式_网信_初重件列表": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_xfxs_cfxfbz_xfjc_zb&name=cfxfbz&stack=cfxfbz&extra_index=transformer@to:@zb,table@to:xf_xfj_cd_shij_xfxs_cfxfbz_xfrc,table@to:xf_xfj_cd_shij_xfxs_cfxfbz_xfrc;transformer@to:@zb&main_name=信访件次,件次占比,信访人次,人次占比&day=[2019-01-01,2020-02-02]&xfxs=网信",
    "日常统计分析_信访形式_网信_初重件占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_xfxs_cfxfbz_xfjc_zb&name=cfxfbz&xfxs=网信",
    "日常统计分析_信访形式_网信_件次": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_xfxs_cfxfbz_xfjc_zb&xfxs=网信",
    "日常统计分析_信访形式_网信_联名件圆环": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_xfxs_lmj_xfjc_zb&name=lmj&stack=lmj&extra_index=transformer@to:@zb&main_name=value,precent&day=[2019-01-01,2020-02-02]&xfxs=网信",
    "日常统计分析_信访形式_网信_登记机构列表": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_xfxs_djjg_xfjc&name=djjg&stack=djjg&extra_index=transformer@to:@zb,table@to:xf_xfj_cd_shij_xfxs_djjg_xfrc_zb,table@to:xf_xfj_cd_shij_xfxs_djjg_xfrc_zb;transformer@to:@zb&main_name=信访件次,件次占比,信访人次,人次占比&day=[2019-01-01,2020-02-02]&xfxs=网信",
    "日常统计分析_信访形式_网信_登记机构占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_xfxs_djjg_xfjc&name=djjg&day=[2019-01-01,2020-02-02]&xfxs=网信",
    "日常统计分析_信访形式_网信_登记机构走势": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_xfxs_djjg_xfjc&name=day&stack=djjg&day=[2019-01-01,2020-02-02]&xfxs=网信",

    # 日常统计分析-内容分类-(右侧旭日图) day=[2019-01-01,2020-02-02]
    # 前端动态参数 "参数=默认值": day=[2019-01-01,2020-02-02]
    "日常统计分析_内容分类_问题分类_内容分类旭日图": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_sjnr_xfjc_zb&name=yjnr,ejnr&limit=4&order=desc&day=[2019-01-01,2020-02-02]",
    # 日常统计分析-内容分类-(右侧非旭日图) day=[2019-01-01,2020-02-02]&ejnr=土地征收
    # 前端动态参数 "参数=默认值": day=[2019-01-01,2020-02-02], ejnr=土地征收
    "日常统计分析_内容分类_问题分类_件次": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_sjnr_xfjc_zb&day=[2019-01-01,2020-02-02]&ejnr=土地征收",
    "日常统计分析_内容分类_问题分类_内容分类件次": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_sjnr_xfjc_zb&name=sjnr&transformer=@zb&day=[2019-01-01,2020-02-02]&ejnr=土地征收",
    "日常统计分析_内容分类_问题分类_人次": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_sjnr_xfrc_zb&day=[2019-01-01,2020-02-02]&ejnr=土地征收",
    "日常统计分析_内容分类_问题分类_内容分类人次": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_sjnr_xfrc_zb&name=sjnr&transformer=@zb&day=[2019-01-01,2020-02-02]&ejnr=土地征收",
    "日常统计分析_内容分类_问题分类_内容分类走势": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_sjnr_xfjc_zb&name=day&stack=sjnr&day=[2019-01-01,2020-02-02]&ejnr=土地征收",

    # 日常统计分析-初件重件-(非地区筛选:上半部分) year=2020&cfxfbz={gd_id3}&xfxs={gd_id4}
    # 前端动态参数 "参数=默认值": year=2020
    "日常统计分析_初件重件_(初件|重件)_(drop|来信|来访|网信)_件次": "127.0.0.1:3389/api/xf/?table=xf_xfj_cy_shij_cfxfbz_xfxs_xfjc_zb&year=2020&cfxfbz={gd_id3}&xfxs={gd_id4}",
    "日常统计分析_初件重件_(初件|重件)_(drop|来信|来访|网信)_初重件列表": "127.0.0.1:3389/api/xf/?table=xf_xfj_cy_shij_cfxfbz_xfxs_xfjc_zb&name=cfxfbz&stack=cfxfbz&extra_index=transformer@to:@zb,table@to:xf_xfj_cy_shij_cfxfbz_xfxs_xfrc_zb,table@to:xf_xfj_cy_shij_cfxfbz_xfxs_xfrc_zb;transformer@to:@zb&main_name=信访件次,件次占比,信访人次,人次占比&year=2020&cfxfbz={gd_id3}&xfxs={gd_id4}",
    "日常统计分析_初件重件_(初件|重件)_(drop|来信|来访|网信)_登记机构占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cy_shij_cfxfbz_xfxs_djjg_xfjc_zb&name=djjg&year=2020&cfxfbz={gd_id3}&xfxs={gd_id4}",
    "日常统计分析_初件重件_(初件|重件)_(drop|来信|来访|网信)_地区分布": "127.0.0.1:3389/api/xf/?table=xf_xfj_cy_xj_cfxfbz_xfxs_xfjc_zb&name=xj_02&year=2020&cfxfbz={gd_id3}&xfxs={gd_id4}",
    # 日常统计分析-初件重件-(地区筛选:下半部分) year=2020&xj_02=南岸区
    # 前端动态参数 "参数=默认值": year=2020, xj_02=南岸区
    "日常统计分析_初件重件_(初件|重件)_(drop|来信|来访|网信)_年龄统计": "127.0.0.1:3389/api/xf/?table=xf_xfj_cy_xj_cfxfbz_xfxs_nlrange_xfrc&name=nlrange&year=2020&xj_02=南岸区",
    "日常统计分析_初件重件_(初件|重件)_(drop|来信|来访|网信)_信访目的占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cy_xj_cfxfbz_xfxs_xfmd_xfjc_zb&name=xfmd&year=2020&xj_02=南岸区",
    "日常统计分析_初件重件_(初件|重件)_(drop|来信|来访|网信)_投诉问题占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cy_xj_cfxfbz_xfxs_yjnr_xfjc_zb&name=yjnr&year=2020&xj_02=南岸区",

    ################################ 社会重点工作分析 ################################
    # 社会重点工作分析-(饼图筛选:左半部分) day=[2019-01-01,2020-02-02]
    # 前端动态参数 "参数=默认值": day=[2019-01-01,2020-02-02]
    "社会重点工作分析_重点工作信访量$": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_yjnr_xfjc_zb&day=[2019-01-01,2020-02-02]",
    "社会重点工作分析_重点工作信访量占比$": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_yjnr_xfjc_zb&name=yjnr&day=[2019-01-01,2020-02-02]",
    "社会重点工作分析_重点工作信访量走势$": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_yjnr_xfjc_zb&name=day&day=[2019-01-01,2020-02-02]&yjnr=房地产开发管理",
    # 社会重点工作分析-(饼图筛选:右半部分) day=[2019-01-01,2020-02-02]&yjnr=房地产开发管理
    # 前端动态参数 "参数=默认值": day=[2019-01-01,2020-02-02], yjnr=房地产开发管理
    "社会重点工作分析_信访量地图分布_全部": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_yjnr_xfjc_zb&name=xj_02&day=[2019-01-01,2020-02-02]&yjnr=房地产开发管理",
    "社会重点工作分析_信访量地图分布_(来信|来访|网信)": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_yjnr_xfxs_xfjc_zb&name=xj_02&day=[2019-01-01,2020-02-02]&yjnr=房地产开发管理&xfxs={gd_id3}",
    "社会重点工作分析_信访量地图分布_进京访": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_yjnr_jjf_xfjc_zb&name=xj_02&jjf=进京访&day=[2019-01-01,2020-02-02]&yjnr=房地产开发管理",

    ################################ 涉众信访态势研判 ################################
    # 涉众信访态势研判 day=[2019-01-01,2020-02-02]&jtf=集体访&xfxs={gd_id2}
    # 前端动态参数 "参数=默认值": day=[2019-01-01,2020-02-02]
    "涉众信访态势研判_(Pinvalid|来信|来访|网信)_区划分布": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_jtf_xfxs_xfjc&name=xj_02&day=[2019-01-01,2020-02-02]&jtf=集体访&xfxs={gd_id2}",
    "涉众信访态势研判_(Pinvalid|来信|来访|网信)_集体访走势": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_jtf_xfxs_xfjc&name=day&day=[2019-01-01,2020-02-02]&jtf=集体访&xfxs={gd_id2}",
    "涉众信访态势研判_(Pinvalid|来信|来访|网信)_人数规模占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_jtf_xfxs_rsrange_xfjc&name=rsrange&day=[2019-01-01,2020-02-02]&jtf=集体访&xfxs={gd_id2}",
    # "涉众信访态势研判_(Pinvalid|来信|来访|网信)_年龄统计": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_jtf_xfxs_nlrange_xfjc&name=nlrange&day=[2019-01-01,2020-02-02]&jtf=集体访&xfxs={gd_id2}",
    "涉众信访态势研判_(Pinvalid|来信|来访|网信)_年龄统计": {'code':200,'msg':'success','data':[{'name':'30岁以下','value':'123'},{'name':'31-40岁','value':'1120'},{'name':'41-50岁','value':'367'},{'name':'51-60岁','value':'227'},{'name':'60岁以上','value':'517'}]},
    "涉众信访态势研判_(Pinvalid|来信|来访|网信)_信访目的占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_jtf_xfxs_xfmd_xfjc&name=xfmd&day=[2019-01-01,2020-02-02]&jtf=集体访&xfxs={gd_id2}",
    "涉众信访态势研判_(Pinvalid|来信|来访|网信)_投诉问题占比": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_shij_jtf_xfxs_yjnr_xfjc&name=yjnr&day=[2019-01-01,2020-02-02]&jtf=集体访&xfxs={gd_id2}",

    ################################ 宏观态势运行预警预测 ################################
    # 宏观态势运行预警预测-信访指数预警[非预测] day=[now-7,now]
    # 前端动态参数 "参数=默认值": 无
    "宏观态势运行预警预测_信访指数预警_地图": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_xfjc&name=xj_02&transformer=yjzt&day=[now-7,now]",
    # 实现有误，需要取最高值
    "宏观态势运行预警预测_信访指数预警_预警状态条目-信访量": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_xfjc&extra_index=transformer@to:tb,transformer@to:hb,transformer@to:yjzt&main_name=信访件次,同比,环比,指数状态&day=[now-7,now]&Cqh=忠县",
    "宏观态势运行预警预测_信访指数预警_预警状态条目-进京访": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_xfxs_jjf_xfjc_zb&extra_index=transformer@to:tb,transformer@to:hb,transformer@to:yjzt&jjf=进京访&main_name=信访件次,同比,环比,指数状态&day=[now-7,now]&Cqh=忠县",
    "宏观态势运行预警预测_信访指数预警_预警状态条目-集体访": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_jtf_xfxs_xfjc&extra_index=transformer@to:tb,transformer@to:hb,transformer@to:yjzt&jtf=集体访&main_name=信访件次,同比,环比,指数状态&day=[now-7,now]&Cqh=忠县",
    "宏观态势运行预警预测_信访指数预警_预警状态条目-扬言件": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_jtf_xfxs_xfjc&extra_index=transformer@to:tb,transformer@to:hb,transformer@to:yjzt&jtf=集体访&main_name=信访件次,同比,环比,指数状态&day=[now-7,now]&Cqh=忠县",
    "宏观态势运行预警预测_信访指数预警_预警状态条目-进京越级访": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_jtf_xfxs_xfjc&extra_index=transformer@to:tb,transformer@to:hb,transformer@to:yjzt&jtf=集体访&main_name=信访件次,同比,环比,指数状态&day=[now-7,now]&Cqh=忠县",
    "宏观态势运行预警预测_信访指数预警_预警状态条目-到市越级访": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_jtf_xfxs_xfjc&extra_index=transformer@to:tb,transformer@to:hb,transformer@to:yjzt&jtf=集体访&main_name=信访件次,同比,环比,指数状态&day=[now-7,now]&Cqh=忠县",

    # 宏观态势运行预警预测-热点问题预警[非预测] day=[now-7,now]
    # 前端动态参数 "参数=默认值": 无
    "宏观态势运行预警预测_热点问题预警_地图": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_xfjc&name=xj_02&transformer=yjzt&day=[now-7,now]",
    # 实现有误，需要取最高值
    "宏观态势运行预警预测_热点问题预警_预警状态条目": "127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_yjnr_xfjc_zb&name=yjnr&stack=yjnr&extra_index=transformer@to:tb,transformer@to:hb,transformer@to:yjzt&main_name=近一周信访件次,同比,环比,指数状态&day=[now-7,now]&Cqh=忠县",
}
