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
FX_DB = 'mysql+pymysql://root:Beidas0ft@39.107.240.28:3307/pt_dev_dabot_yn'
# FX_DB = 'mysql+pymysql://root:Beidas0ft@193.168.15.25:3306/pt_dev_dabot'
# FX_DB = 'mysql+pymysql://root:Beidas0ft@127.0.0.1:3306/pt_dev_test'

# 指标库：指标表的位置
ZB_DB = 'mysql+pymysql://root:Beidas0ft@39.107.240.28:3306/pt_dev_dabot_yn'
# ZB_DB = 'mysql+pymysql://root:Beidas0ft@193.168.15.25:3306/pt_dev_dabot_zb'
# ZB_DB = 'mysql+pymysql://root:Beidas0ft@127.0.0.1:3306/test'


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
DP_CONTAINER = "client"  # 大屏的根路径
DP_ROOT = "ynxfdp"

DP_DIR = ""
DP_URL = "ynxfdp"  # 访问大屏的url

# 头像等获取的文件的地址
FILE_URL = f"/{DP_ROOT}/file/"
FILE_PATH = os.path.join(BASE_DIR, DP_CONTAINER, DP_ROOT, "file")

############################### 权限配置 ###############################
LOGIN_AUTH = False  # 为True时需要满足用户名密码的要求
LEVEL_AUTH = True  # 为True时必须指定 LEVEL_AUTH_COOKIE
LEVEL_AUTH_PARAM = "xzqh"  # 参数中控制权限的参数（跳转到大屏时获得该参数）
LEVEL_AUTH_COOKIE = "xzqhdm"  # cookie中控制权限的参数（写到cookie中给前端）
LEVEL_AUTH_ENCRYPT = False

############################### 参数配置 ###############################
# 特殊参数，除这些参数以外，其他参数会在数据库中当作条件
# 如要修改特殊参数，在get_dataframe层的params_check中的params_check_for_each
# 键：特殊参数
# 值：字符串代表默认值，False 代表 不可为空或默认值无法表示
# 【系统的特殊参数在查表时检查，项目自定义的特殊参数在程序一开始和查表时都检查】
# 有param_trans param_trans的开关才算打开，否则不走param_trans
CUS_SPECIAL_PARAMS = {}
CUS_PARAM_TRANS = ["year2day"]

############################### 数据配置 ###############################
# 随机化配置
RANDOM_OR_ZERO = "ZERO"
EFFICIENT_DIGITS = 4  # VALUE_FLOAT的小数位数，不写默认为4
RANDOM_INT_LOWER = 100  # VALUE_INT的随机化的最小值，不写默认100
RANDOM_INT_UPPER = 999  # VALUE_INT的随机化的最大值，不写默认999

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
CUS_VALUE_MAP = {
    "global_qh": {
        "shij_02": {"红河州": ".*红河.*",  # 红河哈尼族彝族自治州
                    "文山州": ".*文山.*",  # 文山壮族苗族自治州
                    "西双版纳": ".*西双版纳.*",  # 西双版纳傣族自治州
                    "大理州": ".*大理.*",  # 大理白族自治州
                    "德宏州": ".*德宏.*",  # 德宏傣族景颇族自治州
                    "怒江州": ".*怒江.*",  # 怒江傈僳族自治州
                    "迪庆州": ".*迪庆.*",  # 迪庆藏族自治州
                    "楚雄州": ".*楚雄.*"}  # 楚雄彝族自治州
    },
}

# plugin过程中的sql模式中的内容映射，主要用于大表格的反查，支持正则，格式和VALUE_MAP一样
VALUE_MAP_FOR_PLUGIN_SQL = {"xfxs": {"网信": "(^(?!来信$))(^(?!来访$))"}}

# 初始化指标需要的txt文件夹位置
INITIALIZATION_FILE_PATH = os.path.join(SETTINGS_DIR, "init_files")
INITIALIZATION_FILE_SEP = "\t"

# 自定义extensions
CUS_EXTENSIONS = ["yctb", "ychb", "ycyjzt", "yjzt"]

# 有关联关系的字段
RELATION_COLS = ["shej_02+shij_02+xj_02", "yjnr+ejnr+sjnr"]

# 禁止full的情况
DISABLE_FULL_WHEN_NAME = ["xm"]
DISABLE_FULL_WHEN_VALUE = ["shej_02", "shij_02", "xj_02"]

# 自定义颜色系列
COLOR_SERIES = {
    "Embedding": [  # 嵌套图的颜色
        ['#5164ff', '#96a2ff', '#6d7dff'],  # 蓝色系
        ['#3fcfdb', '#39dbc5', '#47c0f6'],  # 青色系
        ['#b04aff', '#c1a4ff', '#a176ff'],  # 紫色系
        ['#fd9f8c', '#f9bc95', '#ff8c86'],  # 橙色系
        # ['#8dc1a9', '#ea7e53', '#73b9bc']   # 紫色系【没用上，目前只要前4个】
    ],
}

# predict（ext）的参数
# 最小可供预测的数据，否则返回均值
PREDICT_MIN_DATA = 20  # 用于预测的最小的训练集的样本量
PREDICT_MIN_MULTI_DATA = 3  # 用于预测的最小的训练集的样本量的倍数，如，预测7天，最少需要21天
PREDICT_STRATEGY_FILL_NA = ("mean", 0.1)  # 补零基准      震荡幅度(相对于均值)
############################### 调试配置 ###############################
# SQLALCHEMY_ECHO = True

# DEBUG模式开关（仅开发模式有用）
DEBUG = True
