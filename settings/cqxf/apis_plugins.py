APIS_PLUGIN = [
    # 受信人列表
    {
        # 重庆_信访形式_受信人名单
        # 测试用例：http://127.0.0.1:3389/api/xf/?gd_id=hb_xfxs_sxrmd&day=[2019-09-01,2020-09-01]
        "url": "/api/xf/\?gd_id=cq_xfxs_sxrmd&",
        "map": {"name": "姓名", "value": "信访件次"},
        "fx_db_sql": """
 """,
        "zb_db_sql": """
    SELECT x1.xm as name, x2.xfjc as value FROM xf_sxr_cy_xm_sx x1
    LEFT JOIN ( SELECT sxr, sum( xfjc ) xfjc FROM xf_sxr_cd_shij_cfxfbz_xfjc_zb
    WHERE `day` >= '{start}' AND `day` <= '{end}' GROUP BY sxr ) x2 
    ON x1.xm = x2.sxr ORDER BY x1.sx
 """,
        # "on": "zjhm"
        # "time_format": "%Y年%m月%d日"
        "value_map": [("value", "{value}", 0)],
    },
]
