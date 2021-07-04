APIS_PLUGIN = [
    # 第一条为仅作为示例
    {
        # 根据正则匹配url
        # 注意：问号前需要有\是转义
        "url":"/api/xf/\?gd_id=YOUR ID$",
        
        # 模式
        "mode": "sql",  # 模式匹配，目前有两种模式  sql/custom  sql模式是默认模式，custom模式需要执行执行文件

        # 文件名【custom模式必须】
        "file": "ztfxgb", # custom模式时，需要指定执行的文件，该文件需要在settings/$project/custom/目录下，后缀.py可有可无，需要实现run方法
        
        # 最终要的字段，以及匹配取值【sql模式必须】
        # 注意：map的键需要全部出现在返回的最终数据表中，并且按照map的获取相应的列
        "map":"",

        # 【sql模式下，至少有一条sql起作用】
        # 分析库（输入库）的SQL：{}包裹的，可以写三种值：1. settings中的变量  2. url的参数  3. start/end  4. url中的query字段的拆分出来的参数
        # 注意：如果无效，程序自动跳过，判断有效标准为是否含有select关键字，两条SQL至少一条要有效
        "fx_db_sql":"",

        # 指标库（输出库）的SQL：{}包裹的，可以写三种值：1. settings中的变量  2. url的参数  3. start/end  4. url中的query字段的拆分出来的参数
        # 注意：如果无效，程序自动跳过，判断有效标准为是否含有select关键字，两条SQL至少一条要有效
        "zb_db_sql":"",

        # 【sql模式下可选】
        # 进行连接的字段
        # 注意： 1. 字符串或者列表均可
        #       2. 只有一个sql的时候，on字段没有用
        #       3. 当有两个sql的时候，on字段为空，或者没有，自动寻找两个数据表中一样的字段进行匹配
        #       4. 当有两个sql的时候，on字段不为空，以on字段为准进行匹配，其他相同的字段，用_x 和_y进行标识
        "on":"",

        # 【sql模式下可选】
        # 时间格式化
        # 注意：如果出现了时间，需要指定格式化的形式，否则按照项目默认格式化规范
        "time_format": "%Y年%m月%d日",

        # 【sql模式下可选】
        # 内容映射：列表，包含多个元组，如果没有或不写，默认就是空字符串
        # 如果元组的长度为4：(新列, 旧列, 更改的内容, 如果内容为空时的默认值)  旧列不会删除，可以由map进行筛选
        # 如果元组的长度为3：(列名, 更改的内容, 如果内容为空时的默认值)
        # {}可以包含四类值
        # 1. settings中的变量
        # 2. url中的参数
        # 3. start/end
        #### 4. url中的query字段的拆分出来的参数
        # 5. map/map.lower/map.upper/ 在提前定义好的字典里寻找匹配的映射
        # 6. value 当前值
        # 7. 反查的大表格需要有query字段，并且严格匹配数据库的字段

        "value_map": [("tx", "{FILE_PATH}{value}", "default.png")]
    },
    # 用于测试query的样例
    {
        # 河北_信访人分析_基本信息
        # 测试用例：http://127.0.0.1:3389/api/xf/?gd_id=h&query=zjhm:130623197709052130
        "url": "/api/xf/\?gd_id=test_query_data&",
        "map": {"tx": "头像", "xm": "姓名", "xbmc": "性别", "age": "年龄", "sjh": "电话", "zjhm": "身份证号", "hkszd": "户籍地",
                "zzmcxq": "居住地", "xfjc": "信访件次", "day": "最新信访时间"},
        "fx_db_sql": """
    SELECT tx, xm, xbmc, age, sjh,zjhm, hkszd, zzmcxq FROM xf_xfrxx WHERE {query} AND xbmc IS NOT NULL AND age IS NOT NULL ORDER BY create_time DESC LIMIT 1;
    """,
        "zb_db_sql": """
        select xfjc, zjhm, day from (
				SELECT xf_xfr_cy_zjhm_xm_xfjc.xfjc, xf_xfr_cy_zjhm_xm_xfjc.zjhm,xf_xfr_cd_zjhm_xfrq_xfsx_xfjc.day FROM xf_xfr_cy_zjhm_xm_xfjc join xf_xfr_cd_zjhm_xfrq_xfsx_xfjc on xf_xfr_cy_zjhm_xm_xfjc.zjhm=xf_xfr_cd_zjhm_xfrq_xfsx_xfjc.zjhm ) as t WHERE {query} order by day desc limit 1;    """,
        "on": "zjhm",
        # "time_format": "%Y年%m月%d日"
        "value_map": [("tx", "{FILE_PATH}{value}", "default.png")]
    },
    {
        # 河北_信访人分析_基本信息
        # 测试用例：http://127.0.0.1:3389/api/xf/?gd_id=hb_xfrfx_jbxx&zjhm=130623197709052130
        "url": "/api/xf/\?gd_id=hb_xfrfx_jbxx&",
        "map": {"tx": "头像", "xm": "姓名", "xbmc": "性别", "age": "年龄", "sjh": "电话", "zjhm": "身份证号","hkszd": "户籍地", "zzmcxq": "居住地", "xfjc":"信访件次","day":"最新信访时间"},
        "fx_db_sql": """
        SELECT tx, xm, xbmc, age, sjh,zjhm, hkszd, zzmcxq FROM xf_xfrxx WHERE zjhm = '{zjhm}' AND xbmc IS NOT NULL AND age IS NOT NULL ORDER BY create_time DESC LIMIT 1;
        """,
        "zb_db_sql": """
        SELECT xf_xfr_cy_zjhm_xm_xfjc.xfjc, xf_xfr_cy_zjhm_xm_xfjc.zjhm,xf_xfr_cd_zjhm_xfrq_xfsx_xfjc.day FROM xf_xfr_cy_zjhm_xm_xfjc join xf_xfr_cd_zjhm_xfrq_xfsx_xfjc on xf_xfr_cy_zjhm_xm_xfjc.zjhm=xf_xfr_cd_zjhm_xfrq_xfsx_xfjc.zjhm WHERE xf_xfr_cy_zjhm_xm_xfjc.zjhm ='{zjhm}' order by xf_xfr_cd_zjhm_xfrq_xfsx_xfjc.day desc limit 1;
        """,
        "on": "zjhm",
        # "time_format": "%Y年%m月%d日"
        "value_map": [("tx", "{FILE_URL}{value}", "default.png")]
    },

{
        # 河北_信访人分析_信访轨迹分析内容
        # 测试用例：http://127.0.0.1:3389/api/xf/?gd_id=hb_xfrfx_xfgjfxnr&xfsxid=20695617
        "url": "/api/xf/\?gd_id=hb_xfrfx_xfgjfxnr&",
        "map": {"xfjbh": "信访编号", "xfrq": "信访日期", "nrflmc": "内容分类", "xfxsmc": "信访形式", "xfmdmc": "信访目的", "wtsdmc": "问题属地","djjgmc":"登记单位","xfjztmc":"信访状态"},
        "fx_db_sql": """
        SELECT xfjbh,xfrq,nrflmc,xfxsmc,xfmdmc,wtsdmc,djjgmc,xfjztmc FROM xf_xfjxx WHERE xfsxid = '{xfsxid}' AND check_flag = 0;

        """,
        "zb_db_sql": """
         """,
        # "on": "zjhm"
        "time_format": "%Y年%m月%d日"
    },

    {
        # 河北_信访人分析_信访轨迹分析时间轴
        # 测试用例：http://127.0.0.1:3389/api/xf/?gd_id=hb_xfrfx_xfgjfxsjz&zjhm=130623197709052130
        "url": "/api/xf/\?gd_id=hb_xfrfx_xfgjfxsjz&",
        "map": {"xfjc": "重复信访次数", "day": "信访日期", "xfsx": "信访事项id"},
        "fx_db_sql": """
         """,
        "zb_db_sql": """
        select xfjc, day, xfsx from ((select xfjc, day, xfsx from xf_xfr_cd_zjhm_xfrq_xfsx_xfjc where zjhm = '{zjhm}' order by day desc limit 3) union (select xfjc, day, xfsx from xf_xfr_cd_zjhm_xfrq_xfsx_xfjc where zjhm = '{zjhm}' order by day limit 1)) as tb order by day;
         """,
        # "on": "zjhm"
        "time_format": "%Y年%m月%d日"
    },

    {
        # 河北_攻坚治理_包案领导
        # 测试用例：http://127.0.0.1:3389/api/xf/?gd_id=hb_gjzl_bald&day=[2019-09-01,2020-09-01]
        "url": "/api/xf/\?gd_id=hb_gjzl_bald&",
        "map": {"xm": "姓名", "id": "id", "xfjc": "信访件次"},
        "fx_db_sql": """
         """,
        "zb_db_sql": """
        select xm, id, xfjc from xf_ba_cd_shej_id_xm_px_xfjc WHERE day >= '{start}' AND day <= '{end}' order by px;
         """,
        # "on": "zjhm",
        # "time_format": "%Y年%m月%d日",
        "value_map": [("xfjc", "{value}", "0")],
    },

    {
        # 河北_信访形式_受信人名单
        # 测试用例：http://127.0.0.1:3389/api/xf/?gd_id=hb_xfxs_sxrmd&day=[2019-09-01,2020-09-01]
        "url": "/api/xf/\?gd_id=hb_xfxs_sxrmd&",
        "map": {"xm": "姓名", "xfjc": "信访件次"},
        "fx_db_sql": """
     """,
        "zb_db_sql": """
        SELECT x1.xm, x2.xfjc FROM xf_sxr_cy_xm_sx x1
        LEFT JOIN ( SELECT sxr, sum( xfjc ) xfjc FROM xf_sxr_cd_shej_cfxfbz_xfjc 
        WHERE `day` >= '{start}' AND `day` <= '{end}' GROUP BY sxr ) x2 
        ON x1.xm = x2.sxr ORDER BY x1.sx
     """,
        # "on": "zjhm"
        # "time_format": "%Y年%m月%d日"
        "value_map": [("xfjc", "{value}", "0")],
    },
]
