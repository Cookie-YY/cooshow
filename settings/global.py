# 设定判断超时的时间（用于数据库连接测试）：Windows下该参数没有用
TIMEOUT = 5

# $反向解析：name=$timetype  =>  name=cy  => name=year
URL_REFERENCE = {
    "cy": "year",
    "cm": "month",
    "shij": "shij_02",
    "shej": "shej_02"
}
# 程序内置extension，可以直接transformer=@xx使用
SYS_EXTENSIONS = ["", "groupby", "tb", "hb", "zb", "predict", "topkzb"]  # 系统内置extension

# 程序内置param_trans
SYS_PARAM_TRANS = ["qh2sheshixj", "qh_include_sub", "qh_godown", "year_range", "year2day", "xj2shij"]

# 程序内置value_map
SYS_VALUE_MAP = {
    "quarter": {"month->quarter": {"第一季度": "1|2|3", "第二季度": "4|5|6", "第三季度": "7|8|9", "第四季度": "10|11|12"}},
    "halfyear": {"month->halfyear": {"上半年": "1|2|3|4|5|6", "下半年": "7|8|9|10|11|12"}},
}

# 特殊参数，除这些参数以外，其他参数会在数据库中当作条件
# 如要修改特殊参数，在get_dataframe层的params_check中的params_check_for_each
# 键：特殊参数
# 值：字符串代表默认值，False 代表 不可为空或默认值无法表示
SYS_SPECIAL_PARAMS = {
    # 确定表的参数
    "realm": (False, None),
    "busin": ("", None),
    "timetype": ("", "cy|cm|cd"),
    "qh": ("", "xj|shij|shej"),
    "lx": ("", None),
    "index": ("", None),
    "table": ("", None),
    "db_engine": ("zb_db", "zb_db|fx_db"),
    
    # 查询数据库的字段
    "name": ("", None),
    "value": (False, None),
    "stack": ("", None),
    "direct_order": ("", None),
    "direct_limit": ("", "\d+"),

    # 辅助查询条件
    "order": ("", None),
    "limit": ("", "\d+|\d\s其他"),  # +会被浏览器转义成空格
    
    # 高级属性
    "transformer": ("@groupby", None),
    "full": ("true", None),
    "name_limit": ("", "\d+"),
    "stack_limit": ("", "\d+"),
    "ceil": ("", "\d+"),
    "ceil_value": (False, None),
    "param_protect": ("", "black_list\(.*?\)|white_list\(.*?\)|none"),
    "param_trans": (False, None),
    "tmp_search": ("", None),                 # 系统内部用于临时增加一个查询字段
    "debug": (False, None),
    "gd_id": ("", None),
    "time_format": (False, None),
    "ext": (False, None),
    "reindex": ("0", None),
    "sql_qhauth_auto": (False, None),         # 系统内部用于给sql模式传递qh条件(权限)
    "sql_qhauth_qh": (False, None),           # 系统内部用于给sql模式传递qh条件(权限)
    "sql_qhauth_sheshixj": (False, None),     # 系统内部用于给sql模式传递qh条件(权限)
    "sql_qhauth_other": (False, None),        # 系统内部用于给sql模式传递qh条件(权限)
    "dq_before": (False, None),               # 表格反查之前的指标图(data query before)
    "dq_after": (False, None),                # 表格反查之后的数据表(data query after)
    "graph_type": (False, None),              # 返回js-echarts-code
    "color": (False, None),                   # 返回js-echarts-code的图表颜色
    "style": (False, None),                   # 返回js-echarts-code的图表类型
    # "reuse": ("none", "none|waiting_for_search|db_results|df"),
    "value_map": (False, None),
}