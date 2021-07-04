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
        # 深圳_执法监督_预警分析_预警详情
        # 测试用例：http://127.0.0.1:3389/api/xf/?gd_id=yn_xfrfx_xfgjfxnr&xfsxid=20695617
        "url": "/api/fz/\?gd_id=预警详情&",
        "map": {"yjrq": "预警日期", "yjdz": "预警地址", "yjdj": "预警等级","yjzq":"预警详情"},
        "fx_db_sql": """
            """,
        "zb_db_sql": """
        SELECT yjrq,yjdz,yjdj,yjzq FROM jd_yj_cd_yjrq_yjdz_yjdj_yjzq_cnt;
             """,
        "time_format": "%Y年%m月%d日"
    },
    {
        # 深圳_执法监督_权责清单_全行业年度职权调整分析
        "url": "/api/fz/\?gd_id=执法监督_权责清单_全行业年度职权调整分析&",
        "map": {"hy": "行业", "month": "月份", "xzcnt": "新增","tzcnt":"调整","hbcnt":"合并","cfcnt":"拆分","cxcnt":"撤销","sumcnt":"总数"},
        "fx_db_sql": """
            """,
        "zb_db_sql": """
        SELECT a.hy,a.month,sum(a.xzcnt)as xzcnt,sum(a.tzcnt) as tzcnt,sum(a.hbcnt)as hbcnt,sum(a.cxcnt) as cxcnt,sum(a.cfcnt) as cfcnt,sum(a.xzcnt+a.tzcnt+a.hbcnt+a.cxcnt+a.cfcnt) as sumcnt
         from 
(SELECT year,hy,month,case tzlx when '新增' then tzcnt else 0 end as xzcnt,case tzlx when '合并' then tzcnt else 0 end as hbcnt,case tzlx when '调整' then tzcnt else 0 end as tzcnt,case tzlx when '撤销' then tzcnt else 0 end as cxcnt,case tzlx when '拆分' then tzcnt else 0 end as cfcnt FROM jd_qz_cm_shij_hy_tzlx_tzcnt) as a
where a.year = {year}
GROUP BY hy,month,year;
         """,
    },

]