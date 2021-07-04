APIS_PLUGIN = [
    # # 用于测试大弹窗的样例
    # {
    #     # 河北_信访人分析_基本信息
    #     # 测试用例：http://127.0.0.1:3389/api/xf/?gd_id=h&query_data=zjhm:130623197709052130
    #     "url": "/api/xf/\?gd_id=test_dtc&",
    #     "map": {"name": "信访形式", "value": "信访件次", "query": "查询id"},
    #     "fx_db_sql": """
    #     """,
    #     "zb_db_sql": """
    #     select xfxs as name, xfrqjc as value, xfxs as query from xf_xxx""",
    #     # "on": "zjhm",
    #     # "time_format": "%Y年%m月%d日"
    #     "value_map": [("query", "cfxfbz:1,yjnr_code:{map}", "")]
    # },

    {
        # 广东_自定义主题分析_主题分析报告
        # 测试用例：http://127.0.0.1:3389/api/xf/?gd_id=gd_zdyztfx_ztfxbg&zt=涉众型经济案件&day=[2020-01-01,2020-01-03]
        "url": "/api/xf/\?gd_id=gd_zdyztfx_ztfxbg&",
        "mode": "custom",
        "file": "ztfxbg",
    },
    {
        # 广东_全局业务监控_表格弹窗
        # 测试用例：http://127.0.0.1:3389/api/xf/?gd_id=gd_qjywjk_bgtc&query=来信&query_date=信访日期&day=[2019-01-01,2020-01-03]
        "url": "/api/xf/\?gd_id=gd_qjywjk_bgtc&",
        "mode": "custom",
        "file": "bgtc",
    },


    ###################### 广东_信访人分析（重点人员）######################
    {
        # 广东_信访人分析_基本信息
        # 测试用例：http://39.107.240.28:3389/api/xf/?gd_id=gd_xfrfx_jbxx&sfzhm=44082519581025149X
        "url": "/api/xf/\?gd_id=gd_xfrfx_jbxx&",
        "map": {"tx": "头像", "xm": "姓名", "xbmc": "性别", "age": "年龄", "sjh": "电话", "sfzhm": "身份证号","hkszd": "户籍地", "zzmcxq": "居住地","xfrq":"最新信访时间"},
        "fx_db_sql": """SELECT xf_xfrxx.tx, xf_xfrxx.xm, xf_xfrxx.xbmc, xf_xfrxx.age, xf_xfrxx.sjh, xf_xfrxx.sfzhm, xf_xfrxx.hkszd, xf_xfrxx.zzmcxq, xf_xfjxx.xfrq xfrq FROM xf_xfrxx join xf_xfjxx on xf_xfrxx.xfjbh=xf_xfjxx.xfjbh WHERE xf_xfrxx.sfzhm = '{sfzhm}'  AND xf_xfrxx.xbmc IS NOT NULL AND xf_xfrxx.age IS NOT NULL ORDER BY xf_xfrxx.create_time DESC LIMIT 1""",
        "zb_db_sql": """ """,
        "on": "sfzhm",
        # "time_format": "%Y年%m月%d日"
        "value_map": [("tx", "{FILE_URL}{value}", "default.png")]
    },
    {
        # 广东_信访人分析_信访轨迹分析内容
        # 测试用例：http://39.107.240.28:3389/api/xf/?gd_id=gd_xfrfx_xfgjfxnr&xfsxid=
        "url": "/api/xf/\?gd_id=gd_xfrfx_xfgjfxnr&",
        "map": {"xfjbh": "信访编号", "xfrq": "信访日期", "nrflmc": "内容分类", "xfxsmc": "信访形式", "xfmdmc": "信访目的", "wtsdmc": "问题属地","djjgmc":"登记单位","xfjztmc":"信访状态"},
        "fx_db_sql": """
        SELECT xfjbh,xfrq,nrflmc,xfxsmc,xfmdmc,wtsdmc,djjgmc,xfjztmc FROM xf_xfjxx WHERE xfsxid = '{xfsxid}' AND check_flag = 0

        """,
        "":"""""",
        "zb_db_sql": """
         """,
        # "on": "sfzhm"
        "time_format": "%Y年%m月%d日"
    },
    {
        # 广东_信访人分析_信访轨迹分析时间轴
        # 测试用例：http://39.107.240.28:3389/api/xf/?gd_id=gd_xfrfx_xfgjfxsjz&sfzhm=44082519581025149X
        "url": "/api/xf/\?gd_id=gd_xfrfx_xfgjfxsjz&",
        "map": {"xfrq": "信访日期", "xfsxid": "信访事项id"},
        "fx_db_sql": """select xfrq, xfsxid from(
        (select xfrq, count(*),   group_concat(xfsxid) as xfsxid from 
        (select xf_xfjxx.xfrq, xf_xfjxx.xfsxid from xf_xfjxx join xf_xfrxx on xf_xfjxx.xfjbh=xf_xfrxx.xfjbh where  xf_xfrxx.sfzhm='{sfzhm}') tb where xfrq between '{start}' and '{end}'  group by xfrq order by xfrq limit 1) 
        union (select xfrq, count(*),   group_concat(xfsxid) as xfsxid from (select xf_xfjxx.xfrq, xf_xfjxx.xfsxid from xf_xfjxx join xf_xfrxx on xf_xfjxx.xfjbh=xf_xfrxx.xfjbh where  xf_xfrxx.sfzhm='{sfzhm}') tb 
        where xfrq between '{start}' and '{end}'  group by xfrq order by xfrq desc limit 3
        ))  as sjz order by xfrq;""",
        "zb_db_sql": """""",
        "time_format": "%Y年%m月%d日"
    },
    ###################### 广东_全局业务监控的弹窗（饼图/一级内容/地图）######################
    {
        # 广东_全局业务监控_信访形式的饼图弹窗
        # 测试用例：http://39.107.240.28:3389/api/xf/?gd_id=gd_qjywjk_xfxstc&query_date=信访日期&day=[2019-01-01,2020-01-01]
        "url": "/api/xf/\?gd_id=gd_qjywjk_xfxstc&",
        "map": {"name": "信访形式", "value": "信访件次", "query": "查询id"},
        "variables": {"v_table": "{query_date}==信访日期 then xf_xfj_cd_xj_xfxs_xfrqxfjc;"
                                 "{query_date}==登记日期 then xf_xfj_cd_xj_xfxs_djrqxfjc;"
                                 "{query_date}==交换日期 then xf_xfj_cd_xj_xfxs_jhrqxfjc;",
                      "v_select": "{query_date}==信访日期 then xfrqxfjc;"
                                  "{query_date}==登记日期 then djrqxfjc;"
                                  "{query_date}==交换日期 then jhrqxfjc;"},
        "fx_db_sql": """""",
        "zb_db_sql": """
        SELECT a.name, a.name as query, sum(a.value) as value from (select (CASE WHEN xfxs = '来信' THEN '来信'
        WHEN xfxs = '来访' THEN '来访'
        ELSE '网信' END) as name, {v_select} as value, day, shej_02, shij_02, xj_02 from {v_table}) a where a.day between '{start}' and '{end}' and a.{sql_qhauth_auto} group by a.name
        """,
        "full": {"name": "xfxs", "value": [0], "query": "$name"}
    },
    {
        # 广东_全局业务监控_一级内容弹窗
        # 测试用例：http://39.107.240.28:3389/api/xf/?gd_id=gd_qjywjk_yjnrtc&query_date=信访日期&day=[2019-01-01,2020-01-01]
        "url": "/api/xf/\?gd_id=gd_qjywjk_yjnrtc&",
        "map": {"name": "一级内容", "value": "信访件次", "query": "查询id"},
        "variables": {"v_table": "{query_date}==信访日期 then xf_xfj_cd_xj_yjnr_xfrqxfjc;"
                                 "{query_date}==登记日期 then xf_xfj_cd_xj_yjnr_djrqxfjc;"
                                 "{query_date}==交换日期 then xf_xfj_cd_xj_yjnr_jhrqxfjc;",
                      "v_select": "{query_date}==信访日期 then xfrqxfjc;"
                                  "{query_date}==登记日期 then djrqxfjc;"
                                  "{query_date}==交换日期 then jhrqxfjc;"},
        "fx_db_sql": """""",
        "zb_db_sql": """
    select yjnr as name, yjnr as query, sum({v_select}) as value from {v_table} where day between '{start}' and '{end}' and {sql_qhauth_auto} group by yjnr 
    """,
        "full": {"name": "yjnr", "value": [0], "query": "$name"}
    },
    {
        # 广东_全局业务监控_地图弹窗
        # 测试用例：http://39.107.240.28:3389/api/xf/?gd_id=gd_qjywjk_dttc&query_date=信访日期&day=[2019-01-01,2020-01-01]
        "url": "/api/xf/\?gd_id=gd_qjywjk_dttc&",
        "map": {"name": "区划", "value": "信访件次", "query": "查询id"},
        "variables": {"v_table": "{query_date}==信访日期 then xf_xfj_cd_xj_xfrqxfjc;"
                                 "{query_date}==登记日期 then xf_xfj_cd_xj_djrqxfjc;"
                                 "{query_date}==交换日期 then xf_xfj_cd_xj_jhrqxfjc;",
                      "v_select": "{query_date}==信访日期 then xfrqxfjc;"
                                  "{query_date}==登记日期 then djrqxfjc;"
                                  "{query_date}==交换日期 then jhrqxfjc;",
                      "v_qhwhere": "{name}==xj_02 then shij_02;"
                                   "{name}==shij_02 then shej_02",
                      "v_qhwhere_value": "{name}==shij_02 then '广东省';"
                                         "{name}==xj_02 then {shij_02}"},
        "fx_db_sql": """""",
        "zb_db_sql": """
select {name} as name, {name} as query, sum({v_select}) as value from {v_table} where {v_qhwhere}='{v_qhwhere_value}' AND day between '{start}' and '{end}' group by {name}
""",
        "full": {"name": "zb_db_sql:select {name} from {v_table} where {v_qhwhere}='{v_qhwhere_value}'", "value": [0], "query": "$name"}
    },

    {
        # 广东_全局业务监控_地图弹窗后的小弹窗
        # 测试用例：http://39.107.240.28:3389/api/xf/?gd_id=gd_qjywjk_tcaftertc&xfjbh=LX0000002019102900499
        "url": "/api/xf/\?gd_id=gd_qjywjk_tcaftertc&",
        "map": {"xfjztmc": "信访件状态", "xfrq": "信访日期", "bjsj": "办结日期",
                "bljg": "办理机构", "blfs": "办理方式", "qxjg": "去向机构"},
        "fx_db_sql": """select a.xfjztmc, a.xfrq, a.bjsj, b.xfjbh, b.bljg, b.blfs, b.qxjg from xf_xfjxx a LEFT JOIN xf_blfsxx b on a.xfjbh=b.xfjbh where b.xfjbh='{xfjbh}';""",
        "zb_db_sql": """""",
    },


]