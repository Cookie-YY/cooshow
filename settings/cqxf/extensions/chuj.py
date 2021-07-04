"""
    # 全局业务监控-重复信访监控
    # xf_xfj_cd_xj_cfxfbz_xfjc      xf_xfj_cd_xj_xfjc
    # 这里的逻辑很奇怪，全局只有这里用到transformer=cjzb（重件占比）
    "全局业务监控_重复信访监控_重件占比$": "http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_cfxfbz_xfjc&transformer=@cjzb&Cqh=广东省&day=[2020-01-01,2020-11-10]&full=none&param_trans=qh_include_sub",
"""

from layers.makeup_dataframe import merge_initialized_table
from libs.extensions import Extension
import pandas as pd
import numpy as np


class Chuj(Extension):
    """初件"""
    """
    计算公式：
        总数-重件

    """

    def __init__(self, apis_copy, apis, *args, **kwargs):
        # 执行父类方法，获得self.apis/self.apis_copy/self.value
        super(Chuj, self).__init__(apis_copy, apis, *args, **kwargs)  # 执行父类方法，获得self.apis/self.apis_copy

    def before_search(self):
        self._before_search()  # 此时self.before_waiting_for_search中就有了最基本的内容
        # self.before_waiting_for_search.append(self.before_waiting_for_search[0].copy())
        self.before_waiting_for_search[0]["table"] = self.apis_copy.get("table").replace("cfxfbz_", "")
        self.before_waiting_for_search[0]["ex_table"] = None

        self.code, self.msg, self.waiting_for_search = Chuj.get_waiting_for_search(self.before_waiting_for_search)

    def after_search(self):
        """
        self.db_results: [[df_my],[df_bmy],[df_jbmy]]
        :return:
        """
        # 获取结果
        from flask import g
        df_chongjian = g.get("df")
        df_all = Extension.groupby_and_sum(self.db_results[0][0], self.value)
        # self.db_results[0][1] = Extension.groupby_and_sum(self.db_results[0][1], self.value)
        # self.db_results[1][0] = Extension.groupby_and_sum(self.db_results[1][0], self.value)
        # self.db_results[1][1] = Extension.groupby_and_sum(self.db_results[1][1], self.value)

        if isinstance(df_chongjian, pd.DataFrame) and df_chongjian.shape[1] == 1 and \
                df_chongjian[self.value][0] is None:
            df_chongjian = np.int32(0)
        # if isinstance(self.db_results[0][1], pd.DataFrame) and self.db_results[0][1].shape[1] == 1 and \
        #         self.db_results[0][1][self.value][0] is None:
        #     self.db_results[0][1] = np.int32(0)
        if isinstance(df_all, pd.DataFrame) and df_all.shape[1] == 1 and \
                df_all[self.value][0] is None:
            df_all = np.int32(0)
        # if isinstance(self.db_results[1][1], pd.DataFrame) and self.db_results[1][1].shape[1] == 1 and \
        #         self.db_results[1][1][self.value][0] is None:
        #     self.db_results[1][1] = np.int32(0)

        # df_tb, df_hb = Yjzt.calculate_tb_and_hb(self.db_results, self.apis_copy)
        # df_tb = df_hb.rename(columns={self.value: "tb"})
        # df_hb = df_hb.rename(columns={self.value: "hb"})

        # self.apis_copy["value"] = "zb"
        if not isinstance(df_chongjian, pd.DataFrame) or not isinstance(df_all, pd.DataFrame):
            self.df = pd.DataFrame({"xfjc": [df_all - df_chongjian]})
            return

        on_list = list(df_chongjian.columns)
        on_list.remove("xfjc")
        # self.apis_copy["value"] = "yjzt"
        # 如果on_list为空，说明不需要merge，只有一行，返回预警状态即可
        if not on_list:
            self.df = pd.DataFrame({"xfjc": [df_all["xfjc"][0]-df_chongjian["xfjc"][0]]})
            return

        else:
            code, msg, df_chongjian = merge_initialized_table({"df": df_chongjian, "value": "xfjc"})  # 融合数据表：加 处理了day的初始化问题
            if code != 200:
                self.code = code
                self.msg = msg
                return
            code, msg, df_all = merge_initialized_table({"df": df_all, "value": "xfjc"})  # 融合数据表：加 处理了day的初始化问题
            if code != 200:
                self.code = code
                self.msg = msg
                return
            df_all = df_all.rename(columns={self.value: "all"})            
            df_chujian = pd.merge(df_chongjian, df_all, how="left", on=on_list)

            def get_res(xfjc, all):
                res = 0
                if xfjc * all:
                    res = xfjc - all
                return res

            df_chujian["xfjc"] = df_chujian.apply(lambda x: get_res(x[self.value], x["all"]), axis=1)

            zb_df = df_chujian.drop(['all'], axis=1)  # drop不会就地修改，创建副本返回
            self.df = zb_df

        # self.apis_copy["value"] = "yjzt"  # 不能放到前面，tb/hb解析的时候接受的db_results中的列名并没有改
        # res = "平稳"
        # if abs(df_tb) > 0.2 or abs(df_hb) > 0.2:
        #     res = "告警"
        # elif abs(df_tb) > 0.1 or abs(df_hb) > 0.1:
        #     res = "异常"
        # self.df = pd.DataFrame({"yjzt": [res]})
