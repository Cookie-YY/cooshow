# -*- coding: utf-8 -*-
# @Time    : 2020/1/28 19:36
# @Author  : Cookie付尧
# @Email   : fuyao@beidasoft.com
# @File    : settings.py
# @Software: PyCharm
import os
import urllib.parse

############################## 数据库配置 ##############################
# 分析库：业务表和码表的位置
FX_DB = 'mysql+pymysql://root:Beidas0ft@39.107.240.28:3307/pt_dev_dabot_gd'
# FX_DB = 'mysql+pymysql://admin_xfxx3:%s@19.15.64.203:15133/zhxf_pre' % urllib.parse.unquote_plus('S65@aG3c')
# FX_DB = 'mysql+pymysql://admin_xfxx1:%s@19.15.64.203:15132/zhxf_gd' % urllib.parse.unquote_plus('5JFGPNe@')
# FX_DB = 'mysql+pymysql://root:%s@localhost:3306/sys' % urllib.parse.quote_plus("@123%")

# 指标库：指标表的位置
ZB_DB = 'mysql+pymysql://root:Beidas0ft@39.107.240.28:3306/pt_pro_dabot_gdauth'
# ZB_DB = 'mysql+pymysql://admin_xfxx8:%s@19.15.64.203:15152/zhxf_fzjc' % urllib.parse.unquote_plus("8cU5XQ%D")
# ZB_DB = 'mysql+pymysql://admin_xfxx7:%s@19.15.64.203:15151/zhxf_fzjc' % urllib.parse.unquote_plus("cDhZ2@zR")
# ZB_DB = 'mysql+pymysql://root:%s@localhost:3306/pt_dev_dabot_gd_zb' % urllib.parse.quote_plus("Beidas0ft")


############################### 缓存配置 ###############################
# CACHE_TYPE = "redis"
CACHE_TYPE = "null"
CACHE_REDIS_HOST = '127.0.0.1'
CACHE_REDIS_PORT = 6379
CACHE_REDIS_DB = ''
CACHE_REDIS_PASSWORD = ''
CACHE_TIMEOUT = 60 * 60 * 24  # 60s * 60min * 24h


############################### 前端配置 ###############################
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))

# 前端大屏相关
DP_CONTAINER = "client"         # 大屏的根路径
DP_ROOT = "gdxfdp"

DP_DIR_1 = "AidDecisionMaking"  # 为空或者相对于DP_ROOT的路径
DP_URL_1 = "AidDecisionMaking"  # 访问大屏的url（不用写/）

DP_DIR_2 = "LeadCockpit"
DP_URL_2 = "LeadCockpit"        # 访问大屏的url（不用写/）

DP_DIR_3 = "assistant"
DP_URL_3 = "assistant"        # 访问大屏的url（不用写/）

# 头像等获取的文件的地址
FILE_URL = f"/{DP_ROOT}/file/"
FILE_PATH = os.path.join(BASE_DIR, DP_CONTAINER, DP_ROOT, "file")


############################### 权限配置 ###############################
LOGIN_AUTH = False  # 为True时需要满足用户名密码的要求
LEVEL_AUTH = True   # 为True时必须指定 LEVEL_AUTH_COOKIE
LEVEL_AUTH_PARAM = "xzqh"     # 参数中控制权限的参数（跳转到大屏时获得该参数）
LEVEL_AUTH_COOKIE = "xzqhdm"  # cookie中控制权限的参数（写到cookie中给前端）
LEVEL_AUTH_ENCRYPT = False


############################### 参数配置 ###############################
# 特殊参数，除这些参数以外，其他参数会在数据库中当作条件
# 如要修改特殊参数，在get_dataframe层的params_check中的params_check_for_each
# 键：特殊参数
# 值：字符串代表默认值，False 代表 不可为空或默认值无法表示
# 【系统的特殊参数在查表时检查，项目自定义的特殊参数在程序一开始和查表时都检查】
# 有param_trans param_trans的开关才算打开，否则不走param_trans
CUS_SPECIAL_PARAMS = {"busin": ("xfj", None), "xzqh": (False, "\d{6}"), "param_trans": ("qh2sheshixj,wx_map", None), "full": ("true", None)}
CUS_PARAM_TRANS = ["wx_map", "xfbm_godown", "zrdw_godown", "djjg_qhauth", "xfbm_qhauth", "zrdw_qhauth", "xfbmsearch_qhauth", "zrdwsearch_qhauth", "find_qh_from_xfbm", "last_day"]

############################### 数据配置 ###############################
# 随机化配置
RANDOM_OR_ZERO = "ZERO"
EFFICIENT_DIGITS = 4     # VALUE_FLOAT的小数位数，不写默认为4
RANDOM_INT_LOWER = 100   # VALUE_INT的随机化的最小值，不写默认100
RANDOM_INT_UPPER = 999   # VALUE_INT的随机化的最大值，不写默认999

# 没有表时，是否报错（NoSuchTableError）
NOTABLE_ERROR = True
# 没有字段时，是否报错（NoSuchColumnError）
NOCOLUMN_ERROR = True

# 计算后（占比/同比/环比）保留的小数位数，可能百分比显示
SIGNIFICANT_DIGITS = 4

# 项目默认的时间格式：当name=day时生效，如果不写或为空：%Y-%m-%d
TIME_FORMAT = "%Y-%m-%d"

# 时间的精确配置
DATE_START = "00:00:00"
DATE_END = "23:59:59"

# df的数值映射 默认所有字段都开启，如果需要关闭特定的接口中的特定的字段，需指定参数，支持正则
# get_dataframe阶段的第一步simpele2df时执行[只要走父类的params_search就会走下面的数据映射]
VALUE_MAP = {
    "global_wx": {"xfxs": {"网信": "(^(?!来信$))(^(?!来访$))"}},
    "quarter": {"month->quarter": {"第一季度": "1|2|3", "第二季度": "4|5|6", "第三季度": "7|8|9", "第四季度": "10|11|12"}},
    "halfyear": {"month->halfyear": {"上半年": "1|2|3|4|5|6", "下半年": "7|8|9|10|11|12"}},
    "dsr_type": {},
}

# plugin过程中的sql模式中的内容映射，主要用于大表格的反查，支持正则，格式和VALUE_MAP一样
VALUE_MAP_FOR_PLUGIN_SQL = {
    "global_wx": {"xfxs": {"网信": "(^(?!来信$))(^(?!来访$))"}},
}

# 初始化指标需要的txt文件夹位置
INITIALIZATION_FILE_PATH = os.path.join(SETTINGS_DIR, "init_files")
INITIALIZATION_FILE_SEP = "\t"
INITIALIZATION_FILE_MAP = {    # 初始化项目时会在init_dicts中增加yjnr/ej_nr/sj_nr, 值是用seq分隔的字段并集
    "yjnr+ejnr+sjnr": {
        "init_dicts": ["yjnr", "ej_nr", "sj_nr"],
        "sep": "_"
    }
}

# 自定义extensions
CUS_EXTENSIONS = ["mylv", "cplv", "jssllv", "yjzt", "aqdflv", "wxzb", "yctb", "ychb", "ycyjzt", "chuj", "cfxflv"]

# 禁止full的情况
DISABLE_FULL_WHEN_NAME = ["xm"]
DISABLE_FULL_WHEN_VALUE = ["shej_02", "shij_02", "xj_02"]

# predict（ext）的参数
# 最小可供预测的数据，否则将均值作为预测结果
PREDICT_MIN_DATA = 20            # 用于预测的最小的训练集的样本量
PREDICT_MIN_MULTI_DATA = 3       # 用于预测的最小的训练集的样本量的倍数，如，预测7天，最少需要21天
PREDICT_STRATEGY_FILL_NA = ("mean", 0.1)   # 补零基准("mean" or "zero")      震荡幅度(当zero时 幅度没用)
############################### 调试配置 ###############################
# SQLALCHEMY_ECHO = True

# DEBUG模式开关（仅开发模式有用）
DEBUG = True

