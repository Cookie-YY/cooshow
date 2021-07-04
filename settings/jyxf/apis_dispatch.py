URL_DISPATCH_MAP = {
    # 全局业务监控
    "全局业务监控_信访形式分布1_信访日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_xj_xfxs_xfjc&transformer=@groupby&shej_02=广东省&day=[2019-01-01,2019-01-09]&Cqh=广东省",
    "全局业务监控_信访形式分布1_登记日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_xj_xfxs_djrqxfjc&value=djrqxfjc&transformer=@groupby&shej_02=广东省&day=[2019-01-01,2019-01-09]&Cqh=广东省",
    "全局业务监控_信访形式分布1_交换日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_shej_xfxs_jhrqxfjc&value=jhrqxfjc&transformer=@groupby&shej_02=广东省&day=[2019-01-01,2019-01-09]",

    "全局业务监控_信访形式分布2_信访日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_xj_xfxs_xfjc&name=xfxs&stack=xfxs&transformer=@groupby&extra_index=transformer@to:@zb,table@to:xf_xfj_cd_xj_xfxs_xfrqxfrc;value@to:xfrqxfrc,table@to:xf_xfj_cd_xj_xfxs_xfrqxfrc;value@to:xfrqxfrc;transformer@to:@zb&main_name=信访件次,件次占比,信访人次,人次占比&day=[2019-01-01,2020-02-02]&full=true&Cqh=广东省",
    "全局业务监控_信访形式分布2_登记日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_xj_xfxs_djrqxfjc&name=xfxs&value=djrqxfjc&stack=xfxs&transformer=@groupby&extra_index=transformer@to:@zb,table@to:xf_xfj_cd_xj_xfxs_djrqxfrc;value@to:djrqxfrc,table@to:xf_xfj_cd_xj_xfxs_djrqxfrc;value@to:djrqxfrc;transformer@to:@zb&main_name=信访件次,件次占比,信访人次,人次占比&day=[2019-01-01,2020-02-02]&full=true&Cqh=广东省",
    "全局业务监控_信访形式分布2_交换日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_shej_xfxs_jhrqxfjc&name=xfxs&value=jhrqxfjc&stack=xfxs&transformer=@groupby&extra_index=transformer@to:@zb,table@to:xf_xfj_cd_shej_xfxs_jhrqxfrc;value@to:jhrqxfrc,table@to:xf_xfj_cd_shej_xfxs_jhrqxfrc;value@to:jhrqxfrc;transformer@to:@zb&main_name=信访件次,件次占比,信访人次,人次占比&day=[2019-01-01,2020-02-02]&full=true",

    # "全局业务监控_信访形式分布3_信访日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_shej_xfxs_xfrqxfjc&name=xfxs&value=xfrqxfjc&transformer=@groupby&shej_02=广东省&day=[2019-01-01,2019-01-09]&full=true",
    # "全局业务监控_信访形式分布3_登记日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_shej_xfxs_djrqxfjc&name=xfxs&value=djrqxfjc&transformer=@groupby&shej_02=广东省&day=[2019-01-01,2019-01-09]&full=true",
    # "全局业务监控_信访形式分布3_交换日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_shej_xfxs_jhrqxfjc&name=xfxs&value=jhrqxfjc&transformer=@groupby&shej_02=广东省&day=[2019-01-01,2019-01-09]&full=true",
    "全局业务监控_信访形式分布3_信访日期$": "http://39.107.240.28:3390/api/xf/?gd_id=gd_qjywjk_xfxstc&query_date=信访日期&table=shej&Cqh=广东省",
    "全局业务监控_信访形式分布3_登记日期$": "http://39.107.240.28:3390/api/xf/?gd_id=gd_qjywjk_xfxstc&query_date=登记日期&table=shej&Cqh=广东省",
    "全局业务监控_信访形式分布3_交换日期$": "http://39.107.240.28:3390/api/xf/?gd_id=gd_qjywjk_xfxstc&query_date=交换日期&table=shej&Cqh=广东省",

    "全局业务监控_四级登记机构_国家_信访日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_qh_djjg_xfxs_xfrqxfjc&name=xfxs&value=xfrqxfjc&transformer=@groupby&day=[2019-01-01,2019-01-09]&full=true&Cqh=广东省&param_trans=djjg_qhauth(国家)",
    "全局业务监控_四级登记机构_国家_登记日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_qh_djjg_xfxs_djrqxfjc&name=xfxs&value=djrqxfjc&transformer=@groupby&day=[2019-01-01,2020-12-02]&full=true&Cqh=广东省&param_trans=djjg_qhauth(国家)",
    "全局业务监控_四级登记机构_国家_交换日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_djjg_xfxs_jhrqxfjc&name=xfxs&value=jhrqxfjc&transformer=@groupby&day=[2019-01-01,2020-12-02]&full=true&Cqh=广东省&param_trans=djjg_qhauth(国家)",

    "全局业务监控_四级登记机构_省级_信访日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_qh_djjg_xfxs_xfrqxfjc&name=xfxs&value=xfrqxfjc&transformer=@groupby&day=[2019-01-01,2019-01-09]&full=true&Cqh=广东省&param_trans=djjg_qhauth(省级)",
    "全局业务监控_四级登记机构_省级_登记日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_qh_djjg_xfxs_djrqxfjc&name=xfxs&value=djrqxfjc&transformer=@groupby&day=[2019-01-01,2020-12-02]&full=true&Cqh=广东省&param_trans=djjg_qhauth(省级)",
    "全局业务监控_四级登记机构_省级_交换日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_djjg_xfxs_jhrqxfjc&name=xfxs&value=jhrqxfjc&transformer=@groupby&day=[2019-01-01,2020-12-02]&full=true&Cqh=广东省&param_trans=djjg_qhauth(省级)",

    "全局业务监控_四级登记机构_市级_信访日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_qh_djjg_xfxs_xfrqxfjc&name=xfxs&value=xfrqxfjc&transformer=@groupby&day=[2019-01-01,2019-01-09]&full=true&Cqh=广东省&param_trans=djjg_qhauth(市级)",
    "全局业务监控_四级登记机构_市级_登记日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_qh_djjg_xfxs_djrqxfjc&name=xfxs&value=djrqxfjc&transformer=@groupby&day=[2019-01-01,2020-12-02]&full=true&Cqh=广东省&param_trans=djjg_qhauth(市级)",
    "全局业务监控_四级登记机构_市级_交换日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_djjg_xfxs_jhrqxfjc&name=xfxs&value=jhrqxfjc&transformer=@groupby&day=[2019-01-01,2020-12-02]&full=true&Cqh=广东省&param_trans=djjg_qhauth(市级)",

    "全局业务监控_四级登记机构_县级_信访日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_qh_djjg_xfxs_xfrqxfjc&name=xfxs&value=xfrqxfjc&transformer=@groupby&day=[2019-01-01,2019-01-09]&full=true&Cqh=广东省&param_trans=djjg_qhauth(县级)",
    "全局业务监控_四级登记机构_县级_登记日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_qh_djjg_xfxs_djrqxfjc&name=xfxs&value=djrqxfjc&transformer=@groupby&day=[2019-01-01,2020-12-02]&full=true&Cqh=广东省&param_trans=djjg_qhauth(县级)",
    "全局业务监控_四级登记机构_县级_交换日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_djjg_xfxs_jhrqxfjc&name=xfxs&value=jhrqxfjc&transformer=@groupby&day=[2019-01-01,2020-12-02]&full=true&Cqh=广东省&param_trans=djjg_qhauth(县级)",

    # 全局业务监控_内容分类
    "全局业务监控_内容分类1_信访日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_xj_yjnr_xfjc&value=xfjc&transformer=@groupby&Cqh=广东省&day=[2019-01-01,2019-01-09]",
    "全局业务监控_内容分类1_登记日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_xj_yjnr_djrqxfjc&value=djrqxfjc&transformer=@groupby&Cqh=广东省&day=[2019-01-01,2019-01-09]",
    "全局业务监控_内容分类1_交换日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_shej_yjnr_jhrqxfjc&value=jhrqxfjc&transformer=@groupby&shej_02=广东省&day=[2019-01-01,2019-01-09]",

    "全局业务监控_内容分类2_信访日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_xj_yjnr_xfjc&name=yjnr&value=xfjc&stack=yjnr&transformer=@groupby&order=-xfjc&limit=3&extra_index=transformer@to:@zb;limit@drop;order@drop,table@to:xf_xfj_cd_xj_yjnr_xfrqxfrc;value@to:xfrqxfrc;limit@drop;order@drop,table@to:xf_xfj_cd_xj_yjnr_xfrqxfrc;value@to:xfrqxfrc;limit@drop;order@drop;transformer@to:@zb&main_name=信访件次,件次占比,信访人次,人次占比&day=[2019-01-01,2020-02-02]&full=true&Cqh=广东省",
    "全局业务监控_内容分类2_登记日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_xj_yjnr_djrqxfjc&name=yjnr&value=djrqxfjc&stack=yjnr&transformer=@groupby&order=-djrqxfjc&limit=3&extra_index=transformer@to:@zb;limit@drop;order@drop,table@to:xf_xfj_cd_xj_yjnr_djrqxfrc;value@to:djrqxfrc;limit@drop;order@drop,table@to:xf_xfj_cd_xj_yjnr_djrqxfrc;value@to:djrqxfrc;limit@drop;order@drop;transformer@to:@zb&main_name=信访件次,件次占比,信访人次,人次占比&day=[2019-01-01,2020-02-02]&full=true&Cqh=广东省",
    "全局业务监控_内容分类2_交换日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_shej_yjnr_jhrqxfjc&name=yjnr&value=jhrqxfjc&stack=yjnr&transformer=@groupby&extra_index=transformer@to:@zb,table@to:xf_xfj_cd_shej_yjnr_jhrqxfrc;value@to:jhrqxfrc,table@to:xf_xfj_cd_shej_yjnr_jhrqxfrc;value@to:jhrqxfrc;transformer@to:@zb&main_name=信访件次,件次占比,信访人次,人次占比&day=[2019-01-01,2020-02-02]&full=true",

    # "全局业务监控_内容分类3_信访日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_shej_yjnr_xfrqxfjc&name=yjnr&value=xfrqxfjc&transformer=@groupby&shej_02=广东省&day=[2019-01-01,2019-01-09]&full=true",
    # "全局业务监控_内容分类3_登记日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_shej_yjnr_djrqxfjc&name=yjnr&value=djrqxfjc&transformer=@groupby&shej_02=广东省&day=[2019-01-01,2019-01-09]&full=true",
    # "全局业务监控_内容分类3_交换日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_shej_yjnr_jhrqxfjc&name=yjnr&value=jhrqxfjc&transformer=@groupby&shej_02=广东省&day=[2019-01-01,2019-01-09]&full=true",
    "全局业务监控_内容分类3_信访日期$": "http://39.107.240.28:3390/api/xf/?gd_id=gd_qjywjk_yjnrtc&query_date=信访日期&Cqh=广东省&table=shej",
    "全局业务监控_内容分类3_登记日期$": "http://39.107.240.28:3390/api/xf/?gd_id=gd_qjywjk_yjnrtc&query_date=登记日期&Cqh=广东省&table=shej",
    "全局业务监控_内容分类3_交换日期$": "http://39.107.240.28:3390/api/xf/?gd_id=gd_qjywjk_yjnrtc&query_date=交换日期&Cqh=广东省&table=shej",

    # 全局业务监控_问题属地1 总数
    "全局业务监控_问题属地1_信访日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_xj_xfjc&transformer=@groupby&shej_02=广东省&shij_02=invalid&xj_02=invalid&day=[2019-01-01,2019-01-09]",
    "全局业务监控_问题属地1_登记日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_xj_djrqxfjc&value=djrqxfjc&transformer=@groupby&shej_02=广东省&shij_02=invalid&xj_02=invalid&day=[2019-01-01,2019-01-09]",
    "全局业务监控_问题属地1_交换日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_xj_jhrqxfjc&value=jhrqxfjc&transformer=@groupby&shej_02=广东省&shij_02=invalid&xj_02=invalid&day=[2019-01-01,2019-01-09]",

    # 全局业务监控_问题属地2 地图
    # "全局业务监控_问题属地2_信访日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_xj_xfrqxfjc&name=shij_02&value=xfrqxfjc&shej_02=广东省&shij_02=invalid&xj_02=invalid&day=[2019-01-01,2019-01-09]&full=true",
    # "全局业务监控_问题属地2_登记日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_xj_djrqxfjc&name=shij_02&value=djrqxfjc&shej_02=广东省&shij_02=invalid&xj_02=invalid&day=[2019-01-01,2019-01-09]&full=true",
    # "全局业务监控_问题属地2_交换日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_xj_jhrqxfjc&name=shij_02&value=jhrqxfjc&shej_02=广东省&shij_02=invalid&xj_02=invalid&day=[2019-01-01,2019-01-09]&full=true",
    "全局业务监控_问题属地2_信访日期$": "http://39.107.240.28:3390/api/xf/?gd_id=gd_qjywjk_dttc&query_date=信访日期&table=shej&Cqh=广东省&param_trans=qh_godown",
    "全局业务监控_问题属地2_登记日期$": "http://39.107.240.28:3390/api/xf/?gd_id=gd_qjywjk_dttc&query_date=登记日期&table=shej&Cqh=广东省&param_trans=qh_godown",
    "全局业务监控_问题属地2_交换日期$": "http://39.107.240.28:3390/api/xf/?gd_id=gd_qjywjk_dttc&query_date=交换日期&table=shej&Cqh=广东省&param_trans=qh_godown",

    # 全局业务监控_问题属地3 折线
    "全局业务监控_问题属地3_信访日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_xj_xfjc&name=day&value=xfjc&shej_02=广东省&shij_02=invalid&xj_02=invalid&day=[2019-01-01,2019-01-09]&full=true",
    "全局业务监控_问题属地3_登记日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_xj_djrqxfjc&name=day&value=djrqxfjc&shej_02=广东省&shij_02=invalid&xj_02=invalid&day=[2019-01-01,2019-01-09]&full=true",
    "全局业务监控_问题属地3_交换日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_xj_jhrqxfjc&name=day&value=jhrqxfjc&shej_02=广东省&shij_02=invalid&xj_02=invalid&day=[2019-01-01,2019-01-09]&full=true",

    "全局业务监控_问题属地4_信访日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_xj_nlrange_xfrqxfrc&name=nlrange&value=xfrqxfrc&transformer=@groupby&shej_02=广东省&shij_02=invalid&xj_02=invalid&day=[2019-01-01,2019-01-09]&full=true",
    "全局业务监控_问题属地4_登记日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_xj_nlrange_djrqxfrc&name=nlrange&value=djrqxfrc&transformer=@groupby&shej_02=广东省&shij_02=invalid&xj_02=invalid&day=[2019-01-01,2019-01-09]&full=true",
    "全局业务监控_问题属地4_交换日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_xj_nlrange_jhrqxfrc&name=nlrange&value=jhrqxfrc&transformer=@groupby&shej_02=广东省&shij_02=invalid&xj_02=invalid&day=[2019-01-01,2019-01-09]&full=true",

    "全局业务监控_问题属地5_信访日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_xj_xb_xfrqxfrc&name=xb&value=xfrqxfrc&transformer=@groupby&shej_02=广东省&shij_02=invalid&xj_02=invalid&day=[2019-01-01,2019-01-09]&full=true",
    "全局业务监控_问题属地5_登记日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_xj_xb_djrqxfrc&name=xb&value=djrqxfrc&transformer=@groupby&shej_02=广东省&shij_02=invalid&xj_02=invalid&day=[2019-01-01,2019-01-09]&full=true",
    "全局业务监控_问题属地5_交换日期$": "http://39.107.240.28:3390/api/xf/?table=xf_xfj_cd_xj_xb_jhrqxfrc&name=xb&value=jhrqxfrc&transformer=@groupby&shej_02=广东省&shij_02=invalid&xj_02=invalid&day=[2019-01-01,2019-01-09]&full=true",





    ####################################### 领导驾驶舱 #######################################
    # 责任单位画像-趋势特征【信访事项待完成】
    "责任单位画像_趋势特征_趋势_信访量$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_yjnr_sljc&name=shij_02&value=sljc&transformer=@groupby&shej_02=广东省&day=[2019-01-01,2019-01-09]&full=true",
    "责任单位画像_趋势特征_趋势_信访事项$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_yjnr_sljc&name=shij_02&value=sljc&transformer=@groupby&shej_02=广东省&day=[2019-01-01,2019-01-09]&full=true",

    # 责任单位画像-办理质量【缺full】
    "责任单位画像_办理质量_办理量$": "http://127.0.0.1:3389/api/xf/?table=xf_xfjg_cd_qh_zrdw_bljc&order=-bljc&limit=10&name=zrdw&value=bljc&transformer=@groupby&Cqh=广东省&day=[2020-01-01,2020-10-09]",
    "责任单位画像_办理质量_满意率$": "http://127.0.0.1:3389/api/xf/?table=xf_xfjg_cd_qh_zrdw_myjc&order=-mylv&limit=10&name=zrdw&transformer=@mylv&day=[2020-01-01,2020-10-09]&full=true",
    # 待实现
    "责任单位画像_办理质量_答复率$": "http://127.0.0.1:3389/api/xf/?table=xf_xfjg_cd_qh_zrdw_myjc&order=-mylv&limit=10&name=zrdw&transformer=@mylv&day=[2020-01-01,2020-10-09]&full=true",
    # 待实现
    "责任单位画像_办理质量_受理率$": "http://127.0.0.1:3389/api/xf/?table=xf_xfjg_cd_qh_zrdw_myjc&order=-mylv&limit=10&name=zrdw&transformer=@mylv&day=[2020-01-01,2020-10-09]&full=true",


    # 每日信访动态
    "每日信访动态_全省信访量$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_xfxs_xfjc&value=xfjc&transformer=@groupby&Cqh=广东省&full=true&day=now-1",
    "每日信访动态_信访形式列表$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_xfxs_xfjc&name=xfxs&value=xfjc&transformer=@groupby&Cqh=广东省&full=true&day=now-1",
    "每日信访动态_地图$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_xfxs_xfjc&transformer=@groupby&stack=$name&value=xfjc&extra_index=stack@to:xfxs&main_name=总数,&Cqh=广东省&full=true&day=now-1&param_trans=qh_godown",
    "每日信访动态_热点问题分布$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_yjnr_xfjc&name=yjnr&value=xfjc&transformer=@groupby&order=desc&limit=10&Cqh=广东省&full=true&day=now-1",
    "每日信访动态_区域信访量排行$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_xfjc&value=xfjc&transformer=@groupby&Cqh=广东省&full=true&day=now-1&param_trans=qh_godown",
    "每日信访动态_信访量概况$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_yyxfjc&Cqh=广东省&transformer=@groupby&full=true&extra_index=table@to:xf_xfj_cd_xj_gjjxfjc,table@to:xf_xfj_cd_xj_jtf_xfjc;jtf@to:集体访&main_name=扬言件,国家局上访,集体访&day=now-1",


    # 信访事项预警
    "信访事项预警_赴省访_信访量$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_xfjc&order=-xfjc&transformer=@groupby&full=true&day=[2020-01-01,2020-10-09]&param_trans=qh_godown&Cqh=广东省",
    # "信访事项预警_赴省访_满意率-信访部门$": "http://127.0.0.1:3389/api/xf/?table=xf_xfjg_cd_bmjb_qh_xfbm_myjc&order=-mylv&transformer=@mylv&full=true&day=[2020-01-01,2020-10-09]&param_trans=qh_include_sub,qh_godown&Cqh=广东省",
    # "信访事项预警_赴省访_满意率-责任单位$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_zrdwgjjmyjc&order=-mylv&transformer=@mylv&full=true&day=[2020-01-01,2020-10-09]&param_trans=qh_include_sub,qh_godown&Cqh=广东省",
    "信访事项预警_赴省访_信访量走势$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cm_xj_xfjc&name=date&transformer=@groupby&full=true&param_protect=black_list(day)&time_format=%Y年%m月&date=[now-12m,now]&Cqh=广东省",
    "信访事项预警_赴省访_预警状态$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_xfjc&full=true&transformer=@yjzt&extra_index=transformer@to:@groupby,transformer@to:@tb,transformer@to:@hb&main_name=预警状态,近一周,同比,环比&day=[now-7,now]&Cqh=广东省&param_protect=black_list(day)",
    "信访事项预警_赴省访_内容分类$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_yjnr_xfjc&name=yjnr&full=true&transformer=@groupby&day=[2020-01-01,2020-10-09]&Cqh=广东省",
    "信访事项预警_赴省访_信访形式$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_xfxs_xfjc&name=xfxs&full=true&transformer=@groupby&day=[2020-01-01,2020-10-09]&Cqh=广东省",

    "信访事项预警_进京访_信访量$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_gjjxfjc&order=-gjjxfjc&transformer=@groupby&full=true&day=[2020-01-01,2020-10-09]&param_trans=qh_godown&Cqh=广东省",
    # "信访事项预警_进京访_满意率-信访部门$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_xfbmgjjmyjc&order=-mylv&transformer=@mylv&full=true&day=[2020-01-01,2020-10-09]&param_trans=qh_godown&Cqh=广东省",
    # "信访事项预警_进京访_满意率-责任单位$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_zrdwgjjmyjc&order=-mylv&transformer=@mylv&full=true&day=[2020-01-01,2020-10-09]&param_trans=qh_godown&Cqh=广东省",
    "信访事项预警_进京访_信访量走势$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cm_xj_gjjxfjc&name=date&transformer=@groupby&full=true&param_protect=black_list(day)&time_format=%Y年%m月&date=[now-12m,now]&Cqh=广东省",
    "信访事项预警_进京访_预警状态$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_gjjxfjc&full=true&transformer=@yjzt&extra_index=transformer@to:@groupby,transformer@to:@tb,transformer@to:@hb&main_name=预警状态,近一周,同比,环比&day=[now-7,now]&Cqh=广东省&param_protect=black_list(day)",
    "信访事项预警_进京访_内容分类$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_yjnr_gjjxfjc&name=yjnr&full=true&transformer=@groupby&day=[2020-01-01,2020-10-09]&Cqh=广东省",
    "信访事项预警_进京访_信访形式$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_xfxs_gjjxfjc&name=xfxs&full=true&transformer=@groupby&day=[2020-01-01,2020-10-09]&Cqh=广东省",

    "信访事项预警_集体访_信访量$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_dszfxfjc&order=desc&transformer=@groupby&full=true&day=[2020-01-01,2020-10-09]&Cqh=广东省&param_trans=qh_godown",
    # "信访事项预警_集体访_满意率-信访部门$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_jtf_xfbmmyjc&order=-mylv&jtf=集体访&transformer=@mylv&full=true&day=[2020-01-01,2020-10-09]&Cqh=广东省&param_trans=qh_godown",
    # "信访事项预警_集体访_满意率-责任单位$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_jtf_zrdwmyjc&order=-mylv&jtf=集体访&transformer=@mylv&full=true&day=[2020-01-01,2020-10-09]&Cqh=广东省&param_trans=qh_godown",
    "信访事项预警_集体访_信访量走势$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cm_xj_dszfxfjc&name=date&transformer=@groupby&full=true&param_protect=black_list(day)&time_format=%Y年%m月&date=[now-12m,now]&Cqh=广东省",
    "信访事项预警_集体访_预警状态$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_dszfxfjc&full=true&transformer=@yjzt&extra_index=transformer@to:@groupby,transformer@to:@tb,transformer@to:@hb&main_name=预警状态,近一周,同比,环比&day=[now-7,now]&Cqh=广东省&param_protect=black_list(day)",
    "信访事项预警_集体访_内容分类$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_yjnr_dszfxfjc&name=yjnr&full=true&transformer=@groupby&day=[2020-01-01,2020-10-09]&Cqh=广东省",
    "信访事项预警_集体访_信访形式$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_xfxs_dszfxfjc&name=xfxs&full=true&transformer=@groupby&day=[2020-01-01,2020-10-09]&Cqh=广东省",

    # 信访内容分类
    "信访内容分类_一级内容分类_列表": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_yjnr_xfjc&name=yjnr&order=desc&limit=10&day=[2020-01-01,2020-10-09]&Cqh=广东省",
    "信访内容分类_一级内容分类_前n占比": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_yjnr_xfjc&name=yjnr&transformer=topkzb(10)&day=[2020-01-01,2020-10-09]&Cqh=广东省",
    "信访内容分类_二级内容分类_列表": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_ejnr_xfjc&name=ej_nr&order=desc&limit=10&day=[2020-01-01,2020-10-09]&Cqh=广东省",
    "信访内容分类_二级内容分类_前n占比": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_ejnr_xfjc&name=ej_nr&transformer=topkzb(10)&day=[2020-01-01,2020-10-09]&Cqh=广东省",
    "信访内容分类_三级内容分类_列表": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_sjnr_xfjc&name=sj_nr&order=desc&limit=10&day=[2020-01-01,2020-10-09]&Cqh=广东省",
    "信访内容分类_三级内容分类_前n占比": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_sjnr_xfjc&name=sj_nr&transformer=topkzb(10)&day=[2020-01-01,2020-10-09]&Cqh=广东省",

    
    # 信访绩效考核
    # 1. 区划分布

    # 【权限控制需要在sql中判断Cqh】按期答复率+网信占比+重复信访率[分信访形式的需要测试]
    "信访绩效考核_区划分布_总体_(全部|drop)$": "http://127.0.0.1:3389/api/xf/?full=true&transformer=@aqdflv&ext=aqdflv_qh_all_shej/aqdflv_qh_all_shij/aqdflv_qh_all_xj&extra_index=transformer@to:@wxzb;ext@to:wxzb_qh_all_xfbm_shej/wxzb_qh_all_xfbm_shij/wxzb_qh_all_xfbm_xj,transformer@to:@cfxflv;ext@to:cfxflv_qh_all_shej/cfxflv_qh_all_shij/cfxflv_qh_all_xj&param_trans=qh_include_sub&main_name=按期答复率,网信占比,重复信访率&day=[2020-01-01,2020-10-10]&Cqh=广东省",
    "信访绩效考核_区划分布_总体_(?!全部)(?!drop)": "http://127.0.0.1:3389/api/xf/?transformer=@aqdflv&ext=aqdflv_qh_xfxs_shej/aqdflv_qh_xfxs_shij/aqdflv_qh_xfxs_xj&extra_index=transformer@to:@cfxflv;ext@to:cfxflv_qh_xfxs_shej/cfxflv_qh_xfxs_shij/cfxflv_qh_xfxs_xj&main_name=按期答复率,重复信访率&xfxs={gd_id4}&full=true&day=[2020-01-01,2020-10-10]&Cqh=广东省",

    # 【权限控制需要在sql中判断Cqh】参评率+满意率+及时受理率
    "信访绩效考核_区划分布_信访部门_(全部|drop)$": "http://127.0.0.1:3389/api/xf/?xfxs=drop&param_trans=qh_include_sub&transformer=@cplv&ext=cplv_qh_all_xfbm_shej/cplv_qh_all_xfbm_shij/cplv_qh_all_xfbm_xj&full=true&extra_index=transformer@to:@mylv;ext@to:mylv_qh_all_xfbm_shej/mylv_qh_all_xfbm_shij/mylv_qh_all_xfbm_xj,transformer@to:@jssllv;ext@to:jssllv_qh_all_xfbm_shej/jssllv_qh_all_xfbm_shij/jssllv_qh_all_xfbm_xj&main_name=参评率,满意率,及时受理率&day=[2020-01-01,2020-10-10]&Cqh=广东省",
    "信访绩效考核_区划分布_信访部门_(?!全部)(?!drop)": "http://127.0.0.1:3389/api/xf/?xfxs={gd_id4}&param_trans=qh_include_sub&transformer=@cplv&ext=cplv_qh_xfxs_xfbm_shej/cplv_qh_xfxs_xfbm_shij/cplv_qh_xfxs_xfbm_xj&full=true&extra_index=transformer@to:@mylv;ext@to:mylv_qh_xfxs_xfbm_shej/mylv_qh_xfxs_xfbm_shij/mylv_qh_xfxs_xfbm_xj,transformer@to:@jssllv;ext@to:jssllv_qh_xfxs_xfbm_shej/jssllv_qh_xfxs_xfbm_shij/jssllv_qh_xfxs_xfbm_xj&main_name=参评率,满意率,及时受理率&day=[2020-01-01,2020-10-10]&Cqh=广东省",
    # 【权限控制需要在sql中判断Cqh】参评率+满意率+及时受理率
    "信访绩效考核_区划分布_责任单位_(全部|drop)$": "http://127.0.0.1:3389/api/xf/?full=true&xfxs=drop&param_trans=qh_include_sub&transformer=@cplv&ext=cplv_qh_all_zrdw_shej/cplv_qh_all_zrdw_shij/cplv_qh_all_zrdw_xj&extra_index=transformer@to:@mylv;ext@to:mylv_qh_all_zrdw_shej/mylv_qh_all_zrdw_shij/mylv_qh_all_zrdw_xj,transformer@to:@jssllv;ext@to:jssllv_qh_all_zrdw_shej/jssllv_qh_all_zrdw_shij&main_name=参评率,满意率,及时受理率&day=[2020-01-01,2020-10-10]&Cqh=广东省",
    "信访绩效考核_区划分布_责任单位_(?!全部)(?!drop)": "http://127.0.0.1:3389/api/xf/?full=true&xfxs={gd_id4}&param_trans=qh_include_sub&transformer=@cplv&ext=cplv_qh_xfxs_zrdw_shej/cplv_qh_xfxs_zrdw_shij/cplv_qh_xfxs_zrdw_xj&extra_index=transformer@to:@mylv;ext@to:mylv_qh_xfxs_zrdw_shej/mylv_qh_xfxs_zrdw_shij/mylv_qh_xfxs_zrdw_xj,transformer@to:@jssllv;ext@to:jssllv_qh_xfxs_zrdw_shej/jssllv_qh_xfxs_zrdw_shij&main_name=参评率,满意率,及时受理率&day=[2020-01-01,2020-10-10]&Cqh=广东省",

    # 地图【qh的full问题】
    "信访绩效考核_区划分布_区划_(网信|来信|来访)_总体-按期答复率$": "http://127.0.0.1:3389/api/xf/?xfxs={gd_id4}&transformer=@aqdflv&ext=aqdflv_qh_xfxs_allshej/aqdflv_qh_xfxs_allshij&Cqh=广东省&param_trans=qh_godown&day=[2020-01-01,2020-10-10]",
    "信访绩效考核_区划分布_区划_drop_总体-按期答复率$": "http://127.0.0.1:3389/api/xf/?transformer=@aqdflv&ext=aqdflv_qh_all_allshej/aqdflv_qh_all_allshij&Cqh=广东省&param_trans=qh_godown&day=[2020-01-01,2020-10-10]",
    "信访绩效考核_区划分布_区划_(网信|来信|来访)_总体-重复信访率": "http://127.0.0.1:3389/api/xf/?xfxs={gd_id4}&transformer=@cfxflv&ext=cfxflv_qh_xfxs_allshej/cfxflv_qh_xfxs_allshij&Cqh=广东省&param_trans=qh_godown&day=[2020-01-01,2020-10-10]",
    "信访绩效考核_区划分布_区划_drop_总体-重复信访率$": "http://127.0.0.1:3389/api/xf/?transformer=@cfxflv&ext=cfxflv_qh_all_allshej/cfxflv_qh_all_allshij&Cqh=广东省&param_trans=qh_godown&day=[2020-01-01,2020-10-10]",
    "信访绩效考核_区划分布_区划_(网信|来信|来访|drop)_总体-网信占比$": "http://127.0.0.1:3389/api/xf/?transformer=@wxzb&ext=wxzb_qh_allshej/wxzb_qh_allshij&Cqh=广东省&param_trans=qh_godown&day=[2020-01-01,2020-10-10]",
    # 已完成【full怎么加】
    "信访绩效考核_区划分布_区划_drop_信访部门-参评率$": "http://127.0.0.1:3389/api/xf/?transformer=@cplv&ext=cplv_qh_all_xfbm_allshej/cplv_qh_all_xfbm_allshij&Cqh=广东省&param_trans=qh_godown&day=[2020-01-01,2020-10-10]",
    "信访绩效考核_区划分布_区划_(网信|来信|来访)_信访部门-参评率$": "http://127.0.0.1:3389/api/xf/?&xfxs={gd_id4}&transformer=@cplv&ext=cplv_qh_xfxs_xfbm_allshej/cplv_qh_xfxs_xfbm_allshij&Cqh=广东省&param_trans=qh_godown&day=[2020-01-01,2020-10-10]",
    # 已完成【full怎么加】
    "信访绩效考核_区划分布_区划_drop_信访部门-满意率$": "http://127.0.0.1:3389/api/xf/?transformer=@mylv&ext=mylv_qh_all_xfbm_allshej/mylv_qh_all_xfbm_allshij&Cqh=广东省&param_trans=qh_godown&day=[2020-01-01,2020-10-10]",
    "信访绩效考核_区划分布_区划_(网信|来信|来访)_信访部门-满意率$": "http://127.0.0.1:3389/api/xf/?&xfxs={gd_id4}&transformer=@mylv&ext=mylv_qh_xfxs_xfbm_allshej/mylv_qh_xfxs_xfbm_allshij&Cqh=广东省&param_trans=qh_godown&day=[2020-01-01,2020-10-10]",

    "信访绩效考核_区划分布_区划_(网信|来信|来访)_信访部门-及时受理率$": "http://127.0.0.1:3389/api/xf/?xfxs={gd_id4}&transformer=@jssllv&ext=jssllv_qh_xfxs_xfbm_allshej/jssllv_qh_xfxs_xfbm_allshij&Cqh=广东省&param_trans=qh_godown&day=[2020-01-01,2020-10-10]",
    "信访绩效考核_区划分布_区划_drop_信访部门-及时受理率$": "http://127.0.0.1:3389/api/xf/?transformer=@jssllv&ext=jssllv_qh_all_xfbm_allshej/jssllv_qh_all_xfbm_allshij&Cqh=广东省&param_trans=qh_godown&day=[2020-01-01,2020-10-10]",

    "信访绩效考核_区划分布_区划_drop_责任单位-参评率$": "http://127.0.0.1:3389/api/xf/?transformer=@cplv&ext=cplv_qh_all_zrdw_allshej/cplv_qh_all_zrdw_allshij&Cqh=广东省&param_trans=qh_godown&day=[2020-01-01,2020-10-10]",
    "信访绩效考核_区划分布_区划_(网信|来信|来访)_责任单位-参评率$": "http://127.0.0.1:3389/api/xf/?&xfxs={gd_id4}&transformer=@cplv&ext=cplv_qh_xfxs_zrdw_allshej/cplv_qh_xfxs_zrdw_allshij&Cqh=广东省&param_trans=qh_godown&day=[2020-01-01,2020-10-10]",

    "信访绩效考核_区划分布_区划_drop_责任单位-满意率$": "http://127.0.0.1:3389/api/xf/?transformer=@mylv&ext=mylv_qh_all_zrdw_allshej/mylv_qh_all_zrdw_allshij&Cqh=广东省&param_trans=qh_godown&day=[2020-01-01,2020-10-10]",
    "信访绩效考核_区划分布_区划_(网信|来信|来访)_责任单位-满意率$": "http://127.0.0.1:3389/api/xf/?&xfxs={gd_id4}&transformer=@mylv&ext=mylv_qh_xfxs_zrdw_allshej/mylv_qh_xfxs_zrdw_allshij&Cqh=广东省&param_trans=qh_godown&day=[2020-01-01,2020-10-10]",

    "信访绩效考核_区划分布_区划_(网信|来信|来访)_责任单位-及时受理率$": "http://127.0.0.1:3389/api/xf/?xfxs={gd_id4}&transformer=@jssllv&ext=jssllv_qh_xfxs_zrdw_allshej/jssllv_qh_xfxs_zrdw_allshij&Cqh=广东省&param_trans=qh_godown&day=[2020-01-01,2020-10-10]",
    "信访绩效考核_区划分布_区划_drop_责任单位-及时受理率$": "http://127.0.0.1:3389/api/xf/?xfxs={gd_id4}&transformer=@jssllv&ext=jssllv_qh_all_zrdw_allshej/jssllv_qh_all_zrdw_allshij&Cqh=广东省&param_trans=qh_godown&day=[2020-01-01,2020-10-10]",

    # 2. 信访部门 [xfxs=drop/来信/来访/网信  xfbm=广东省信访局   xfxs=   bmjb=省级]（bmjb给到sql实现的三率，正常实现的不影响）
    # 【转交办效率待实现】待领 待办 超期未答复 转交办效率
    "信访绩效考核_信访部门_工作过程监控$": "http://127.0.0.1:3389/api/xf/?table=xf_xfjg_cd_bmjb_qh_xfbm_xfxs_dljc&value=dljc&transformer=@groupby&full=true&day=[2020-01-01,2020-10-09]&extra_index=table@to:xf_xfjg_cd_bmjb_qh_xfbm_xfxs_dbjc;value@to:dbjc,table@to:xf_xfjg_cd_bmjb_qh_xfbm_xfxs_cqwbjjc;value@to:cqwbjjc&main_name=待领,待办,超期未答复&xfbm=广东省信访局&param_trans=@trimXfbm",

    "信访绩效考核_信访部门_参评饼图$": "http://127.0.0.1:3389/api/xf/?transformer=@cplv&ext=cplv_xfbm_all_shejnums/cplv_xfbm_all_shijnums/cplv_xfbm_all_xjnums/cplv_xfbm_xfxs_shejnums/cplv_xfbm_xfxs_shijnums/cplv_xfbm_xfxs_xjnums&name=cpqk&full=true&day=[2020-01-01,2020-10-09]&xfbm=广东省信访局&bmjb=省级",
    "信访绩效考核_信访部门_参评率$": "http://127.0.0.1:3389/api/xf/?transformer=@cplv&ext=cplv_qh_all_xfbm_shej/cplv_qh_all_xfbm_shij/cplv_qh_all_xfbm_xj/cplv_qh_xfxs_xfbm_shej/cplv_qh_xfxs_xfbm_shij/cplv_qh_xfxs_xfbm_xj&full=true&day=[2020-01-01,2020-10-09]&xfbm=广东省信访局&bmjb=省级&xfxs=",

    "信访绩效考核_信访部门_满意饼图$": "http://127.0.0.1:3389/api/xf/?transformer=@mylv&ext=mylv_xfbm_all_shejnums/mylv_xfbm_all_shijnums/mylv_xfbm_all_xjnums/mylv_xfbm_xfxs_shejnums/mylv_xfbm_xfxs_shijnums/mylv_xfbm_xfxs_xjnums&name=myqk&full=true&day=[2020-01-01,2020-10-09]&xfbm=广东省信访局&bmjb=省级",
    "信访绩效考核_信访部门_满意率$": "http://127.0.0.1:3389/api/xf/?transformer=@mylv&ext=mylv_qh_all_xfbm_shej/mylv_qh_all_xfbm_shij/mylv_qh_all_xfbm_xj/mylv_qh_xfxs_xfbm_shej/mylv_qh_xfxs_xfbm_shij/mylv_qh_xfxs_xfbm_xj&full=true&day=[2020-01-01,2020-10-09]&xfbm=广东省信访局&bmjb=省级",

    "信访绩效考核_信访部门_及时受理饼图$": "http://127.0.0.1:3389/api/xf/?transformer=@jssllv&ext=jssllv_qh_all_xfbm_shej_nums/jssllv_qh_all_xfbm_shij_nums/jssllv_qh_all_xfbm_xj_nums/jssllv_qh_xfxs_xfbm_shej_nums/jssllv_qh_xfxs_xfbm_shij_nums/jssllv_qh_xfxs_xfbm_xj_nums&name=slqk&full=true&xfbm=广东省信访局&bmjb=省级&day=[2020-01-01,2020-10-09]",
    "信访绩效考核_信访部门_及时受理率$": "http://127.0.0.1:3389/api/xf/?&full=true&transformer=@jssllv&ext=jssllv_qh_all_xfbm_shej/jssllv_qh_all_xfbm_shij/jssllv_qh_all_xfbm_xj/jssllv_qh_xfxs_xfbm_shej/jssllv_qh_xfxs_xfbm_shij/jssllv_qh_xfxs_xfbm_xj&xfbm=广东省信访局&bmjb=省级&day=[2020-01-01,2020-10-09]",

    "信访绩效考核_信访部门_网信占比饼图$": "http://127.0.0.1:3389/api/xf/?transformer=@wxzb&ext=wxzb_xfbm_shejnums/wxzb_xfbm_shijnums/wxzb_xfbm_xjnums&name=wxqk&full=true&day=[2020-01-01,2020-10-09]&xfbm=广东省信访局&bmjb=省级",
    "信访绩效考核_信访部门_网信占比率$": "http://127.0.0.1:3389/api/xf/?transformer=@wxzb&ext=wxzb_qh_all_xfbm_shej/wxzb_qh_all_xfbm_shij/wxzb_qh_all_xfbm_xj&full=true&day=[2020-01-01,2020-10-09]&xfbm=广东省信访局&bmjb=省级",

    # xfbm_godowm需要实现【直属小弟】 排名需要把name换成
    "信访绩效考核_信访部门_排名_参评率$": "http://127.0.0.1:3389/api/xf/?xfxs=&transformer=@cplv&ext=cplv_qh_all_xfbm_allshej/cplv_qh_all_xfbm_allshij/cplv_qh_xfxs_xfbm_allshej/cplv_qh_xfxs_xfbm_allshij&name=qh&order=-cplv&day=[2020-01-01,2020-10-10]&xfbm=广东省信访局&bmjb=省级&param_trans=qh_godown",
    "信访绩效考核_信访部门_排名_满意率$": "http://127.0.0.1:3389/api/xf/?xfxs=&transformer=@mylv&ext=mylv_qh_all_xfbm_allshej/mylv_qh_all_xfbm_allshij/mylv_qh_xfxs_xfbm_allshej/mylv_qh_xfxs_xfbm_allshij&name=qh&order=-mylv&day=[2020-01-01,2020-10-10]&xfbm=广东省信访局&bmjb=省级&param_trans=qh_godown",
    "信访绩效考核_信访部门_排名_及时受理率$": "http://127.0.0.1:3389/api/xf/?xfxs=&full=true&transformer=@jssllv&ext=jssllv_qh_all_xfbm_allshej/jssllv_qh_all_xfbm_allshij/jssllv_qh_xfxs_xfbm_allshej/jssllv_qh_xfxs_xfbm_allshij&order=-jssllv&name=qh&day=[2020-01-01,2020-10-09]&xfbm=广东省信访局&bmjb=省级&param_trans=qh_godown",
    "信访绩效考核_信访部门_排名_网信占比$": "http://127.0.0.1:3389/api/xf/?transformer=wxzb&ext=wxzb_qh_allshej/wxzb_qh_allshij&full=true&transformer=@wxzb&name=qh&order=-wxzb&day=[2020-01-01,2020-10-09]&full=true&xfbm=广东省信访局&bmjb=省级&param_protect=black_list(xfxs)&param_trans=qh_godown",

    # 3. 责任单位[xfxs=drop/来信/来访/网信  zrdw=广东省统计局  xfxs=  Cqh=广东省（bmjb给到sql实现的三率，正常实现的不影响）]
    # 【转交办效率待实现】待领 待办 超期未答复 转交办效率
    "信访绩效考核_责任单位_工作过程监控$": "http://127.0.0.1:3389/api/xf/?table=xf_xfjg_cd_qh_zrdw_xfxs_dljc&value=dljc&transformer=@groupby&full=true&day=[2020-01-01,2020-10-09]&extra_index=table@to:xf_xfjg_cd_qh_zrdw_xfxs_dbjc;value@to:dbjc,table@to:xf_xfjg_cd_qh_zrdw_xfxs_cqwbjjc;value@to:cqwbjjc&main_name=待领,待办,超期未答复&zrdw=广东省信访局",

    "信访绩效考核_责任单位_参评饼图$": "http://127.0.0.1:3389/api/xf/?transformer=@cplv&ext=cplv_zrdw_all_shejnums/cplv_zrdw_all_shijnums/cplv_zrdw_all_xjnums/cplv_zrdw_xfxs_shejnums/cplv_zrdw_xfxs_shijnums/cplv_zrdw_xfxs_xjnums&name=cpqk&full=true&day=[2020-01-01,2020-10-09]&zrdw=广东省信访局&Cqh=广东省",
    "信访绩效考核_责任单位_参评率$": "http://127.0.0.1:3389/api/xf/?transformer=@cplv&ext=cplv_qh_all_zrdw_shej/cplv_qh_all_zrdw_shij/cplv_qh_all_zrdw_xj/cplv_qh_xfxs_zrdw_shej/cplv_qh_xfxs_zrdw_shij/cplv_qh_xfxs_zrdw_xj&full=true&day=[2020-01-01,2020-10-09]&zrdw=广东省信访局&Cqh=广东省",

    "信访绩效考核_责任单位_满意饼图$": "http://127.0.0.1:3389/api/xf/?transformer=@mylv&ext=mylv_zrdw_all_shejnums/mylv_zrdw_all_shijnums/mylv_zrdw_all_xjnums/mylv_zrdw_xfxs_shejnums/mylv_zrdw_xfxs_shijnums/mylv_zrdw_xfxs_xjnums&name=myqk&full=true&day=[2020-01-01,2020-10-09]&zrdw=广东省统计局&Cqh=广东省",
    "信访绩效考核_责任单位_满意率$": "http://127.0.0.1:3389/api/xf/?transformer=@mylv&ext=mylv_qh_all_zrdw_shej/mylv_qh_all_zrdw_shij/mylv_qh_all_zrdw_xj/mylv_qh_xfxs_zrdw_shej/mylv_qh_xfxs_zrdw_shij/mylv_qh_xfxs_zrdw_xj&full=true&day=[2020-01-01,2020-10-09]&zrdw=广东省统计局&Cqh=广东省",

    # 调试模式下，当Cqh=广东省时报错
    "信访绩效考核_责任单位_及时受理饼图$": "http://127.0.0.1:3389/api/xf/?transformer=@jssllv&ext=jssllv_qh_all_zrdw_shej_nums/jssllv_qh_all_zrdw_shij_nums/jssllv_qh_all_zrdw_xj_nums/jssllv_qh_xfxs_zrdw_shej_nums/jssllv_qh_xfxs_zrdw_shij_nums/jssllv_qh_xfxs_zrdw_xj_nums&name=slqk&day=[2020-01-01,2020-10-09]&zrdw=广东省信访局&Cqh=广东省",
    "信访绩效考核_责任单位_及时受理率$": "http://127.0.0.1:3389/api/xf/?full=true&transformer=@jssllv&ext=jssllv_qh_all_zrdw_shej/jssllv_qh_all_zrdw_shij/jssllv_qh_all_zrdw_xj/jssllv_qh_xfxs_zrdw_shej/jssllv_qh_xfxs_zrdw_shij/jssllv_qh_xfxs_zrdw_xj&day=[2020-01-01,2020-10-09]&zrdw=广东省统计局&Cqh=广东省",

    # "信访绩效考核_责任单位_网信占比饼图$": "http://127.0.0.1:3389/api/xf/?table=xf_xfjg_cd_qh_zrdw_xfxs_xfjc&name=xfxs&transformer=@groupby&full=true&day=[2020-01-01,2020-10-09]&zrdw=广东省统计局",
    # "信访绩效考核_责任单位_网信占比率$": "http://127.0.0.1:3389/api/xf/?table=xf_xfjg_cd_qh_zrdw_xfxs_myjc&full=true&transformer=@mylv&day=[2020-01-01,2020-10-09]&zrdw=广东省统计局",

    # zrdw_godown待实现【省级的时候，直属小弟】
    "信访绩效考核_责任单位_排名_参评率$": "http://127.0.0.1:3389/api/xf/?&transformer=@cplv&ext=cplv_zrdw_all_allshej/cplv_zrdw_all_allshij/cplv_zrdw_xfxs_allshej/cplv_zrdw_xfxs_allshej&day=[2020-01-01,2020-10-10]&limit=20&Cqh=广东省&name=qh&xfxs=&order=-cplv&full=true",
    "信访绩效考核_责任单位_排名_满意率$": "http://127.0.0.1:3389/api/xf/?&transformer=@mylv&ext=mylv_zrdw_all_allshej/mylv_zrdw_all_allshij/mylv_zrdw_xfxs_allshej/mylv_zrdw_xfxs_allshej&day=[2020-01-01,2020-10-10]&limit=20&Cqh=广东省&name=qh&xfxs=&order=-mylv&full=true",
    "信访绩效考核_责任单位_排名_及时受理率$": "http://127.0.0.1:3389/api/xf/?&transformer=@jssllv&ext=jssllv_zrdw_all_allshej/jssllv_qh_all_zrdw_allshij/jssllv_zrdw_xfxs_allshej/jssllv_qh_xfxs_zrdw_allshij&order=-jssllv&limit=20&day=[2020-01-01,2020-10-09]&name=qh&full=true&Cqh=广州市&xfxs=",
    # "信访绩效考核_责任单位_(来信|来访|网信)_排名_及时受理率$": "http://127.0.0.1:3389/api/xf/?&full=true&transformer=@jssllv&ext=jssllv_zrdw_xfxs_allshej/jssllv_zrdw_xfxs_allshij&order=-jssllv&xfxs={gd_id4}&limit=20&day=[2020-01-01,2020-10-09]&name=zrdw&full=true&zrdw=广东省统计局&Cqh=广东省",
    # "信访绩效考核_责任单位_drop_排名_及时受理率$": "http://127.0.0.1:3389/api/xf/?&full=true&transformer=@jssllv&ext=jssllv_zrdw_all_allshej/jssllv_qh_all_zrdw_allshij&order=-jssllv&limit=20&day=[2020-01-01,2020-10-09]&name=zrdw&full=true&Cqh=广州市",
    # "信访绩效考核_责任单位_排名_网信占比$": "http://127.0.0.1:3389/api/xf/?table=xf_xfjg_cd_qh_zrdw_xfxs_xfjc&full=true&transformer=@wxzb&name=xfbm&order=-wxzb&day=[2020-01-01,2020-10-09]&full=true&param_trans=zrdw_godown&param_protect=black_list(zrdw+xfxs)",

    ####################################### 辅助决策 #######################################
    # 全局业务监控-满意度-信访部门
    "全局业务监控_信访部门_参评情况$": "http://127.0.0.1:3389/api/xf/?transformer=@cplv&ext=cplv_xfbm_all_shejnums/cplv_xfbm_all_shijnums/cplv_xfbm_all_xjnums/cplv_xfbm_xfxs_shejnums/cplv_xfbm_xfxs_shijnums/cplv_xfbm_xfxs_xjnums&name=cpqk&full=true&day=[2020-01-01,2020-10-09]&xfbm=广东省信访局&bmjb=省级",
    # 默认有个xfbm的值
    "全局业务监控_信访部门_参评率$": "http://127.0.0.1:3389/api/xf/?transformer=@cplv&ext=cplv_qh_all_xfbm_shej/cplv_qh_all_xfbm_shij/cplv_qh_all_xfbm_xj/cplv_qh_xfxs_xfbm_shej/cplv_qh_xfxs_xfbm_shij/cplv_qh_xfxs_xfbm_xj&full=true&day=[2020-01-01,2020-10-09]&xfbm=广东省信访局&bmjb=省级&xfxs=",
    "全局业务监控_信访部门_评价情况$": "http://127.0.0.1:3389/api/xf/?transformer=@mylv&ext=mylv_xfbm_all_shejnums/mylv_xfbm_all_shijnums/mylv_xfbm_all_xjnums/mylv_xfbm_xfxs_shejnums/mylv_xfbm_xfxs_shijnums/mylv_xfbm_xfxs_xjnums&name=myqk&full=true&day=[2020-01-01,2020-10-09]&xfbm=广东省信访局&bmjb=省级",
    # 默认有个xfbm的值
    "全局业务监控_信访部门_满意率$": "http://127.0.0.1:3389/api/xf/?transformer=@mylv&ext=mylv_qh_all_xfbm_shej/mylv_qh_all_xfbm_shij/mylv_qh_all_xfbm_xj/mylv_qh_xfxs_xfbm_shej/mylv_qh_xfxs_xfbm_shij/mylv_qh_xfxs_xfbm_xj&full=true&day=[2020-01-01,2020-10-09]&xfbm=广东省信访局&bmjb=省级",
    # 需要传信访级别
    "全局业务监控_信访部门_满意率排名$": "http://127.0.0.1:3389/api/xf/?xfxs=&transformer=@mylv&ext=mylv_qh_all_xfbm_allshej/mylv_qh_all_xfbm_allshij/mylv_qh_xfxs_xfbm_allshej/mylv_qh_xfxs_xfbm_allshij&name=qh&order=-mylv&day=[2020-01-01,2020-10-10]&xfbm=广东省信访局&bmjb=省级&param_trans=qh_godown&limit=10",

    # 全局业务监控-满意度-责任单位
    "全局业务监控_责任单位_参评情况$": "http://127.0.0.1:3389/api/xf/?transformer=@cplv&ext=cplv_zrdw_all_shejnums/cplv_zrdw_all_shijnums/cplv_zrdw_all_xjnums/cplv_zrdw_xfxs_shejnums/cplv_zrdw_xfxs_shijnums/cplv_zrdw_xfxs_xjnums&name=cpqk&full=true&day=[2020-01-01,2020-10-09]&zrdw=广东省信访局&Cqh=广东省",
    # 默认有个zrdw的值
    "全局业务监控_责任单位_参评率$": "http://127.0.0.1:3389/api/xf/?transformer=@cplv&ext=cplv_qh_all_zrdw_shej/cplv_qh_all_zrdw_shij/cplv_qh_all_zrdw_xj/cplv_qh_xfxs_zrdw_shej/cplv_qh_xfxs_zrdw_shij/cplv_qh_xfxs_zrdw_xj&full=true&day=[2020-01-01,2020-10-09]&zrdw=广东省信访局&Cqh=广东省",
    "全局业务监控_责任单位_评价情况$": "http://127.0.0.1:3389/api/xf/?transformer=@mylv&ext=mylv_zrdw_all_shejnums/mylv_zrdw_all_shijnums/mylv_zrdw_all_xjnums/mylv_zrdw_xfxs_shejnums/mylv_zrdw_xfxs_shijnums/mylv_zrdw_xfxs_xjnums&name=myqk&full=true&day=[2020-01-01,2020-10-09]&zrdw=广东省统计局&Cqh=广东省",
    # 默认有个zrdw的值
    "全局业务监控_责任单位_满意率$": "http://127.0.0.1:3389/api/xf/?transformer=@mylv&ext=mylv_qh_all_zrdw_shej/mylv_qh_all_zrdw_shij/mylv_qh_all_zrdw_xj/mylv_qh_xfxs_zrdw_shej/mylv_qh_xfxs_zrdw_shij/mylv_qh_xfxs_zrdw_xj&full=true&day=[2020-01-01,2020-10-09]&zrdw=广东省统计局&Cqh=广东省",

    # 需要传Cqh
    "全局业务监控_责任单位_满意率排名$": "http://127.0.0.1:3389/api/xf/?&xfxs=&transformer=@mylv&ext=mylv_zrdw_all_allshej/mylv_zrdw_all_allshij/mylv_zrdw_xfxs_allshej/mylv_zrdw_xfxs_allshej&day=[2020-01-01,2020-10-10]&limit=10&Cqh=广东省&name=qh&xfxs=&order=-mylv&full=true",

    # 全局业务监控-重复信访监控
    # xf_xfj_cd_xj_cfxfbz_xfjc      xf_xfj_cd_xj_xfjc
    # 这里的逻辑很奇怪，全局只有这里用到transformer=chuj（需要用总数-重件就是初件）
    "全局业务监控_重复信访监控_重件占比$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_cfxfbz_xfjc&Cqh=广东省&day=[2020-01-01,2020-11-10]&extra_index=transformer@to:chuj&main_name=重件,初件&reindex=2,1&param_trans=qh_include_sub",
    "全局业务监控_重复信访监控_四级登记机构分布$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_qh_cfxfbz_djjg_xfjc&name=djjg&value=xfjc&transformer=@groupby&Cqh=广东省&day=[2020-01-01,2020-11-10]&full=true&param_trans=qh_include_sub",

    # 矛盾分析预警预判-现状分析
    "矛盾分析预警预判_专项督办信访总量$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cy_xj_zxdbxfjc&value=zxdbxfjc&year=2020&Cqh=广东省",
    "矛盾分析预警预判_专项督办信访饼图$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cy_xj_xfxs_zxdbxfjc&name=xfxs&value=zxdbxfjc&full=true&year=2020&Cqh=广东省",
    # year参数是[now-5,now]
    "矛盾分析预警预判_专项督办信访趋势$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cy_xj_zxdbxfjc&name=year&value=zxdbxfjc&year=[now-5,now]&full=true&Cqh=广东省",
    "矛盾分析预警预判_国家专项督办信访总量$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cy_xj_gjzxdbxfjc&value=gjzxdbxfjc&full=true&year=2020&Cqh=广东省",
    "矛盾分析预警预判_国家专项督办信访饼图$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cy_xj_xfxs_gjzxdbxfjc&name=xfxs&value=gjzxdbxfjc&full=true&year=2020&Cqh=广东省",
    "矛盾分析预警预判_省内专项督办-省级$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cy_xj_xfxs_shezxdbxfjc&name=xfxs&value=shezxdbxfjc&full=true&year=2020&Cqh=广东省",
    "矛盾分析预警预判_省内专项督办-市级$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cy_xj_xfxs_shizxdbxfjc&name=xfxs&value=shizxdbxfjc&full=true&year=2020&Cqh=广东省",
    "矛盾分析预警预判_省内专项督办-县级$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cy_xj_xfxs_xzxdbxfjc&name=xfxs&value=xzxdbxfjc&full=true&year=2020&Cqh=广东省",

    # 矛盾分析预警预判-预警预测
    "矛盾分析预警预判_预警预测_预警地图$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_zxdbjxfjc&value=zxdbxfjc&day=[now-200,now]&transformer=predict(7d+p=1+d=1+q=0)&Cqh=广东省&extra_index=transformer@to:yctb(7d),transformer@to:ychb(7d),transformer@to:ycyjzt&main_name=a,b,c,d&reindex=4&param_trans=qh_godown",
    "矛盾分析预警预判_预警预测_预警状态$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_zxdbjxfjc&value=zxdbxfjc&day=[now-200,now]&transformer=predict(7d+p=1+d=1+q=0)&Cqh=广东省&extra_index=transformer@to:yctb(7d),transformer@to:ychb(7d),transformer@to:ycyjzt&main_name=未来一周,同比,环比,预警状态&reindex=4,1,2,3",
    "矛盾分析预警预判_预警预测_走势$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_zxdbjxfjc&value=zxdbxfjc&name=day&stack=day&day=[now-50,now]&extra_index=transformer@to:predict(7d+p=1+d=1+q=0);day@to:[now-200,now]&main_name=真实,预测&Cqh=广东省",

    # 自定义主题分析
    "自定义主题分析_信访量四级登记机构分布$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_zt_qh_djjg_xfjc&name=djjg&value=xfjc&transformer=@groupby&Cqh=广东省&day=[2020-01-01,2020-10-10]&full=true&param_trans=qh_include_sub",
    "自定义主题分析_信访量四级登记机构分布走势$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_zt_qh_djjg_xfjc&name=day&value=xfjc&stack=djjg&transformer=@groupby&Cqh=广东省&day=[2020-01-01,2020-10-10]&full=true&param_trans=qh_include_sub",
    "自定义主题分析_主题分析报告": "http://127.0.0.1:3389/api/xf/?gd_id=gd_zdyztfx_ztfxbg&param_trans=djjg_qhauth&zt={gd_id3}",   # 需要用到djjg的qh_auth
    # 信访总量预警
    "信访总量预警_总量预警_预警状态$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_xfjc&full=true&transformer=@yjzt&extra_index=transformer@to:@groupby,transformer@to:@tb,transformer@to:@hb&main_name=预警状态,近一周,同比,环比&day=[now-7,now]&Cqh=广东省&param_protect=black_list(day)",
    "信访总量预警_总量预警_预警地图$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_xfjc&full=true&transformer=@yjzt&day=[now-7,now]&Cqh=广东省&param_protect=black_list(day)&param_trans=qh_godown",

    ####################################### 微信端 #######################################

    "考核_信访部门_参评率$": "http://127.0.0.1:3389/api/xf/?transformer=@cplv&ext=cplv_qh_all_xfbm_shej/cplv_qh_all_xfbm_shij/cplv_qh_all_xfbm_xj/cplv_qh_xfxs_xfbm_shej/cplv_qh_xfxs_xfbm_shij/cplv_qh_xfxs_xfbm_xj&full=true&day=[2020-01-01,2020-10-09]&xfxs=",
    "考核_信访部门_参评率饼图$": "http://127.0.0.1:3389/api/xf/?transformer=@cplv&ext=cplv_xfbm_all_shejnums/cplv_xfbm_all_shijnums/cplv_xfbm_all_xjnums/cplv_xfbm_xfxs_shejnums/cplv_xfbm_xfxs_shijnums/cplv_xfbm_xfxs_xjnums&name=cpqk&full=true&day=[2020-01-01,2020-10-09]",
    "考核_信访部门_满意率$": "http://127.0.0.1:3389/api/xf/?transformer=@mylv&ext=mylv_qh_all_xfbm_shej/mylv_qh_all_xfbm_shij/mylv_qh_all_xfbm_xj/mylv_qh_xfxs_xfbm_shej/mylv_qh_xfxs_xfbm_shij/mylv_qh_xfxs_xfbm_xj&full=true&day=[2020-01-01,2020-10-09]&xfxs=",
    "考核_信访部门_满意率饼图$": "http://127.0.0.1:3389/api/xf/?transformer=@mylv&ext=mylv_xfbm_all_shejnums/mylv_xfbm_all_shijnums/mylv_xfbm_all_xjnums/mylv_xfbm_xfxs_shejnums/mylv_xfbm_xfxs_shijnums/mylv_xfbm_xfxs_xjnums&name=myqk&full=true&day=[2020-01-01,2020-10-09]",

    "考核_信访部门_及时受理率$": "http://127.0.0.1:3389/api/xf/?&full=true&transformer=@jssllv&ext=jssllv_qh_all_xfbm_shej/jssllv_qh_all_xfbm_shij/jssllv_qh_all_xfbm_xj/jssllv_qh_xfxs_xfbm_shej/jssllv_qh_xfxs_xfbm_shij/jssllv_qh_xfxs_xfbm_xj&day=[2020-01-01,2020-10-09]",
    "考核_信访部门_及时受理率饼图$": "http://127.0.0.1:3389/api/xf/?transformer=@jssllv&ext=jssllv_qh_all_xfbm_shej_nums/jssllv_qh_all_xfbm_shij_nums/jssllv_qh_all_xfbm_xj_nums/jssllv_qh_xfxs_xfbm_shej_nums/jssllv_qh_xfxs_xfbm_shij_nums/jssllv_qh_xfxs_xfbm_xj_nums&name=slqk&full=true&day=[2020-01-01,2020-10-09]",
    # 待开发
    "考核_信访部门_网信占比$": "http://127.0.0.1:3389/api/xf/?transformer=@wxzb&ext=wxzb_qh_all_xfbm_shej/wxzb_qh_all_xfbm_shij/wxzb_qh_all_xfbm_xj&full=true&day=[2020-01-01,2020-10-09]",
    # 待开发
    "考核_信访部门_网信占比饼图$": "http://127.0.0.1:3389/api/xf/?transformer=@wxzb&ext=wxzb_xfbm_shejnums/wxzb_xfbm_shijnums/wxzb_xfbm_xjnums&name=wxqk&full=true&day=[2020-01-01,2020-10-09]",

    "考核_责任单位_参评率$": "http://127.0.0.1:3389/api/xf/?transformer=@cplv&ext=cplv_qh_all_zrdw_shej/cplv_qh_all_zrdw_shij/cplv_qh_all_zrdw_xj/cplv_qh_xfxs_zrdw_shej/cplv_qh_xfxs_zrdw_shij/cplv_qh_xfxs_zrdw_xj&full=true&day=[2020-01-01,2020-10-09]&zrdw=广东省信访局&Cqh=广东省",
    "考核_责任单位_参评率饼图$": "http://127.0.0.1:3389/api/xf/?transformer=@cplv&ext=cplv_zrdw_all_shejnums/cplv_zrdw_all_shijnums/cplv_zrdw_all_xjnums/cplv_zrdw_xfxs_shejnums/cplv_zrdw_xfxs_shijnums/cplv_zrdw_xfxs_xjnums&name=cpqk&full=true&day=[2020-01-01,2020-10-09]&zrdw=广东省信访局&Cqh=广东省",
    "考核_责任单位_满意率$": "http://127.0.0.1:3389/api/xf/?transformer=@mylv&ext=mylv_qh_all_zrdw_shej/mylv_qh_all_zrdw_shij/mylv_qh_all_zrdw_xj/mylv_qh_xfxs_zrdw_shej/mylv_qh_xfxs_zrdw_shij/mylv_qh_xfxs_zrdw_xj&full=true&day=[2020-01-01,2020-10-09]&zrdw=广东省统计局&Cqh=广东省",
    "考核_责任单位_满意率饼图$": "http://127.0.0.1:3389/api/xf/?transformer=@mylv&ext=mylv_zrdw_all_shejnums/mylv_zrdw_all_shijnums/mylv_zrdw_all_xjnums/mylv_zrdw_xfxs_shejnums/mylv_zrdw_xfxs_shijnums/mylv_zrdw_xfxs_xjnums&name=myqk&full=true&day=[2020-01-01,2020-10-09]&zrdw=广东省统计局&Cqh=广东省",
    "考核_责任单位_及时受理率$": "http://127.0.0.1:3389/api/xf/?full=true&transformer=@jssllv&ext=jssllv_qh_all_zrdw_shej/jssllv_qh_all_zrdw_shij/jssllv_qh_all_zrdw_xj/jssllv_qh_xfxs_zrdw_shej/jssllv_qh_xfxs_zrdw_shij/jssllv_qh_xfxs_zrdw_xj&day=[2020-01-01,2020-10-09]&zrdw=广东省统计局&Cqh=广东省",
    "考核_责任单位_及时受理率饼图$": "http://127.0.0.1:3389/api/xf/?transformer=@jssllv&ext=jssllv_qh_all_zrdw_shej_nums/jssllv_qh_all_zrdw_shij_nums/jssllv_qh_all_zrdw_xj_nums/jssllv_qh_xfxs_zrdw_shej_nums/jssllv_qh_xfxs_zrdw_shij_nums/jssllv_qh_xfxs_zrdw_xj_nums&name=slqk&day=[2020-01-01,2020-10-09]&zrdw=广东省信访局&Cqh=广东省",
    "考核_责任单位_网信占比$": "",
    "考核_责任单位_网信占比饼图$": "",

    "运行_信访部门_工作过程监控$": "http://127.0.0.1:3389/api/xf/?table=xf_xfjg_cd_bmjb_qh_xfbm_dljc&value=dljc&transformer=@groupby&full=true&day=[2020-01-01,2020-10-09]&extra_index=table@to:xf_xfjg_cd_bmjb_qh_xfbm_dbjc;value@to:dbjc&main_name=待领,待办&Cqh=广东省&param_trans=last_day,qh_include_sub",
    "运行_信访部门_信访量走势$": "http://127.0.0.1:3389/api/xf/?table=xf_xfjg_cd_bmjb_qh_xfbm_xfjc&value=xfjc&name=day&transformer=@groupby&full=true&day=[now-30,now]&Cqh=广东省&param_trans=qh_include_sub",
    "运行_责任单位_工作过程监控$": "http://127.0.0.1:3389/api/xf/?table=xf_xfjg_cd_qh_zrdw_dljc&value=dljc&transformer=@groupby&full=true&extra_index=table@to:xf_xfjg_cd_qh_zrdw_dbjc;value@to:dbjc&main_name=待领,待办&Cqh=广东省&param_trans=last_day,qh_include_sub",
    "运行_责任单位_信访量走势$": "http://127.0.0.1:3389/api/xf/?table=xf_xfjg_cd_qh_zrdw_xfjc&value=xfjc&name=day&transformer=@groupby&full=true&day=[now-30,now]&Cqh=广东省&param_trans=qh_include_sub",

    "态势_信访量$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_xfxs_xfjc&value=xfjc&transformer=@groupby&full=true&day=[now-30,now]&Cqh=广东省&param_trans=qh_include_sub",
    "态势_信访形式分布$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_xfxs_xfjc&value=xfjc&name=xfxs&transformer=@groupby&full=true&day=[now-30,now]&Cqh=广东省&param_trans=qh_include_sub",
    "态势_信访量走势$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_xfxs_xfjc&transformer=@groupby&value=xfjc&name=day&stack=xfxs&transformer=@groupby&full=true&day=[now-30,now]&Cqh=广东省&param_trans=qh_include_sub",

    "预警_预警状态$": "$信访总量预警_总量预警_预警状态$",

    "预警_信访量走势$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_xfjc&transformer=@groupby&value=xfjc&name=day&full=true&day=[now-30,now]&Cqh=广东省&param_trans=qh_include_sub",

    # 公共接口
    # 部门索引弹窗
    "公共_部门索引弹窗$": "http://39.107.240.28:3390/api/xf/?table=search_xfbm_jb&name=xfbm_alpha&value=xfbm&transformer=@groupby&jb=2&full=none&param_trans=xfbmsearch_qhauth",
    "公共_单位索引弹窗$": "http://39.107.240.28:3390/api/xf/xf/?table=search_qh_zrdw_jb&name=qh_alpha&value=qh&transformer=@groupby&jb=1&full=none&param_trans=zrdwsearch_qhauth",
    "公共_单位索引弹窗_责任单位$": "http://39.107.240.28:3390/api/xf/xf/?table=search_qh_zrdw_jb&value=zrdw&transformer=@groupby&jb=1&Cqh=广东省&full=none",
    "公共_区划索引弹窗$": "http://39.107.240.28:3390/api/xf/xf/?table=search_qh&value=shej_02&transformer=@groupby&full=none&param_trans=qhsearch_qhauth,addshijwhenxj",
}
