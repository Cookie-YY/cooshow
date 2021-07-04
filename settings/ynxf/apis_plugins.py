APIS_PLUGIN = [
    # 第一条为仅作为示例
    {
        # 根据正则匹配url
        # 注意：问号前需要有\是转义
        "url": "/api/xf/\?gd_id=YOUR ID$",

        # 模式
        "mode": "sql",  # 模式匹配，目前有两种模式  sql/custom  sql模式是默认模式，custom模式需要执行执行文件

        # 文件名【custom模式必须】
        "file": "ztfxgb",  # custom模式时，需要指定执行的文件，该文件需要在settings/$project/custom/目录下，后缀.py可有可无，需要实现run方法

        # 最终要的字段，以及匹配取值【sql模式必须】
        # 注意：map的键需要全部出现在返回的最终数据表中，并且按照map的获取相应的列
        "map": "",

        # 【sql模式下，至少有一条sql起作用】
        # 分析库（输入库）的SQL：{}包裹的，可以写三种值：1. settings中的变量  2. url的参数  3. start/end  4. url中的query字段的拆分出来的参数
        # 注意：如果无效，程序自动跳过，判断有效标准为是否含有select关键字，两条SQL至少一条要有效
        "fx_db_sql": "",

        # 指标库（输出库）的SQL：{}包裹的，可以写三种值：1. settings中的变量  2. url的参数  3. start/end  4. url中的query字段的拆分出来的参数
        # 注意：如果无效，程序自动跳过，判断有效标准为是否含有select关键字，两条SQL至少一条要有效
        "zb_db_sql": "",

        # 【sql模式下可选】
        # 进行连接的字段
        # 注意： 1. 字符串或者列表均可
        #       2. 只有一个sql的时候，on字段没有用
        #       3. 当有两个sql的时候，on字段为空，或者没有，自动寻找两个数据表中一样的字段进行匹配
        #       4. 当有两个sql的时候，on字段不为空，以on字段为准进行匹配，其他相同的字段，用_x 和_y进行标识
        "on": "",

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
    {
        # 云南_信访人分析_重点人员列表
        # 测试用例：http://127.0.0.1:3389/api/xf/?gd_id=yn_xfrfx_xfrlb&query=zx  # 全部/扬言/专项    qb/yy/zx
        "url": "/api/xf/\?gd_id=yn_xfrfx_xfrlb&",
        "map": {"name": "姓名", "value": "身份证号"},
        "variables": {"v_table": "{query}==全部 then xf_xfr_cy_zjhm_xm_xfjc;"  # 全部
                                 "{query}==扬言 then xf_xfr_cy_zjhm_xm_yy_xfjc;"   # 扬言
                                 "{query}==专项 then xf_xfr_cy_zjhm_xm_zxbz_xfjc"}, # 专项
        "fx_db_sql": """""",
        "zb_db_sql": """
    SELECT xm as name, zjhm as value FROM {v_table} WHERE zjhm in (SELECT zjhm FROM xf_xfr_cd_zjhm_xfrq_xfsx_xfjc) order by xfjc desc limit 100 """
    },

    {
        # 云南_信访人分析_基本信息
        # 测试用例：http://127.0.0.1:3389/api/xf/?gd_id=hb_xfrfx_jbxx&zjhm=130623197709052130
        "url": "/api/xf/\?gd_id=yn_xfrfx_jbxx&",
        "map": {"tx": "头像", "xm": "姓名", "xbmc": "性别", "age": "年龄", "sjh": "电话", "zjhm": "身份证号", "hkszd": "户籍地",
                "zzmcxq": "居住地", "xfjc": "信访件次", "day": "最新信访时间"},
        "fx_db_sql": """
        SELECT tx, xm, xbmc, age, sjh,zjhm, hkszd, zzmcxq FROM xf_xfrxx WHERE zjhm = '{zjhm}' ORDER BY create_time DESC LIMIT 1;
        """,
        "zb_db_sql": """
        SELECT xf_xfr_cy_zjhm_xm_xfjc.xfjc, xf_xfr_cy_zjhm_xm_xfjc.zjhm,xf_xfr_cd_zjhm_xfrq_xfsx_xfjc.day FROM xf_xfr_cy_zjhm_xm_xfjc join xf_xfr_cd_zjhm_xfrq_xfsx_xfjc on xf_xfr_cy_zjhm_xm_xfjc.zjhm=xf_xfr_cd_zjhm_xfrq_xfsx_xfjc.zjhm WHERE xf_xfr_cy_zjhm_xm_xfjc.zjhm ='{zjhm}' order by xf_xfr_cd_zjhm_xfrq_xfsx_xfjc.day desc limit 1 """,
        "on": "zjhm",
        # "time_format": "%Y年%m月%d日"
        "value_map": [("tx", "{FILE_URL}{value}", "default.png")]
    },

    {
        # 云南_信访人分析_信访轨迹分析内容
        # 测试用例：http://127.0.0.1:3389/api/xf/?gd_id=yn_xfrfx_xfgjfxnr&xfsxid=20695617
        "url": "/api/xf/\?gd_id=yn_xfrfx_xfgjfxnr&",
        "map": {"xfjbh": "信访编号", "xfrq": "信访日期", "nrflmc": "内容分类", "xfxsmc": "信访形式", "xfmdmc": "信访目的", "wtsdmc": "问题属地",
                "djjgmc": "登记单位", "xfjztmc": "信访状态"},
        "fx_db_sql": """
        SELECT xfjbh,xfrq,nrflmc,xfxsmc,xfmdmc,wtsdmc,djjgmc,xfjztmc FROM xf_xfjxx WHERE xfsxid = '{xfsxid}' AND check_flag = 0;

        """,
        "zb_db_sql": """
         """,
        # "on": "zjhm"
        "time_format": "%Y年%m月%d日"
    },

    {
        # 云南_信访人分析_信访轨迹分析时间轴
        # 测试用例：http://127.0.0.1:3389/api/xf/?gd_id=yn_xfrfx_xfgjfxsjz&zjhm=130623197709052130
        "url": "/api/xf/\?gd_id=yn_xfrfx_xfgjfxsjz&",
        "map": {"xfjc": "重复信访次数", "day": "信访日期", "xfsx": "信访事项id"},
        "fx_db_sql": """
         """,
        "zb_db_sql": """
         select xfjc, day, xfsx from ((select xfjc, day, xfsx from xf_xfr_cd_zjhm_xfrq_xfsx_xfjc where zjhm = '{zjhm}' order by day desc limit 3) union (select xfjc, day, xfsx from xf_xfr_cd_zjhm_xfrq_xfsx_xfjc where zjhm = '{zjhm}' order by day limit 1)) as tb order by day""",
        # "on": "zjhm"
        "time_format": "%Y年%m月%d日"
    },

    # 热点模型分析 带弹窗的饼图 进京/到省 & 次数/人数
    # 云南 热点模型分析 人数规模饼图(带弹窗)
    {
        # 测试用例：http://39.107.240.28:3389/api/xf/?gd_id=gd_qjywjk_dttc&query_date=信访日期&day=[2019-01-01,2020-01-01]
        "url": "/api/xf/\?gd_id=yn_rdmxfx_rspie&",
        "map": {"name": "人数规模", "value": "信访件次", "query": "查询id"},
        "variables": {"v_table": "{query_level}==fsf then xf_xfj_cd_shej_rsrange_xfxs_fsf_xfjc;"
                                 "{query_level}==jjf then xf_xfj_cd_shej_rsrange_xfxs_jjf_xfjc"},
        "fx_db_sql": """""",
        "zb_db_sql": """
select rsrange as name, rsrange as query, sum(xfjc) as value from {v_table} where 1=1 AND day between '{start}' and '{end}' group by name,query
""",
        "full": {"name": ["1人", "2-5人", "6-20人", "21-50人", "50人以上"], "value": [0],
                 "query": "$name"}
    },
    # 云南 热点模型分析 重复访次数饼图(带弹窗)
    {
        # 测试用例：http://127.0.0.1:3389/api/xf/?gd_id=yn_rdmxfx_cfcspie&query_level=到省&day=[2019-01-01,2020-01-01]
        "url": "/api/xf/\?gd_id=yn_rdmxfx_cfcspie&",
        "map": {"name": "重复访次数", "value": "信访件次", "query": "查询id"},
        "variables": {"v_table": "{query_level}==fsf then xf_xfj_cd_shej_cfcsrange_xfxs_fsf_xfjc;"
                                 "{query_level}==jjf then xf_xfj_cd_shej_cfcsrange_xfxs_jjf_xfjc"},
        "fx_db_sql": """""",
        "zb_db_sql": """
        select cfcsrange as name, cfcsrange as query, count(name) as value from {v_table} where 1=1 AND day between '{start}' and '{end}' group by name
        """,
        "full": {"name": ["1次", "2-5次", "6-10次", "11-30次", "31-50次", "50次以上"], "value": [0],
                 "query": "$name"}
    },

    # 云南 热点模型分析 到省访/进京访 饼图的弹窗 (人数/次数)
    {
        # 测试用例：http://127.0.0.1:3389/api/xf/?gd_id=yn_rdmxfx_datalist&query=1次&day=[2020-01-01,2020-12-31]&query_level=fsf
        "url": "/api/xf/\?gd_id=yn_rdmxfx_datalist&",  # 这里会传query=2-5次&query_level=fsf
        "mode": "custom",
        "file": "datalist"
    },


    # 云南_行为轨迹预警_重点人员摘要
    {
        # 测试用例：http://127.0.0.1:3389/api/xf/?gd_id=yn_xwgjyj_zdryzy&month=1&zjhm=10000000
        "url": "/api/xf/\?gd_id=yn_xwgjyj_zdryzy&",
        "mode": "custom",
        "file": "zdryzy",
    },
    # 云南_行为转化预警_重点信访人列表
    {
        # 测试用例：http://127.0.0.1:3389/api/xf/?gd_id=yn_xwgjyj_zdryzy&month=1&zjhm=10000000
        "url": "/api/xf/\?gd_id=yn_xwzhyj_zdxfrlb&",
        "map": {"name": "重点人员", "value": "信访件次", "query": "查询id"},
        "fx_db_sql": """""",
        "zb_db_sql": """
        select xm as name, zjhm as query, xfxwzs as value from xf_xfr_cm_zjhm_xm_xfxwzs where year={year} order by xfxwzs desc limit {limit}
        """,
        # "full": {"name": "yjnr", "value": [0], "query": "$name"}
    },

    # 行为分析模块
    # 行为转化漏斗
    {
        # 测试用例：http://127.0.0.1:3389/api/xf/?gd_id=yn_xwzhyj_xwzhld&year=2020&shij_02=昆明市
        "url": "/api/xf/\?gd_id=yn_xwzhyj_xwzhld&",
        "mode": "custom",
        "file": "zhld",
    },
    # 行为时间轨迹
    {
        # 测试用例：http://127.0.0.1:3389/api/xf/?gd_id=yn_xwgjyj_xwsjz&zjhm=1000000
        "url": "/api/xf/\?gd_id=yn_xwgjyj_xwsjz&",
        # "mode": "custom",
        "map": {"name": "日期", "value": "信访行为"},
        "fx_db_sql": """""",
        "zb_db_sql": """
        SELECT day as name,group_concat(xfxw separator '</br>') value FROM xf_xfr_cd_zjhm_xm_xfxw where zjhm='{zjhm}' GROUP BY day;""",
        "time_format": "%Y年%m月%d日"
    },


]
