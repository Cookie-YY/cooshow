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
FX_DB = 'mysql+pymysql://root:Beidas0ft@39.107.240.28:3307/pt_dev_dabot'
# FX_DB = 'mysql+pymysql://root:Beidas0ft@193.168.15.25:3306/pt_dev_dabot'
# FX_DB = 'mysql+pymysql://root:Beidas0ft@127.0.0.1:3306/pt_dev_test'

# 指标库：指标表的位置
ZB_DB = 'mysql+pymysql://root:Beidas0ft@39.107.240.28:3306/pt_dev_dabot_hb'
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
DP_CONTAINER = "client"    # 大屏的根路径
DP_ROOT = "hbxfdp"

DP_DIR = ""
DP_URL = "hbxfdp"          # 访问大屏的url（不用写/）

# 头像等获取的文件的地址
FILE_URL = f"/{DP_ROOT}/file/"
FILE_PATH = os.path.join(BASE_DIR, DP_CONTAINER, DP_ROOT, "file")


############################### 参数配置 ###############################
# 特殊参数，除这些参数以外，其他参数会在数据库中当作条件
# 如要修改特殊参数，在get_dataframe层的params_check中的params_check_for_each
# 键：特殊参数
# 值：字符串代表默认值，False 代表 不可为空或默认值无法表示
# 【系统的特殊参数在查表时检查，项目自定义的特殊参数在程序一开始和查表时都检查】
# 有param_trans param_trans的开关才算打开，否则不走param_trans
CUS_SPECIAL_PARAMS = {"busin": ("xfj", None), "full": (False, None)}
# CUS_PARAM_TRANS = ["wx_map"]


############################### 数据配置 ###############################
# 随机化配置
RANDOM_OR_ZERO = "RANDOM"
EFFICIENT_DIGITS = 4     # VALUE_FLOAT的小数位数，不写默认为4
RANDOM_INT_LOWER = 100   # VALUE_INT的随机化的最小值，不写默认100
RANDOM_INT_UPPER = 999   # VALUE_INT的随机化的最大值，不写默认999

# 关闭NoTableError的报错
NOTABLE_ERROR = True

# 计算后（占比/同比/环比）保留的小数位数，可能百分比显示
SIGNIFICANT_DIGITS = 4

# 项目默认的时间格式：当name=day时生效，如果不写或为空：%Y-%m-%d
TIME_FORMAT = "%Y-%m-%d"

# df的数值映射 默认所有字段都开启，如果需要关闭特定的接口中的特定的字段，需指定参数，支持正则
# get_dataframe阶段的第一步simpele2df时执行
VALUE_MAP = {"xfxs": {"网信": "网上投诉|短信信访|微博信访|网上建议"}}

# plugin过程中的sql模式中的内容映射，主要用于大表格的反查，支持正则，格式和VALUE_MAP一样
VALUE_MAP_FOR_PLUGIN_SQL = {}

# 初始化指标需要的txt文件夹位置
INITIALIZATION_FILE_PATH = os.path.join(SETTINGS_DIR, "init_files")

# 自定义extensions
CUS_EXTENSIONS = []

# 有关联关系的字段
RELATION_COLS = ["shej_02+shij_02+xj_02", "yjnr+ejnr+sjnr"]

############################### 调试配置 ###############################
# SQLALCHEMY_ECHO = True

# DEBUG模式开关（仅开发模式有用）
DEBUG = True

# 特殊参数，除这些参数以外，其他参数会在数据库中当作条件
# 如要修改特殊参数，在get_dataframe层的params_check中的params_check_for_each
# 键：特殊参数
# 值：字符串代表默认值，False 代表 不可为空或默认值无法表示




