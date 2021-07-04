import os
import sys


class ConfigCheck:
    def __init__(self, config):
        self.config = config
        [getattr(ConfigCheck, i)(self) for i in ConfigCheck.__dict__ if i.startswith("check")]

    # SPECIAL_PARAMS
    def check_SPECIAL_PARAMS(self):
        # 对象：特殊参数的配置
        # 作用：赋予默认值/有特殊含义(不作为筛选条件)
        # 格式标准：SPECIAL_PARAMS = {"demo": (False, "")}
        # 内容标准：在参数中预先定义
        SPECIAL_PARAMS = self.config.get("SPECIAL_PARAMS", {})
        for k, v in SPECIAL_PARAMS.items():
            if not ((v[0] is False or isinstance(v[0], str)) and
                    (v[1] is None or isinstance(v[1], str))):
                sys.exit("ConfigError[SPECIAL_PARAMS]: The element in SPECIAL_PARAMS must be as follow "
                         "(False or str, str)")

    # 必须有shej_02+shij_02+xj_02的文件 或者是  shij_02+xj_02
    def check_INITIALIZATION_FILE_PATH(self):
        INITIALIZATION_FILE_PATH = self.config.get("INITIALIZATION_FILE_PATH")
        if not INITIALIZATION_FILE_PATH:
            sys.exit("ConfigError[INITIALIZATION_FILE_PATH]: Missing INITIALIZATION_FILE_PATH")
        cond1 = "shej_02+shij_02+xj_02" in os.listdir(INITIALIZATION_FILE_PATH)
        cond2 = "shij_02+xj_02" in os.listdir(INITIALIZATION_FILE_PATH)
        if not(cond1 or cond2):
            sys.exit("ConfigError[INITIALIZATION_FILE_PATH]: There should be file "
                     "named [shej_02+shij_02+xj_02] or [shij_02+xj_02] in config INITIALIZATION_FILE_PATH")

    # plgin的检查：从check_plugin中拿出来
    # 开了LEVEL_AUTH 但是没有 LEVEL_AUTH_MAP 或者 没有 LEVEL_AUTH_PARAM和LEVEL_AUTH_COOKIE