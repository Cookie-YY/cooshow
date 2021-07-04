import re
import threading
import urllib.parse

import pymysql
from sqlalchemy import create_engine
from sqlalchemy import MetaData


def get_db_dict(url):
    pattern = "(.*?)\+(.*?)://(.*?):(.*)@(.*?):(.*?)/(.*)"
    res = re.findall(pattern, url)
    if not res:
        exit("请检查url拼写")
    dbtype, driver, user, passwd, ip, port, dbname = res[0]
    return {"host": ip, "port": int(port), "user": user, "passwd": urllib.parse.unquote_plus(passwd), "db": dbname, "charset": "utf8"}

# INDEX_DB = 'mysql+pymysql://root:Beidas0ft@39.107.240.28:3306/pt_dev_dabot'
from app import app

ZB_DB = app.config.get("ZB_DB")
FX_DB = app.config.get("FX_DB")

FX_DB_DICT = get_db_dict(FX_DB)
ZB_DB_DICT = get_db_dict(ZB_DB)

class SigleConect:
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(SigleConect, "_instance"):
            with SigleConect._instance_lock:
                if not hasattr(SigleConect, "_instance"):
                    SigleConect._instance = object.__new__(cls)
        return SigleConect._instance

    def __init__(self):
        print("should only once")
        # pymysql的数据库连接
        self.fx_pymysql = pymysql.connect(**FX_DB_DICT)
        self.zb_pymysql = pymysql.connect(**ZB_DB_DICT)

        # sqlalchemy的数据库连接
        self.zb_engine = create_engine(ZB_DB,
                                  pool_recycle=-1,
                                  pool_size=100,
                                  max_overflow=0)

        self.fx_engine = create_engine(FX_DB,
                                  pool_recycle=-1,
                                  pool_size=5,
                                  max_overflow=0)

        self.metadata = MetaData()

sc = SigleConect()
fx_pymysql = sc.fx_engine
zb_pymysql = sc.zb_pymysql
zb_engine = sc.zb_engine
fx_engine = sc.fx_engine
metadata = sc.metadata