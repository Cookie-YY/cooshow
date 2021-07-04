import platform

from app import app
from utils.db_connection import zb_engine, fx_engine
from utils.timeout import timeout

TIMEOUT = app.config["TIMEOUT"]


# @timeout(TIMEOUT, error_message="ConnectionError")  # windows系统需要注释掉这一行
def connect_db_test(engine, name):
    engine.connect()
    print(f"{name}：{engine.url}")


def env_test():
    # 连接数据库的测试
    if platform.system() == "Windows":
        connect_db_test(fx_engine, "分析库")
        connect_db_test(zb_engine, "指标库")
    else:
        timeout(TIMEOUT, error_message="ConnectionError")(connect_db_test(fx_engine, "分析库"))
        timeout(TIMEOUT, error_message="ConnectionError")(connect_db_test(zb_engine, "指标库"))


if __name__ == '__main__':
    env_test()


