# apis分发-深圳
URL_DISPATCH_MAP = {
    ################################ 公共接口 ################################

    # "全部行业": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_ajlx_ajcnt&value=hy",
    "全部行业": {"code": 200, "msg": "success", "data": [{"value": ["全部", "发展改革", "教育", "科技创新", "工业和信息化", "公安", "民政", "司法",
                                                                "财政", "人力资源和社会保障", "规划和自然资源", "生态环境", "住房建设", "交通运输",
                                                                "水务", "商务", "文化广电旅游体育", "卫生健康", "退役军人", "应急管理", "审计",
                                                                "市场监管", "统计", "医疗保障", "金融", "城管", "气象", "档案", "民宗",
                                                                "事业单位登记", "保密", "烟草", "防空", "新闻出版", "农业农村", "海洋渔业",
                                                                "其他"]}], "table": ["jd_cf_cy_xj_hy_ajlx_ajcnt"]},
    # "全部区划": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_ajlx_ajcnt&value=xj_02",
    "全部区划": {"code": 200, "msg": "success", "data": [
        {"value": ["全部", "市辖区", "罗湖区", "福田区", "南山区", "宝安区", "龙岗区", "盐田区", "龙华区", "坪山区", "光明区", "大鹏新区", "深汕合作区"]}],
             "table": ["jd_cf_cy_xj_hy_ajlx_ajcnt"]},
    "全部法律法规": "127.0.0.1:3389/api/fz/?table=jd_fl_cy_shij_xljb_pllx_cnt_ratio&value=xljb",
    ################################ 政府立法 ################################

    "政府立法_立法计划总量":
        "127.0.0.1:3389/api/fz/?table=lf_cy_shij_dydw_cnt&value=cnt&extra_index=name@to:dydw&main_name=总量,&year=2020",
    "政府立法_档位情况":
        "127.0.0.1:3389/api/fz/?table=lf_cy_shij_dydw_cnt&name=dydw&value=cnt&year=2020",
    "政府立法_办理情况":
        "127.0.0.1:3389/api/fz/?table=lf_cy_shij_dydw_blqk_cnt&name=blqk&value=cnt&year=2020",
    # "政府立法_办理领域":
    #     "127.0.0.1:3389/api/fz/?table=无表，显示已删除",
    "政府立法_规范级别":
        "127.0.0.1:3389/api/fz/?table=lf_cy_shij_dydw_gfjb_cnt&name=gfjb&value=cnt&year=2020",
    "政府立法_公开意见征求_总次数":
        "127.0.0.1:3389/api/fz/?table=lf_cy_shij_dydw_tlcnt_cyrcnt_yjsum_yxcnt&value=tlcnt&year=2020",
    "政府立法_公开意见征求_参与意见有效":
        "127.0.0.1:3389/api/fz/?table=lf_cy_shij_dydw_tlcnt_cyrcnt_yjsum_yxcnt&value=cyrcnt&extra_index=value@to:yjsum,value@to:yxcnt&main_name=参与人数,意见总数,有效数&year=2020",
    "政府立法_公开意见征求_具体条例":
        "127.0.0.1:3389/api/fz/?table=lf_cy_shij_dydw_tl_cyrcnt_yjsum_yxcnt_wxcnt&name=tl&stack=tl&value=cyrcnt&year=2020&extra_index=value@to:yxcnt,value@to:wxcnt&main_name=总量,有效数,无效数&limit=4",

    ################################ 行政复议 ################################

    "行政复议_收案总数_总数":
        "127.0.0.1:3389/api/fz/?table=fy_cy_shij_ajzt_cnt&value=cnt&year=2020",
    "行政复议_收案总数_分类":
        "127.0.0.1:3389/api/fz/?table=fy_cy_shij_ajzt_cnt&name=ajzt&value=cnt&year=2020",
    "行政复议_全市行政复议事项统计":
        "127.0.0.1:3389/api/fz/?table=fy_cy_shij_fysx_cnt&name=fysx&value=cnt&year=2020",
    "行政复议_全市收案情况统计":
        "127.0.0.1:3389/api/fz/?table=fy_cy_shij_sqfs_cnt&name=sqfs&value=cnt&year=2020",
    "行政复议_全市立案情况统计":
        "127.0.0.1:3389/api/fz/?table=fy_cy_shij_slzt_cnt&name=slzt&value=cnt&year=2020",
    "行政复议_全市审结情况统计":
        "127.0.0.1:3389/api/fz/?table=fy_cy_shij_jalx_cnt&name=jalx&value=cnt&year=2020",
    # "行政复议_全市纠错率统计_总数":
    #     "127.0.0.1:3389/api/fz/?table=fy_cy_shij_cnt&value=cnt&year=2020",
    "行政复议_全市案件涉及领域排名":
        "127.0.0.1:3389/api/fz/?table=fy_cy_shij_gllb_cnt&name=gllb&value=cnt&year=2020",
    "行政复议_全市纠错率统计_分类":
        "127.0.0.1:3389/api/fz/?table=fy_cy_shij_jclx_cnt&name=jclx&value=cnt&year=2020",
    "行政复议_区政府":
        "127.0.0.1:3389/api/fz/?table=fy_cy_xj_ajzt_cnt&name=xj_02&stack=xj_02&ajzt=审结&value=cnt&year=2020&extra_index=ajzt@to:收案,ajzt@to:受理&main_name=审结,收案,受理",
    "行政复议_部门":
        "127.0.0.1:3389/api/fz/?table=fy_cy_shij_gllb_ajzt_cnt&name=gllb&stack=gllb&ajzt=审结&value=cnt&year=2020&extra_index=ajzt@to:收案,ajzt@to:受理&main_name=审结,收案,受理",

    ################################ 执法监督 ################################
    # 执法监督-首页 year=2020&xj_02=市辖区
    # 前端动态参数 "参数=默认值": year=2020&xj_02=市辖区
    "执法监督_首页_案件总量$": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_ajlx_cnt&year=2020&param_trans=xj2shij",
    "执法监督_首页_案件总量地图": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_ajlx_cnt&name=xj_02&year=2020&param_protect=black_list(xj_02)",
    "执法监督_首页_职权总量": "127.0.0.1:3389/api/fz/?table=jd_zq_cy_xj_zqlx_cnt&name=zqlx&year=2020&param_trans=xj2shij",
    "执法监督_首页_关联职权法律规范": "127.0.0.1:3389/api/fz/?table=jd_zq_cy_xj_xljb_cnt&name=xljb&year=2020&param_trans=xj2shij",
    "执法监督_首页_行政许可": "127.0.0.1:3389/api/fz/?table=jd_xk_cy_xj_jdlx_cnt&name=jdlx&year=2020&param_trans=xj2shij",
    "执法监督_首页_行政检查": "127.0.0.1:3389/api/fz/?table=jd_jc_cy_xj_jcxs_cnt&name=jcxs&year=2020&param_trans=xj2shij",
    "执法监督_首页_行政处罚": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_ajlx_cnt&name=ajlx&year=2020&param_trans=xj2shij",
    "执法监督_首页_行政强制": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_xj_qzlx_cnt&name=qzlx&year=2020&param_trans=xj2shij",
    # "执法监督_首页_执法要素_监督机关": "127.0.0.1:3389/api/fz/?table=jd_jdjg_cy_xj_cj_cnt&extra_index=xj_02@drop&main_name=区级,市级&year=2020",
    "执法监督_首页_执法要素_监督机关": "127.0.0.1:3389/api/fz/?table=jd_jdjg_cy_xj_cj_cnt&name=cj&year=2020&param_trans=xj2shij",
    # "执法监督_首页_执法要素_行政机关": "127.0.0.1:3389/api/fz/?table=jd_xzjg_cy_xj_cj_cnt&extra_index=xj_02@drop&main_name=区级,市级&year=2020",
    "执法监督_首页_执法要素_行政机关": "127.0.0.1:3389/api/fz/?table=jd_xzjg_cy_xj_cj_cnt&name=cj&year=2020&param_trans=xj2shij",
    # "执法监督_首页_执法要素_执法主体": "127.0.0.1:3389/api/fz/?table=jd_zfzt_cy_xj_cj_cnt&extra_index=xj_02@drop&main_name=区级,市级&year=2020",
    "执法监督_首页_执法要素_执法主体": "127.0.0.1:3389/api/fz/?table=jd_zfzt_cy_xj_cj_cnt&name=cj&year=2020&param_trans=xj2shij",
    "执法监督_首页_执法要素_执法人员": "127.0.0.1:3389/api/fz/?table=jd_zfry_cy_xj_ryxz_cnt&name=ryxz&year=2020&param_trans=xj2shij",
    # "执法监督_首页_执法要素_监督人员": "127.0.0.1:3389/api/fz/?table=jd_jdry_cy_xj_cj_cnt&extra_index=xj_02@to:drop&main_name=区级,市级&year=2020",
    "执法监督_首页_执法要素_监督人员": "127.0.0.1:3389/api/fz/?table=jd_jdry_cy_xj_cj_cnt&name=cj&year=2020&param_trans=xj2shij",

    ################################ 执法监督 ################################
    # 执法监督-预警监控 year=2020&xj_02=市辖区
    "执法监督_预警监控_预警案件总量_总量": "127.0.0.1:3389/api/fz/?table=jd_yj_cy_shij_yjlx_yjdj_cnt&year=2020",
    "执法监督_预警监控_预警案件总量_分类": "127.0.0.1:3389/api/fz/?table=jd_yj_cy_shij_yjlx_yjdj_cnt&name=yjlx&stack=yjdj&year=2020",
    # "执法监督_预警监控_预警案件总量":"127.0.0.1:3389/api/fz/?table=jd_yj_cy_shij_yjlx_yjdj_cnt&value=cnt&transformer=@groupby&year=2020",
    "执法监督_预警监控_案件趋势": "127.0.0.1:3389/api/fz/?table=jd_yj_cm_shij_yjdj_cnt&name=month&value=cnt&stack=yjdj&transformer=@groupby&year=2020",
    # "备注1": "表jd_yj_cy_shij_ajlx_cnt中的ajlx与图不对应",
    "执法监督_预警监控_案件种类占比": "127.0.0.1:3389/api/fz/?table=jd_yj_cy_shij_ajzl_ratio&name=ajzl&value=ratio&year=2020",
    # "备注2": "表jd_yj_cy_shij_bm_cnt中的bm为数字，cnt为null",
    "执法监督_预警监控_各部门案件量": "127.0.0.1:3389/api/fz/?table=jd_yj_cy_shij_bm_cnt&name=bm&value=cnt&year=2020",
    "执法监督_预警监控_预警状态总量": "127.0.0.1:3389/api/fz/?table=jd_yj_cd_yjrq_yjdz_yjdj_yjzq_cnt&name=yjdj&value=cnt&transformer=@groupby&param_trans=year2day",
    # "执法监督_预警监控_预警详情": "127.0.0.1:3389/api/fz/?table=jd_yj_cd_yjrq_yjdz_yjdj_cnt&value=yjrq&extra_index=value@to:yjdz,value@to:yjdj&main_name=预警时间,预警地址,预警等级",
    # "备注3": "表jd_yj_cy_shij_yjlx_ratio中的yjlx与图中不符",
    "执法监督_预警监控_预警占比": "127.0.0.1:3389/api/fz/?table=jd_yj_cy_shij_yjlx_ratio&name=yjlx&value=ratio&year=2020",
    "执法监督_预警监控_占比情况": {'code': 200, 'msg': 'success',
                       'data': [{'name': '预警', 'value': 2132}, {'name': '正常', 'value': 7982},
                                ]},
    "执法监督_预警监控_预警状态占比": "127.0.0.1:3389/api/fz/?table=jd_yj_cy_shij_yjdj_ratio&name=yjdj&value=ratio&year=2020",

    # 执法监督-行政处罚 year=2020&is_ga=true/false
    # 前端动态参数 "参数=默认值": year=2020&is_ga=true/false 【含公安传is_ga=true不含公安传is_ga=false】
    # 左侧固定
    "执法监督_行政处罚_案件量_处罚职权总数": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_zqcnt_lxratio&value=zqcnt&year=2020",
    # "执法监督_行政处罚_案件量_处罚案件总数": {'code': 200, 'msg': 'success',
    #                          'data': [{'name': '总数', 'value': 139784}, {'name': '一般', 'value': 133605},
    #                                   {'name': '简易', 'value': 6179}, {'name': '同比', 'value': 1.7005},
    #                                   {'name': '环比', 'value': 0.0927}]},
    # "执法监督_行政处罚_案件量_处罚案件总数": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_ajlx_cnt&value=cnt&extra_index=ajlx@to:一般案件,ajlx@to:简易案件,table@to:jd_cf_cy_shij_ajlx_yratio_mratio;value@to:yratio,table@to:jd_cf_cy_shij_ajlx_yratio_mratio;value@to:mratio&main_name=总数,一般,简易,同比,环比&year=2020",
    "执法监督_行政处罚_案件量_处罚案件总数": "127.0.0.1:3389/api/fz/?table=jd_cf_cm_shij_ajlx_yratio_mratio&value=yratio&extra_index=value@to:mratio,table@to:jd_cf_cy_shij_ajlx_cnt;ajlx@to:一般案件;month@drop;value@to:cnt,table@to:jd_cf_cy_shij_ajlx_cnt;ajlx@to:简易案件;month@drop;value@to:cnt,table@to:jd_cf_cy_shij_ajlx_cnt;month@drop;value@to:cnt&reindex=5,3,4,1,2&main_name=同比,环比,一般,简易,总数&year=2020",
    "执法监督_行政处罚_案件量_处罚职权履行率": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_zqcnt_lxratio&year=2020",
    # 变化
    "执法监督_行政处罚_案件量_全行业行政处罚案件量分析_drop": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_hy_ajlx_ajcnt&name=hy&stack=ajlx&year=2020",
    "执法监督_行政处罚_案件量_全行业行政处罚案件量分析_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_ajlx_ajcnt&name=xj_02&stack=ajlx&year=2020&hy={gd_id5}",
    "执法监督_行政处罚_案件量_全市区行政处罚案件量分析_drop": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_ajlx_ajcnt&name=xj_02&stack=ajlx&year=2020",
    "执法监督_行政处罚_案件量_全市区行政处罚案件量分析_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_ajlx_ajcnt&name=hy&stack=ajlx&year=2020&xj_02={gd_id5}",
    "执法监督_行政处罚_案件量_办理环节案件量分析": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_hy_bahj_ajcnt&name=bahj&year=2020",
    "执法监督_行政处罚_案件量_处罚案件办结类型分析": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_hy_jalx_ajcnt&name=jalx&year=2020",
    "执法监督_行政处罚_案件量_全措施分析": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_hy_cslx_ajcnt&name=cslx&year=2020",
    "执法监督_行政处罚_案件量_全行业处罚案件执行类型_drop": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_hy_zxlx_ajcnt&name=hy&stack=zxlx&year=2020",
    # 缺少总撤案量
    "执法监督_行政处罚_案件量_全行业处罚案件执行类型_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_zxlx_ajcnt&name=xj_02&stack=zxlx&year=2020&hy={gd_id5}",
    # 缺少总撤案量
    "执法监督_行政处罚_案件量_全市区处罚案件执行类型_drop": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_zxlx_ajcnt&name=xj_02&stack=zxlx&year=2020",
    # 缺少总撤案量
    "执法监督_行政处罚_案件量_全市区处罚案件执行类型_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_zxlx_ajcnt&name=hy&stack=zxlx&year=2020&xj_02={gd_id5}",
    # 缺少总撤案量
    "执法监督_行政处罚_案件量_行政处罚案件量月趋势分析": "127.0.0.1:3389/api/fz/?table=jd_cf_cm_shij_hy_ajlx_ajcnt&name=month&year=2020",
    "执法监督_行政处罚_案件量_处罚案件执行类型月趋势分析_半年": "127.0.0.1:3389/api/fz/?table=jd_cf_cm_shij_hy_zxlx_ajcnt&name=month&stack=zxlx&year=2020",
    "执法监督_行政处罚_案件量_处罚案件执行类型月趋势分析_季度": "127.0.0.1:3389/api/fz/?table=jd_cf_cm_shij_hy_zxlx_ajcnt&name=month&stack=zxlx&year=2020",
    "执法监督_行政处罚_案件量_处罚案件执行类型月趋势分析_月度": "127.0.0.1:3389/api/fz/?table=jd_cf_cm_shij_hy_zxlx_ajcnt&name=month&stack=zxlx&year=2020",
    # 缺少总撤案量
    "执法监督_行政处罚_案件量_行政处罚案件来源分析": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_hy_ajly_ajcnt&name=ajly&year=2020",
    "执法监督_行政处罚_案件量_行政处罚对象类型分析$": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_hy_dxlx1_ajcnt&name=dxlx1&year=2020",
    # "执法监督_行政处罚_案件量_行政处罚对象类型分析_个体工商户": {'code': 200, 'msg': 'success',  # 个体工商户怎么筛选
    #                                    'data': [{'name': '个体工商户', 'value': 70}, {'name': '自然人', 'value': 50703},
    #                                             {'name': '法人', 'value': 72587}, {'name': '其他组织', 'value': 9717}]},
    "执法监督_行政处罚_案件量_行政处罚对象类型分析_个体工商户": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_hy_dxlx2_ajcnt&name=dxlx2&year=2020",
    # "执法监督_行政处罚_案件量_历年行政处罚案件量分析": {'code': 200, 'msg': 'success',
    #                               "map": {"value_g0_1": "总量", "value_g0_2": "一般案件", "value_g0_3": "简易案件"},
    #                               'data': [{'name': 2017, 'value_g0_1': 123, 'value_g0_2': 93, 'value_g0_3': 30},
    #                                        {'name': 2018, 'value_g0_1': 123, 'value_g0_2': 93, 'value_g0_3': 30},
    #                                        {'name': 2019, 'value_g0_1': 123, 'value_g0_2': 93, 'value_g0_3': 30},
    #                                        {'name': 2020, 'value_g0_1': 123, 'value_g0_2': 93, 'value_g0_3': 30}]},
    # "执法监督_行政处罚_案件量_历年行政处罚案件量分析": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_ajlx_ajcnt&name=year&stack=year&extra_index=stack@to:ajlx&main_name=总量:bar,一般案件:line,简易案件:line",
    "执法监督_行政处罚_案件量_历年行政处罚案件量分析": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_ajlx_ajcnt&name=year&stack=year&extra_index=stack@to:ajlx&main_name=总量,一般案件,简易案件",
    # 执法监督_行政处罚_金额 year=2020&is_ga=true/false
    # 左侧固定
    "执法监督_行政处罚_金额_行政处罚金额月趋势分析_月度": "127.0.0.1:3389/api/fz/?table=jd_cf_cm_shij_hy_ajlx_amt&name=month&year=2020",
    "执法监督_行政处罚_金额_行政处罚金额月趋势分析_季度": "127.0.0.1:3389/api/fz/?table=jd_cf_cm_shij_hy_ajlx_amt&name=month&year=2020",
    "执法监督_行政处罚_金额_行政处罚金额月趋势分析_半年": "127.0.0.1:3389/api/fz/?table=jd_cf_cm_shij_hy_ajlx_amt&name=month&year=2020",
    "执法监督_行政处罚_金额_全行业行政处罚金额分析_drop": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_hy_ajlx_amt&name=hy&year=2020",
    "执法监督_行政处罚_金额_全行业行政处罚金额分析_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_ajlx_amt&name=xj_02&year=2020&hy={gd_id5}",
    "执法监督_行政处罚_金额_全市区行政处罚金额分析_drop": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_ajlx_amt&name=xj_02&year=2020",
    "执法监督_行政处罚_金额_全市区行政处罚金额分析_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_ajlx_amt&name=hy&year=2020&xj_02={gd_id5}",
    # "执法监督_行政处罚_金额_历年行政处罚金额": {'code': 200, 'msg': 'success',
    #                           "map": {"value_g0_1": "总量", "value_g0_2": "一般案件", "value_g0_3": "简易案件"},
    #                           'data': [{'name': 2017, 'value_g0_1': 12300, 'value_g0_2': 9300, 'value_g0_3': 3000},
    #                                    {'name': 2018, 'value_g0_1': 12300, 'value_g0_2': 9300, 'value_g0_3': 3000},
    #                                    {'name': 2019, 'value_g0_1': 12300, 'value_g0_2': 9300, 'value_g0_3': 3000},
    #                                    {'name': 2020, 'value_g0_1': 12300, 'value_g0_2': 9300, 'value_g0_3': 3000}]},
    # "执法监督_行政处罚_金额_历年行政处罚金额": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_ajlx_amt&name=year&stack=year&extra_index=stack@to:ajlx&main_name=总量:bar,一般案件:line,简易案件:line",
    "执法监督_行政处罚_金额_历年行政处罚金额": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_ajlx_amt&name=year&stack=year&extra_index=stack@to:ajlx&main_name=总量,一般案件,简易案件",
    # 执法监督_行政处罚_处罚量 year=2020&is_ga=true/false
    # 左侧固定
    "执法监督_行政处罚_处罚量_全行业人均处罚量分析": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_hy_ajlx_avg&name=hy&stack=hy&extra_index=stack@to:ajlx&main_name=总量,一般案件,简易案件&year=2020",
    "执法监督_行政处罚_处罚量_全市区人均处罚量分析": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_ajlx_avg&name=xj_02&stack=xj_02&extra_index=stack@to:ajlx&main_name=总量,一般案件,简易案件&year=2020",
    # "执法监督_行政处罚_处罚量_历年人均处罚量分析": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_ajlx_avg&name=year&stack=year&extra_index=stack@to:ajlx&main_name=总量,一般案件,简易案件",
    "执法监督_行政处罚_处罚量_历年人均处罚量分析": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_ajlx_avg&name=year&stack=ajlx&main_name=总量,一般案件,简易案件",
    # "执法监督_行政处罚_处罚量_一线执法率": {'code': 200, 'msg': 'success',
    #                         "map": {"value_g0_1": "编制人员", "value_g0_2": "办案人员", "value_g0_3": "持证人员",
    #                                 "value_g0_4": "职权数", "value_g0_5": "一线执法率"},
    #                         'data': [{'name': '发改', 'value_g0_1': 12300, 'value_g0_2': 9300, 'value_g0_3': 1,
    #                                   'value_g0_4': 1, 'value_g0_5': 1},
    #                                  {'name': '教育', 'value_g0_1': 12300, 'value_g0_2': 9300, 'value_g0_3': 1,
    #                                   'value_g0_4': 1, 'value_g0_5': 1},
    #                                  {'name': '科创', 'value_g0_1': 12300, 'value_g0_2': 9300, 'value_g0_3': 1,
    #                                   'value_g0_4': 1, 'value_g0_5': 1},
    #                                  {'name': '文体', 'value_g0_1': 12300, 'value_g0_2': 9300, 'value_g0_3': 1,
    #                                   'value_g0_4': 1, 'value_g0_5': 1}]},
    "执法监督_行政处罚_处罚量_一线执法率":"127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_hy_bzcnt_bacnt_czcnt_zqcnt_ratio&name=hy&stack=hy&value=bzcnt&extra_index=value@to:bacnt,value@to:czcnt,value@to:zqcnt,value@to:ratio&main_name=编制人员,办案人员,持证人员,职权数,一线执法率",
    # 执法监督_行政处罚_职权履行率 year=2020&is_ga=true/false
    # 左侧固定
    # "执法监督_行政处罚_权职履行率_全行业职权履行情况分析_drop": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_hy_zqcnt_lxcnt_lxjhratio_lxratio&name=hy&stack=hy&value=zqcnt&extra_index=value@to:lxcnt,value@to:lxjhratio,value@to:lxratio&main_name=职权数:overlap,履行数:bar,履职均衡率:line,履行率:line&year=2020",
    "执法监督_行政处罚_权职履行率_全行业职权履行情况分析_drop": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_hy_zqcnt_lxcnt_lxjhratio_lxratio&name=hy&stack=hy&value=zqcnt&extra_index=value@to:lxcnt,value@to:lxjhratio,value@to:lxratio&main_name=职权数,履行数,履职均衡率,履行率&year=2020",
    # "执法监督_行政处罚_权职履行率_全行业职权履行情况分析_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_zqcnt_lxcnt_lxjhratio_lxratio&name=xj_02&stack=xj_02&value=zqcnt&extra_index=value@to:lxcnt,value@to:lxjhratio,value@to:lxratio&main_name=职权数:overlap,履行数:bar,履职均衡率:line,履行率:line&year=2020&hy={gd_id5}",
    "执法监督_行政处罚_权职履行率_全行业职权履行情况分析_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_zqcnt_lxcnt_lxjhratio_lxratio&name=xj_02&stack=xj_02&value=zqcnt&extra_index=value@to:lxcnt,value@to:lxjhratio,value@to:lxratio&&main_name=职权数,履行数,履职均衡率,履行率&year=2020&hy={gd_id5}",
    # "执法监督_行政处罚_权职履行率_全市区职权履行情况分析_drop": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_zqcnt_lxcnt_lxjhratio_lxratio&name=xj_02&stack=xj_02&value=zqcnt&extra_index=value@to:lxcnt,value@to:lxjhratio,value@to:lxratio&main_name=职权数:overlap,履行数:bar,履职均衡率:line,履行率:line&year=2020",
    "执法监督_行政处罚_权职履行率_全市区职权履行情况分析_drop": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_zqcnt_lxcnt_lxjhratio_lxratio&name=xj_02&stack=xj_02&value=zqcnt&extra_index=value@to:lxcnt,value@to:lxjhratio,value@to:lxratio&&main_name=职权数,履行数,履职均衡率,履行率&year=2020",
    # "执法监督_行政处罚_权职履行率_全市区职权履行情况分析_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_zqcnt_lxcnt_lxjhratio_lxratio&name=hy&stack=hy&value=zqcnt&extra_index=value@to:lxcnt,value@to:lxjhratio,value@to:lxratio&main_name=职权数:overlap,履行数:bar,履职均衡率:line,履行率:line&year=2020&xj_02={gd_id5}",
    "执法监督_行政处罚_权职履行率_全市区职权履行情况分析_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_zqcnt_lxcnt_lxjhratio_lxratio&name=hy&stack=hy&value=zqcnt&extra_index=value@to:lxcnt,value@to:lxjhratio,value@to:lxratio&&main_name=职权数,履行数,履职均衡率,履行率&year=2020&xj_02={gd_id5}",
    # "执法监督_行政处罚_权职履行率_历年职权履行情况": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_zqcnt_lxcnt_lxjhratio_lxratio&name=year&stack=year&value=zqcnt&extra_index=value@to:lxcnt,value@to:lxjhratio,value@to:lxratio&main_name=职权数:overlap,履行数:bar,履职均衡率:line,履行率:line",
    "执法监督_行政处罚_权职履行率_历年职权履行情况": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_zqcnt_lxcnt_lxjhratio_lxratio&name=year&stack=year&value=zqcnt&extra_index=value@to:lxcnt,value@to:lxjhratio,value@to:lxratio&main_name=&main_name=职权数,履行数,履职均衡率,履行率",

    # 执法监督_行政处罚_案件移送 year=2020&is_ga=true/false
    # 左侧固定
    "执法监督_行政处罚_案件移送_移送案件数月趋势分析_月度": "127.0.0.1:3389/api/fz/?table=jd_cf_cm_shij_hy_ajyscnt&name=month&year=2020",
    "执法监督_行政处罚_案件移送_移送案件数月趋势分析_季度": "127.0.0.1:3389/api/fz/?table=jd_cf_cm_shij_hy_ajyscnt&name=hy&stack=hy&value=zqcnt&year=2020",
    "执法监督_行政处罚_案件移送_移送案件数月趋势分析_半年": "127.0.0.1:3389/api/fz/?table=jd_cf_cm_shij_hy_ajyscnt&name=hy&stack=hy&value=zqcnt&year=2020",
    "执法监督_行政处罚_案件移送_全行业移送案件数_drop": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_hy_ajyscnt&name=hy&year=2020",
    "执法监督_行政处罚_案件移送_全行业移送案件数_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_ajyscnt&name=xj_02&year=2020&hy={gd_id5}",
    "执法监督_行政处罚_案件移送_全市区移送案件数_drop": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_ajyscnt&name=xj_02&year=2020",
    "执法监督_行政处罚_案件移送_全市区移送案件数_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_ajyscnt&name=hy&year=2020&xj_02={gd_id5}",
    "执法监督_行政处罚_案件移送_历年移送案件数": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_ajyscnt&name=year",

    # 执法监督_行政处罚_案件评查 year=2020&is_ga=true/false
    # 左侧固定
    "执法监督_行政处罚_案件评查_历年案卷评查成绩": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_hy_score&name=hy&stack=year",
    "执法监督_行政处罚_案件评查_全行业案卷评查执行率_drop": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_hy_ypcnt_sjcnt_zxratio&name=hy&stack=hy&value=zxratio&extra_index=value@to:ypcnt,value@to:sjcnt&main_name=执行率,应评查数,实际评查数&year=2020",
    # 表中缺少督察案卷数和案卷合格数
    "执法监督_行政处罚_案件评查_全行业案卷评查执行率_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_ypcnt_sjcnt_zxratio&name=xj_02&stack=xj_02&value=zxratio&extra_index=value@to:ypcnt,value@to:sjcnt&main_name=执行率,应评查数,实际评查数&year=2020&hy={gd_id5}",
    # 表中缺少督察案卷数和案卷合格数
    "执法监督_行政处罚_案件评查_全市区案卷评查执行率_drop": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_ypcnt_sjcnt_zxratio&name=xj_02&stack=xj_02&value=zxratio&extra_index=value@to:ypcnt,value@to:sjcnt&main_name=执行率,应评查数,实际评查数&year=2020",
    # 表中缺少督察案卷数和案卷合格数
    "执法监督_行政处罚_案件评查_全市区案卷评查执行率_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_ypcnt_sjcnt_zxratio&name=hy&stack=hy&value=zxratio&extra_index=value@to:ypcnt,value@to:sjcnt&main_name=执行率,应评查数,实际评查数&year=2020&xj_02={gd_id5}",
    # 表中缺少督察案卷数和案卷合格数
    "执法监督_行政处罚_案件评查_全行业案卷评查合格率_drop": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_hy_dccnt_hgcnt_hgratio&name=hy&stack=hy&value=hgratio&extra_index=value@to:dccnt,value@to:hgcnt&main_name=合格率,督察案卷数,案卷合格数&year=2020",
    "执法监督_行政处罚_案件评查_全行业案卷评查合格率_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_dccnt_hgcnt_hgratio&name=xj_02&stack=xj_02&value=hgratio&extra_index=value@to:dccnt,value@to:hgcnt&main_name=合格率,督察案卷数,案卷合格数&year=2020&hy={gd_id5}",
    "执法监督_行政处罚_案件评查_全市区案卷评查合格率_drop": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_dccnt_hgcnt_hgratio&name=xj_02&stack=xj_02&value=hgratio&extra_index=value@to:dccnt,value@to:hgcnt&main_name=合格率,督察案卷数,案卷合格数&year=2020",
    "执法监督_行政处罚_案件评查_全市区案卷评查合格率_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_dccnt_hgcnt_hgratio&name=hy&stack=hy&value=hgratio&extra_index=value@to:dccnt,value@to:hgcnt&main_name=合格率,督察案卷数,案卷合格数&year=2020&xj_02={gd_id5}",
    # "执法监督_行政处罚_案件评查_评查要素": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_yslx_cnt&name=yslx&year=2020",  # 待实现

    # 执法监督_行政处罚_处罚周期 year=2020&is_ga=true/false
    # 左侧固定
    # 缺延期案件和终止案件的筛选字段
    # "执法监督_行政处罚_处罚周期_处罚周期分析": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_hy_ajzl_laavg_dcavg_scavg_cfavg_jaavg&value=laavg&name=year&stack=year&extra_index=value@to:dcavg,value@to:scavg,value@to:cfavg,value@to:jaavg&main_name=立案阶段,调查取证阶段,审查决定阶段,处罚执行阶段,结案阶段",
    # "执法监督_行政处罚_处罚周期_处罚周期分析": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_hy_ajzl_laavg_dcavg_scavg_cfavg_jaavg&value=laavg&name=year&stack=year&extra_index=value@to:dcavg,value@to:scavg,value@to:cfavg,value@to:jaavg&main_name=立案阶段,调查取证阶段,审查决定阶段,处罚执行阶段,结案阶段&year=[2018,2019]",
    "执法监督_行政处罚_处罚周期_处罚周期分析": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_hy_ajzl_bahj_hjxh_avg&value=avg&name=bahj&stack=year&year=[2018,2019]",
    # "执法监督_行政处罚_处罚周期_处罚周期分析": {'code': 200, 'msg': 'success',
    #                           "map": {"value_g0_1": "立案阶段", "value_g0_2": "调查取证阶段", "value_g0_3": "审查决定阶段",
    #                                   "value_g0_4": "处罚执行阶段", "value_g0_5": "经案阶段"},
    #                           'data': [{'name': 2017, 'value_g0_1': 12300, 'value_g0_2': 9300, 'value_g0_3': 3000,
    #                                     'value_g0_4': 3000, 'value_g0_5': 3000},
    #                                    {'name': 2018, 'value_g0_1': 12300, 'value_g0_2': 9300, 'value_g0_3': 3000,
    #                                     'value_g0_4': 3000, 'value_g0_5': 3000},
    #                                    ]},

    # 执法监督_行政处罚_投诉举报分析 year=2020&is_ga=true/false
    # 左侧固定
    "执法监督_行政处罚_投诉举报分析_全行业投诉举报吻合度_drop": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_hy_ajlx_cfcnt_jbcnt_whratio&name=hy&stack=hy&value=cfcnt&extra_index=value@to:jbcnt,value@to:whratio&main_name=处罚案件,投诉举报,吻合度&year=2020",
    # 弹窗问一下萌哥
    "执法监督_行政处罚_投诉举报分析_全行业投诉举报吻合度_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_ajlx_cfcnt_jbcnt_whratio&name=xj_02&stack=xj_02&value=cfcnt&extra_index=value@to:jbcnt,value@to:whratio&main_name=处罚案件,投诉举报,吻合度&year=2020&hy={gd_id5}",
    "执法监督_行政处罚_投诉举报分析_全市区投诉举报吻合度_drop": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_ajlx_cfcnt_jbcnt_whratio&name=xj_02&stack=xj_02&value=cfcnt&extra_index=value@to:jbcnt,value@to:whratio&main_name=处罚案件,投诉举报,吻合度&year=2020",
    "执法监督_行政处罚_投诉举报分析_全市区投诉举报吻合度_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_ajlx_cfcnt_jbcnt_whratio&name=hy&stack=hy&value=cfcnt&extra_index=value@to:jbcnt,value@to:whratio&main_name=处罚案件,投诉举报,吻合度&year=2020&xj_02={gd_id5}",
    "执法监督_行政处罚_投诉举报分析_投诉举报量月趋势分析_月度": "127.0.0.1:3389/api/fz/?table=jd_cf_cm_shij_hy_jbcnt&name=month&year=2020",
    "执法监督_行政处罚_投诉举报分析_全行业投诉举报量_drop": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_hy_jbcnt&name=hy&year=2020",
    "执法监督_行政处罚_投诉举报分析_全行业投诉举报量_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_jbcnt&name=xj_02&year=2020&hy={gd_id5}",
    "执法监督_行政处罚_投诉举报分析_全市区投诉举报量_drop": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_jbcnt&name=xj_02&year=2020",
    "执法监督_行政处罚_投诉举报分析_全市区投诉举报量_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_jbcnt&name=hy&year=2020&xj_02={gd_id5}",
    "执法监督_行政处罚_投诉举报分析_历年投诉举报量": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_xj_hy_jbcnt&name=year",
    "执法监督_行政处罚_投诉举报分析_投诉举报法人类型": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_hy_dxlx1_jbcnt&name=dxlx1&year=2020",

    # 执法监督_行政强制 year=2020&is_ga=true/false
    # 左侧面板
    "执法监督_行政强制_强制职权总数": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_shij_zqcnt_lxratio&value=zqcnt&year=2020",
    # "执法监督_行政强制_强制案件总数": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_shij_qzlx_cnt&extra_index=qzlx@to:强制措施,qzlx@to:强制执行,table@to:jd_qz_cy_shij_yratio_mratio;value@to:yratio,table@to:jd_qz_cy_shij_yratio_mratio;value@to:mratio&year=2020&main_name=总数,强制措施,强制执行,同比,环比",
    "执法监督_行政强制_强制案件总数": "127.0.0.1:3389/api/fz/?table=jd_qz_cm_shij_yratio_mratio&value=yratio&extra_index=value@to:mratio,table@to:jd_qz_cy_shij_qzlx_cnt;month@drop;qzlx@to:强制措施;value@to:cnt,table@to:jd_qz_cy_shij_qzlx_cnt;month@drop;qzlx@to:强制执行;value@to:cnt,table@to:jd_qz_cy_shij_qzlx_cnt;month@drop;value@to:cnt&year=2020&reindex=5,3,4,1,2&main_name=同比,环比,强制措施,强制执行,总数",
    # "执法监督_行政强制_强制职权同环比": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_shij_yratio_mratio&value=yratio&extra_index=value@to:mratio&year=2020&main_name=同比,环比",
    "执法监督_行政强制_强制职权履行率": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_shij_zqcnt_lxratio&value=lxratio&year=2020",

    # 右侧变化
    "执法监督_行政强制_全行业行政强制案件量分析_drop": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_shij_hy_ajlx_cnt&name=hy&stack=ajlx&year=2020",
    "执法监督_行政强制_全行业行政强制案件量分析_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_xj_hy_ajlx_cnt&name=xj_02&stack=ajlx&year=2020&hy={gd_id4}",
    "执法监督_行政强制_全市区行政强制案件量分析_drop": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_xj_hy_ajlx_cnt&name=xj_02&stack=ajlx&year=2020",
    "执法监督_行政强制_全市区行政强制案件量分析_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_xj_hy_ajlx_cnt&name=hy&stack=ajlx&year=2020&xj_02={gd_id4}",

    # 执法监督_行政许可 year=2020&is_ga=true/false
    # 左侧面板
    "执法监督_行政许可_许可案件总数": "127.0.0.1:3389/api/fz/?table=jd_xk_cy_shij_jdlx_cnt&jdlx=予以许可&extra_index=jdlx@to:不予许可&main_name=予以许可,不予许可&year=2020",
    "执法监督_行政许可_全市许可职权总数": "127.0.0.1:3389/api/fz/?table=jd_xk_cy_shij_zqcnt_lxcnt_ratio&value=zqcnt&extra_index=value@to:ratio&main_name=总数,许可职权履行率&year=2020&full=true",
    # "备注7": "表jd_xk_cy_shij_zqcnt缺履行率列",
    # "执法监督_行政许可_许可职权履行率": "127.0.0.1:3389/api/fz/?table=jd_xk_cy_shij_zqcnt_ratio&year=2020",
    "执法监督_行政许可_许可行政复议结果": "127.0.0.1:3389/api/fz/?table=jd_xk_cy_shij_fycnt&value=fycnt&year=2020",
    "执法监督_行政许可_许可双公示结果": "127.0.0.1:3389/api/fz/?table=jd_xk_cy_shij_gscnt&value=gscnt&year=2020",
    # 变化
    "执法监督_行政许可_行政许可案件量_全行业行政许可案件量分析_drop": "127.0.0.1:3389/api/fz/?table=jd_xk_cy_shij_hy_ajcnt&name=hy&year=2020",
    "执法监督_行政许可_行政许可案件量_全行业行政许可案件量分析_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_xk_cy_xj_hy_ajcnt&name=xj_02&year=2020&hy={gd_id5}",
    "执法监督_行政许可_行政许可案件量_全市区行政许可案件量分析_drop": "127.0.0.1:3389/api/fz/?table=jd_xk_cy_xj_hy_ajcnt&name=xj_02&year=2020",
    "执法监督_行政许可_行政许可案件量_全市区行政许可案件量分析_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_xk_cy_xj_hy_ajcnt&name=hy&year=2020&xj_02={gd_id5}",
    "执法监督_行政许可_行政许可案件量_许可事项子事项数量分析": "127.0.0.1:3389/api/fz/?table=jd_xk_cy_shij_hy_sxcnt_zxcnt_ratio&name=hy&stack=hy&value=sxcnt&extra_index=value@to:zxcnt,value@to:ratio&main_name=事项,子事项,占比&year=2020",
    # "执法监督_行政许可_许可职权履行情况_全行业许可职权履行分析_drop": "127.0.0.1:3389/api/fz/?table=jd_xk_cy_xj_hy_zqcnt_lxcnt_lxratio_lzratio&name=hy&stack=hy&value=zqcnt&extra_index=value@to:lxcnt,value@to:lzratio,value@to:lxratio&main_name=职权数:overlap,履行数:bar,履职均衡率:line,履行率:line&year=2020",
    "执法监督_行政许可_许可职权履行情况_全行业许可职权履行分析_drop": "127.0.0.1:3389/api/fz/?table=jd_xk_cy_xj_hy_zqcnt_lxcnt_lxratio_lzratio&name=hy&stack=hy&value=zqcnt&extra_index=value@to:lxcnt,value@to:lzratio,value@to:lxratio&main_name=职权数,履行数,履职均衡率,履行率&year=2020",
    # 库里缺少字段
    "执法监督_行政许可_许可职权履行情况_全行业许可职权履行分析_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_xk_cy_xj_hy_zqcnt_lxcnt_lxratio_lzratio&name=xj_02&stack=xj_02&value=zqcnt&extra_index=value@to:lxcnt,value@to:lzratio,value@to:lxratio&main_name=职权数,履行数,履职均衡率,履行率&year=2020&hy={gd_id5}",
    # # 库里缺少字段
    # "执法监督_行政许可_许可职权履行情况_历年许可职权履行分析": {'code': 200, 'msg': 'success',
    #                                   "map": {"value_g0_1": "总量", "value_g0_2": "履行数", "value_g0_3": "履行率",
    #                                           "value_g0_4": "履行均衡率"},
    #                                   'data': [{'name': 2017, 'value_g0_1': 12300, 'value_g0_2': 9300, 'value_g0_3': 1,
    #                                             'value_g0_4': 1},
    #                                            {'name': 2018, 'value_g0_1': 12300, 'value_g0_2': 9300, 'value_g0_3': 1,
    #                                             'value_g0_4': 1},
    #                                            {'name': 2019, 'value_g0_1': 12300, 'value_g0_2': 9300, 'value_g0_3': 1,
    #                                             'value_g0_4': 1},
    #                                            {'name': 2020, 'value_g0_1': 12300, 'value_g0_2': 9300, 'value_g0_3': 1,
    #                                             'value_g0_4': 1},
    #                                            ]},
    "执法监督_行政许可_许可职权履行情况_历年许可职权履行分析": "127.0.0.1:3389/api/fz/?table=jd_xk_cy_xj_hy_zqcnt_lxcnt_lxratio_lzratio&name=year&stack=year&value=zqcnt&extra_index=value@to:lxcnt,value@to:lzratio,value@to:lxratio&main_name=职权数,履行数,履职均衡率,履行率",
    # 执法监督_行政检查 year=2020&is_ga=true/false
    # 左侧面板
    "执法监督_行政检查_检查案件总数": "127.0.0.1:3389/api/fz/?table=jd_jc_cy_shij_jcxs_cnt",
    "执法监督_行政检查_检查案件同环比": "127.0.0.1:3389/api/fz/?table=jd_jc_cm_shij_yratio_mratio&value=yratio&extra_index=value@to:mratio&year=2020&month=1&main_name=同比,环比",
    "备注8": "表jd_jc_cy_shij_cj_avg中cj与图中类型不符合",
    "执法监督_行政检查_人均检查量$": "127.0.0.1:3389/api/fz/?table=jd_jc_cy_shij_cj_avg&value=avg&extra_index=cj@to:市级,cj@to:区级&main_name=全市,市级,区级&year=2020",
    "备注9": "表jd_jc_cy_shij_lxratio没有检查职权的总数和履行数",
    "执法监督_行政检查_检查职权履行率": "127.0.0.1:3389/api/fz/?table=jd_jc_cy_shij_zqcnt_lxcnt_lxratio&value=zqcnt&extra_index=value@to:lxcnt&main_name=总数,履行数&year=2020",
    # 变化
    "执法监督_行政检查_行政检查案件量_全行业检查量分析_drop": "127.0.0.1:3389/api/fz/?table=jd_jc_cy_shij_hy_cnt&name=hy&year=2020",
    "执法监督_行政检查_行政检查案件量_全行业检查量分析_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_jc_cy_xj_hy_cnt&name=xj_02&year=2020&hy={gd_id5}",
    "执法监督_行政检查_行政检查案件量_全市区检查量分析_drop": "127.0.0.1:3389/api/fz/?table=jd_jc_cy_xj_hy_cnt&name=xj_02&year=2020",
    "执法监督_行政检查_行政检查案件量_全市区检查量分析_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_jc_cy_xj_hy_cnt&name=hy&year=2020&xj_02={gd_id5}",
    "执法监督_行政检查_行政检查案件量_检查量月趋势分析_月度": "127.0.0.1:3389/api/fz/?table=jd_jc_cm_shij_hy_cnt&name=month&year=2020",
    # 没有cnt字段

    "执法监督_行政检查_行政检查案件量_全行业检查种类统计_drop": "127.0.0.1:3389/api/fz/?table=jd_jc_cy_shij_hy_jczl_cnt&name=hy&year=2020",
    "执法监督_行政检查_行政检查案件量_全行业检查种类统计_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_jc_cy_xj_hy_jczl_cnt&name=xj_02&year=2020&hy={gd_id5}",
    "执法监督_行政检查_行政检查案件量_全市区检查种类统计_drop": "127.0.0.1:3389/api/fz/?table=jd_jc_cy_xj_hy_jczl_cnt&name=xj_02&year=2020",
    "执法监督_行政检查_行政检查案件量_全市区检查种类统计_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_jc_cy_xj_hy_jczl_cnt&name=hy&year=2020&xj_02={gd_id5}",
    "执法监督_行政检查_行政检查案件量_历年检查量": "127.0.0.1:3389/api/fz/?table=jd_jc_cy_xj_hy_cnt&name=year",

    "执法监督_行政检查_人均检查量_全行业人均检查量分析_drop": "127.0.0.1:3389/api/fz/?table=jd_jc_cy_shij_hy_avg&name=hy&year=2020",
    "执法监督_行政检查_人均检查量_全行业人均检查量分析_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_jc_cy_xj_hy_avg&name=xj_02&year=2020&hy={gd_id5}",
    "执法监督_行政检查_人均检查量_全市区人均检查量分析_drop": "127.0.0.1:3389/api/fz/?table=jd_jc_cy_xj_hy_avg&name=xj_02&year=2020",
    "执法监督_行政检查_人均检查量_全市区人均检查量分析_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_jc_cy_xj_hy_avg&name=hy&year=2020&xj_02={gd_id5}",
    "执法监督_行政检查_人均检查量_行政检查参与率": "127.0.0.1:3389/api/fz/?table=jd_jc_cy_shij_hy_bzcnt_bacnt_ratio&name=hy&stack=hy&value=bzcnt&extra_index=value@to:bacnt,value@to:ratio&main_name=编制人员,办案人员,参与率&year=2020",
    # 缺少hy字段

    # "执法监督_行政检查_检查综合分析_检查类型占比": "127.0.0.1:3389/api/fz/?table=jd_jc_cy_shij_hy_jcxs_cnt_ratio&value=cnt&extra_index=stack@to:jcxs&main_name=总量,&year=2020",
    "执法监督_行政检查_检查综合分析_检查类型占比": "127.0.0.1:3389/api/fz/?table=jd_jc_cy_shij_hy_jcxs_cnt_ratio&value=cnt&name=jcxs&year=2020",
    # 缺少总量的表

    # 执法监督_行政诉讼 year=2020&is_ga=true/false
    # 左侧面板
    "备注10": "jd_ss_cy_shij_sjlx_ratio中sjlx与图中不符，且缺少应诉案件量总数值",
    "执法监督_行政诉讼_一审情况分析": "127.0.0.1:3389/api/fz/?table=jd_ss_cy_shij_sjlx_cnt_ratio&value=cnt&extra_index=sjlx@to:判决,sjlx@to:调解,sjlx@to:裁定&main_name=总数,判决,调解,裁定",
    "备注11": "jd_ss_cy_shij_dwlx_cnt中dwlx的值有问题（两个单位名字放一起了）？",
    "执法监督_行政诉讼_工作单位": "127.0.0.1:3389/api/fz/?table=jd_ss_cy_shij_dwlx_cnt&name=dwlx&value=cnt&year=2020",
    # 变化
    "执法监督_行政诉讼_行政诉讼案件量_全行业行政诉讼案件量分析_drop": "127.0.0.1:3389/api/fz/?table=jd_ss_cy_shij_hy_ajlx_cnt&name=hy&stack=ajlx&year=2020",
    "执法监督_行政诉讼_行政诉讼案件量_全行业行政诉讼案件量分析_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_ss_cy_xj_hy_ajlx_cnt&name=xj_02&stack=ajlx&year=2020&hy={gd_id5}",
    "执法监督_行政诉讼_行政诉讼案件量_全市区行政诉讼案件量分析_drop": "127.0.0.1:3389/api/fz/?table=jd_ss_cy_xj_hy_ajlx_cnt&name=xj_02&stack=ajlx&year=2020",
    "执法监督_行政诉讼_行政诉讼案件量_全市区行政诉讼案件量分析_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_ss_cy_xj_hy_ajlx_cnt&name=hy&stack=ajlx&year=2020&xj_02={gd_id5}",

    # 执法监督_机构人员 year=2020&is_ga=true/false
    # 左侧面板
    "执法监督_机构人员_行业总数":
        "127.0.0.1:3389/api/fz/?table=jd_ry_cy_shij_hy_hycnt&value=hycnt&year=2020",
    "执法监督_机构人员_执法人员总数":
        "127.0.0.1:3389/api/fz/?table=jd_ry_cy_shij_hy_rycnt&value=rycnt&year=2020",
    "执法监督_机构人员_工作单位":
        "127.0.0.1:3389/api/fz/?table=jd_ry_cy_shij_hy_cj_dwcnt&extra_index=cj@to:市级,cj@to:区级,cj@to:街道&main_name=总数,市级,区级,街道&year=2020",
    # "执法监督_机构人员_工作单位_分类":
    #     "127.0.0.1:3389/api/fz/?table=jd_ry_cy_shij_hy_cj_dwcnt&name=cj&year=2020",
    # "备注4": "工作单位和执法主体是一个表？",
    "执法监督_机构人员_执法主体":
        "127.0.0.1:3389/api/fz/?table=jd_ry_cy_shij_hy_cj_ztcnt&extra_index=cj@to:市级,cj@to:区级,cj@to:街道&main_name=总数,市级,区级,街道&year=2020",
    # "执法监督_机构人员_执法主体_分类":
    #     "127.0.0.1:3389/api/fz/?table=jd_ry_cy_shij_hy_cj_ztcnt&name=cj&year=2020",

    "执法监督_机构人员_执法人员分析_执法人员数量":
        "127.0.0.1:3389/api/fz/?table=jd_ry_cy_xj_hy_nld_cnt&value=cnt&year=2020",
    "执法监督_机构人员_执法人员分析_年龄阶段":
        "127.0.0.1:3389/api/fz/?table=jd_ry_cy_xj_hy_nld_cnt&name=nld&value=cnt&year=2020",
    "执法监督_机构人员_执法人员分析_编制类型":
        "127.0.0.1:3389/api/fz/?table=jd_ry_cy_xj_hy_bzlx_cnt&name=bzlx&value=cnt&year=2020",
    "执法监督_机构人员_执法人员分析_各区县":
        "127.0.0.1:3389/api/fz/?table=jd_ry_cy_xj_hy_cnt&name=xj_02&value=cnt&year=2020",
    "执法监督_机构人员_执法人员分析_性别":
        "127.0.0.1:3389/api/fz/?table=jd_ry_cy_xj_hy_xb_cnt&name=xb&value=cnt&transformer=@zb&year=2020",
    "执法监督_机构人员_执法人员分析_职级":
        "127.0.0.1:3389/api/fz/?table=jd_ry_cy_xj_hy_zj_cnt&name=zj&value=cnt&year=2020&full=true",
    "执法监督_机构人员_执法人员分析_学历":
        "127.0.0.1:3389/api/fz/?table=jd_ry_cy_xj_hy_xl_cnt&name=xl&value=cnt&year=2020",
    "执法监督_机构人员_执法人员分析_党员":
        "127.0.0.1:3389/api/fz/?table=jd_ry_cy_xj_hy_zzmm_cnt&name=zzmm&value=cnt&year=2020&transformer=@zb",
    "执法监督_机构人员_执法对象分析":
        "127.0.0.1:3389/api/fz/?table=jd_ry_cy_xj_hy_nld_cnt&name=hy",
    "执法监督_机构人员_执法证件类型分析":
        "127.0.0.1:3389/api/fz/?table=jd_ry_cy_xj_hy_lxdj_sllx_cnt&name=sllx,lxdj&value=cnt&year=2020",

    # 执法监督_法律规范 year=2020&is_ga=true/false
    # 左侧面板
    "执法监督_法律规范_职权关联法律总数": "127.0.0.1:3389/api/fz/?table=jd_fl_cy_shij_cnt&value=cnt&year=2020",
    "执法监督_法律规范_涉案法律总数": "127.0.0.1:3389/api/fz/?table=jd_fl_cy_shij_xljb_pllx_cnt_ratio&value=cnt&year=2020",
    # "备注12": "jd_fl_cy_shij_xljb_ajlx_cnt，没有可判断未涉案、高频、低频的列",
    "执法监督_法律规范_未涉案法律总数": "127.0.0.1:3389/api/fz/?table=jd_fl_cy_shij_xljb_pllx_cnt_ratio&value=cnt&year=2020&pllx=未涉案",
    "执法监督_法律规范_高频触发法律总数": "127.0.0.1:3389/api/fz/?table=jd_fl_cy_shij_xljb_pllx_cnt_ratio&value=cnt&year=2020&pllx=高频",
    "执法监督_法律规范_低频触发法律总数": "127.0.0.1:3389/api/fz/?table=jd_fl_cy_shij_xljb_pllx_cnt_ratio&value=cnt&year=2020&pllx=低频",
    # 变化
    # 没有可判断未涉案、高频、低频的列
    "执法监督_法律规范_涉案法律规范分析": "127.0.0.1:3389/api/fz/?table=jd_fl_cy_shij_xljb_pllx_cnt_ratio&name=xljb&stack=pllx&value=cnt&transformer=@zb(cnt/xljb)&year=2020",
    # 字段取值不对
    "执法监督_法律规范_法律分类占比统计": "127.0.0.1:3389/api/fz/?table=jd_fl_cy_shij_hy_xljb_cnt_lxcnt_lxratio&name=xljb&value=cnt&year=2020",
    # "执法监督_法律规范_全行业法律法规履行情况_drop": "127.0.0.1:3389/api/fz/?table=jd_fl_cy_shij_hy_xljb_cnt_lxcnt_lxratio&name=hy&stack=hy&value=cnt&extra_index=value@to:lxcnt,value@to:lxratio&year=2020&main_name=总量:overlap,履行数:bar,履行率:line",
    "执法监督_法律规范_全行业法律法规履行情况_drop": "127.0.0.1:3389/api/fz/?table=jd_fl_cy_shij_hy_xljb_cnt_lxcnt_lxratio&name=hy&stack=hy&value=cnt&extra_index=value@to:lxcnt,value@to:lxratio&year=2020&main_name=总量,履行数,履行率",
    # 缺少行业字段
    # "执法监督_法律规范_全行业法律法规履行情况_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_fl_cy_xj_hy_xljb_cnt_lxcnt_lxratio&name=xj_02&stack=xj_02&hy={gd_id4}&value=cnt&extra_index=value@to:lxcnt,value@to:lxratio&main_name=总量:overlap,履行数:bar,履行率:line&year=2020",
    "执法监督_法律规范_全行业法律法规履行情况_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_fl_cy_xj_hy_xljb_cnt_lxcnt_lxratio&name=xj_02&stack=xj_02&hy={gd_id4}&value=cnt&extra_index=value@to:lxcnt,value@to:lxratio&main_name=总量,履行数,履行率&year=2020",
    # 缺少行业字段
    "执法监督_法律规范_全市区法律法规履行情况_drop": "127.0.0.1:3389/api/fz/?table=jd_fl_cy_xj_hy_xljb_cnt_lxcnt_lxratio&name=xj_02&stack=xj_02&value=cnt&extra_index=value@to:lxcnt,value@to:lxratio&main_name=总量,履行数,履行率&year=2020",
    # "执法监督_法律规范_全市区法律法规履行情况_drop": "127.0.0.1:3389/api/fz/?table=jd_fl_cy_xj_hy_xljb_cnt_lxcnt_lxratio&name=xj_02&stack=xj_02&value=cnt&extra_index=value@to:lxcnt,value@to:lxratio&main_name=总量:overlap,履行数:bar,履行率:line&year=2020",
    "执法监督_法律规范_全市区法律法规履行情况_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_fl_cy_xj_hy_xljb_cnt_lxcnt_lxratio&name=hy&stack=hy&value=cnt&extra_index=value@to:lxcnt,value@to:lxratio&main_name=总量,履行数,履行率&year=2020&xj_02={gd_id4}",
    # "执法监督_法律规范_全市区法律法规履行情况_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_fl_cy_xj_hy_xljb_cnt_lxcnt_lxratio&name=hy&stack=hy&value=cnt&extra_index=value@to:lxcnt,value@to:lxratio&main_name=总量:overlap,履行数:bar,履行率:line&year=2020&xj_02={gd_id4}",
    "执法监督_法律规范_历年法律法规履行情况": "127.0.0.1:3389/api/fz/?table=jd_fl_cy_shij_hy_xljb_cnt_lxcnt_lxratio&name=year&stack=year&value=cnt&extra_index=value@to:lxcnt,value@to:lxratio&main_name=总量,履行数,履行率",
    # "执法监督_法律规范_历年法律法规履行情况": "127.0.0.1:3389/api/fz/?table=jd_fl_cy_shij_xljb_cnt_lxcnt_lxratio&name=year&stack=year&value=cnt&extra_index=value@to:lxcnt,value@to:lxratio&main_name=总量:overlap,履行数:bar,履行率:line",
    "执法监督_法律规范_历年法律法规变化统计": "127.0.0.1:3389/api/fz/?table=jd_fl_cy_shij_xljb_lfxz_cnt&name=year&stack=xljb&value=cnt",

    # 执法监督_权责清单 year=2020&is_ga=true/false
    # 左侧
    "执法监督_权责清单_职权总数": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_shij_zqcnt_flcnt_yjcnt&value=zqcnt&year=2020",
    "执法监督_权责清单_关联法律规范数": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_shij_zqcnt_flcnt_yjcnt&value=flcnt&year=2020",
    "执法监督_权责清单_关联依据数": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_shij_zqcnt_flcnt_yjcnt&value=yjcnt&year=2020",
    # "备注13": "jd_cf_cy_shij_zqcnt_lxratio中没有已履行数",
    # "执法监督_权责清单_处罚职权总数": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_zqcnt_lxratio&value=zqcnt&year=2020",
    "执法监督_权责清单_处罚职权履行率": "127.0.0.1:3389/api/fz/?table=jd_cf_cy_shij_zqcnt_lxcnt_lxratio&value=zqcnt&extra_index=value@to:lxcnt&main_name=总数,履行数&year=2020",
    # "备注14": "jd_xk_cy_shij_zqcnt中没有履行率、已履行数",
    "执法监督_权责清单_许可职权履行率": "127.0.0.1:3389/api/fz/?table=jd_xk_cy_shij_zqcnt_lxcnt_ratio&value=zqcnt&extra_index=value@to:lxcnt&main_name=总数,履行数&year=2020",
    # 变化
    # "执法监督_权责清单_全行业职权分析_drop": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_shij_hy_zqlx_cnt&name=hy&stack=zqlx&value=cnt",
    "执法监督_权责清单_全行业职权分析_drop": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_shij_hy_zqlx_cnt&name=hy&stack=hy&value=cnt&extra_index=stack@to:zqlx&main_name=总数,",
    "执法监督_权责清单_全行业职权分析_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_xj_hy_zqlx_cnt&name=xj_02&stack=xj_02&value=cnt&extra_index=stack@to:zqlx&main_name=总数,&hy={gd_id4}",
    "执法监督_权责清单_全市区职权分析_drop": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_xj_hy_zqlx_cnt&name=xj_02&stack=xj_02&value=cnt&extra_index=stack@to:zqlx&main_name=总数,",
    "执法监督_权责清单_全市区职权分析_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_xj_hy_zqlx_cnt&name=hy&stack=hy&extra_index=stack@to:zqlx&xj_02={gd_id4}&main_name=总数,",
    "执法监督_权责清单_全行业休眠职权分析_drop": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_shij_hy_zqlx_xmcnt&name=hy&stack=hy&extra_index=stack@to:zqlx&main_name=总数,",
    "执法监督_权责清单_全行业休眠职权分析_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_xj_hy_zqlx_xmcnt&name=xj_02&stack=xj_02&extra_index=stack@to:zqlx&main_name=总数,",
    "执法监督_权责清单_全市区休眠职权分析_drop": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_xj_hy_zqlx_cnt&name=xj_02&stack=xj_02&extra_index=stack@to:zqlx&main_name=总数,",
    "执法监督_权责清单_全市区休眠职权分析_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_xj_hy_zqlx_cnt&name=hy&stack=hy&xj_02={gd_id4}&extra_index=stack@to:zqlx&main_name=总数,",
    "执法监督_权责清单_职权类型分析": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_xj_hy_zqlx_cnt&name=zqlx&value=cnt",
    "执法监督_权责清单_职权来源分析": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_shij_xljb_cnt&name=xljb&value=cnt",
    "执法监督_权责清单_历年职权分析": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_xj_hy_zqlx_cnt&name=year&stack=year&value=cnt&extra_index=stack@to:zqlx&main_name=总数,",
    "执法监督_权责清单_全行业涉刑职权_drop": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_shij_hy_sxcnt&name=hy",
    "执法监督_权责清单_全行业涉刑职权_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_xj_hy_sxcnt&name=xj_02&gd_id={gd_id4}",
    "执法监督_权责清单_全市区涉刑职权_drop": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_xj_hy_sxcnt&name=xj_02",
    "执法监督_权责清单_全市区涉刑职权_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_xj_hy_sxcnt&name=hy&xj_02={gd_id4}",
    "执法监督_权责清单_历年涉刑职权": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_xj_hy_sxcnt&name=year",
    # "执法监督_权责清单_全行业年度职权调整分析$": "127.0.0.1:3389/api/fz/?table=jd_qz_cm_shij_hy_tzlx_tzcnt&name=hy&stack=month&extra_index=stack@to:tzlx",
    "执法监督_权责清单_全行业年度职权调整分析$": "127.0.0.1:3389/api/fz/\?gd_id=执法监督_权责清单_全行业年度职权调整分析",
    # "执法监督_权责清单_全行业年度职权调整分析_(.*?)_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_qz_cm_shij_hy_tzlx_tzcnt&name=tzlx&value=tzcnt&hy={gd_id4}&month={gd_id5}",
    "执法监督_权责清单_全行业自由裁量权分析_drop": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_shij_hy_clcnt&name=hy",
    "执法监督_权责清单_全行业自由裁量权分析_(.*?)": "127.0.0.1:3389/api/fz/?table=jd_qz_cy_xj_hy_clcnt&name=xj_02&hy={gd_id4}",  # 缺表
    #   #执法监督_主题分析 year=2020&is_ga=true/false
    "执法监督_主题分析_地下管线分析_(.*?)_行业涉及职权分布":"127.0.0.1:3389/api/fz/?table=jd_zt_cy_ztlx1_ztlx2_shij_hy_cnt&name=hy&ztlx2={gd_id4}",
    "执法监督_主题分析_地下管线分析_(.*?)_职权分布":"127.0.0.1:3389/api/fz/?table=jd_zt_cy_ztlx1_ztlx2_shij_zqlx_zqcnt&name=zqlx&ztlx2={gd_id4}",
    "执法监督_主题分析_地下管线分析_(.*?)_依据分布":"127.0.0.1:3389/api/fz/?table=jd_zt_cy_ztlx1_ztlx2_shij_zqlx_yjcnt&name=zqlx&ztlx2={gd_id4}",
    "执法监督_主题分析_地下管线分析_(.*?)_具体法律法规分析_数目$":"127.0.0.1:3389/api/fz/?table=jd_zt_cy_ztlx_shij_fl_zqlx_yjzq_zqcnt_yjcnt_wlxzqcnt_ajcnt&value=zqcnt&ztlx2={gd_id4}&extra_index=value@to:yjcnt,value@to:wlxzqcnt,value@to:ajcnt&main_name=行使职权数,行使依据数,未履行职权,案件数",
    "执法监督_主题分析_地下管线分析_(.*?)_具体法律法规分析_详情_drop":"127.0.0.1:3389/api/fz/?table=jd_zt_cy_ztlx_shij_fl_zqlx_yjzq_zqcnt_yjcnt_wlxzqcnt_ajcnt&name=yjzq&stack=zqlx&value=ajcnt&ztlx2={gd_id4}",
    "执法监督_主题分析_地下管线分析_(.*?)_具体法律法规分析_详情_(.*?)":"127.0.0.1:3389/api/fz/?table=jd_zt_cy_ztlx_shij_fl_zqlx_yjzq_yjmc&name=yjzq&value=yjmc&ztlx2={gd_id4}&yjzq={gd_id7}",
    "执法监督_主题分析_地下管线分析_(.*?)_涉及法律法规":"127.0.0.1:3389/api/fz/?table=jd_zt_cy_ztlx_shij_fl_zqlx_yjzq_zqcnt_yjcnt_wlxzqcnt_ajcnt&value=fl&ztlx2={gd_id4}",


}
