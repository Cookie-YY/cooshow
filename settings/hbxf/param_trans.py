from flask import g  # 用于存放变化后的init_dicts
from libs.param_trans import ParamTrans


class PT(ParamTrans):
    # 获得 qh2sheshixj/qh_include_sub/qh_godown
    def __init__(self, apis_copy):
        super(PT, self).__init__(apis_copy)   # 得到self.apis_copy
