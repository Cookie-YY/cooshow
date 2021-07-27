import os
import urllib.parse
from settings import PROJECT

############################### Directory settings ###############################
SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(SETTINGS_DIR))


############################### DataBase settings ###############################
# SRC_DB: Raw database which save records.
SRC_DB = 'sqlite://{}'.format(os.path.join(BASE_DIR, "demo.sqlite"))
# DEST_DB: Dest database which save results calculated from records
DEST_DB = 'sqlite://{}'.format(os.path.join(BASE_DIR, "demo.sqlite"))


############################### Cache settings ###############################
# When CACHE_TYPE="null", the other settings about cache will be ignored
CACHE_TYPE = "null"               # "redis"/"null"
CACHE_REDIS_HOST = '127.0.0.1'
CACHE_REDIS_PORT = 6379
CACHE_REDIS_DB = ''
CACHE_REDIS_PASSWORD = ''         # '' if no password
CACHE_TIMEOUT = 60 * 60 * 24      # 60s * 60min * 24h


############################### FrontEnd settings ###############################
FRONT_DIR = os.path.join(BASE_DIR, "client")
FRONT_PROJECT = PROJECT
# File settings.
FILE_URL = f"/{FRONT_PROJECT}/file/"
FILE_PATH = os.path.join(FRONT_DIR, FRONT_PROJECT, "file")
# Specific front-end project, you can specify more than one project.
# Each front-end project should has its SHOW_INDEX_FILE.
SHOW_URL = "demo"                      # url:   http:{host}:{port}/{SHOW_URL}
SHOW_DIR = "demo"
SHOW_INDEX_FILE = "index.html"         # path:  {FRONT_DIR}/{FRONT_PROJECT}/{SHOW_INDEX_FILE}
# SHOW_URL_1 = "demo"
# SHOW_DIR_1 = "demo1"
# SHOW_INDEX_FILE_1 = "index.html"


############################### Auth/Login settings ###############################
LOGIN_AUTH = False  # 为True时需要满足用户名密码的要求
LEVEL_AUTH = True  # 为True时必须指定 LEVEL_AUTH_COOKIE
LEVEL_AUTH_PARAM = "xzqh"  # 参数中控制权限的参数（跳转到大屏时获得该参数）
LEVEL_AUTH_COOKIE = "xzqhdm"  # cookie中控制权限的参数（写到cookie中给前端）
LEVEL_AUTH_ENCRYPT = False

############################### Params settings ###############################
# 特殊参数，除这些参数以外，其他参数会在数据库中当作条件
# 如要修改特殊参数，在get_dataframe层的params_check中的params_check_for_each
# 键：特殊参数
# 值：字符串代表默认值，False 代表 不可为空或默认值无法表示
# 【系统的特殊参数在查表时检查，项目自定义的特殊参数在程序一开始和查表时都检查】
# 有param_trans param_trans的开关才算打开，否则不走param_trans
CUS_SPECIAL_PARAMS = {"busin": ("xfj", None), "xzqh": (False, "\d{6}"), "param_trans": ("is_ga,qh2sheshixj", None),
                      "full": ("none", None)}
CUS_PARAM_TRANS = ["is_ga"]
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
############################### Data settings ###############################
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
DATE_END = "00:00:00"

# df的数值映射 默认所有字段都开启，如果需要关闭特定的接口中的特定的字段，需指定参数，支持正则
# get_dataframe阶段的第一步simpele2df时执行[只要走父类的params_search就会走下面的数据映射]
CUS_VALUE_MAP = {
}
# plugin过程中的sql模式中的内容映射，主要用于大表格的反查，支持正则，格式和VALUE_MAP一样
VALUE_MAP_FOR_PLUGIN_SQL = {
}
# 初始化指标需要的txt文件夹位置
INITIALIZATION_FILE_PATH = os.path.join(SETTINGS_DIR, "init_files")
INITIALIZATION_FILE_SEP = "\t"

# 自定义extensions
CUS_EXTENSIONS = ["mylv", "cplv", "jssllv", "yjzt", "aqdflv", "wxzb", "yctb", "ychb", "ycyjzt", "cjzb"]

# 有关联关系的字段
RELATION_COLS = ["shej_02+shij_02+xj_02", "yjnr+ejnr+sjnr"]

# 禁止full的情况
DISABLE_FULL_WHEN_NAME = ["xm"]
DISABLE_FULL_WHEN_VALUE = ["shej_02", "shij_02", "xj_02"]

# predict（ext）的参数
# 最小可供预测的数据，否则返回均值
PREDICT_MIN_DATA = 20  # 用于预测的最小的训练集的样本量
PREDICT_MIN_MULTI_DATA = 3  # 用于预测的最小的训练集的样本量的倍数，如，预测7天，最少需要21天
PREDICT_STRATEGY_FILL_NA = ("mean", 0.1)  # 补零基准      震荡幅度(相对于均值)


############################### Debug settings ###############################
# SQLALCHEMY_ECHO = True

# DEBUG模式开关（仅开发模式有用）
DEBUG = True
