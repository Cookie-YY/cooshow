from layers.makeup_dataframe import merge_initialized_table
from libs.extensions import Extension
import pandas as pd
import numpy as np


class Yjzt(Extension):
    """预警状态"""
    """
    计算公式：
        当同比或环比的绝对值超过20%即为告警，绝对值超过10%即为异常，否则为平稳

    """
    def __init__(self, apis_copy, apis, *args, **kwargs):
        # 执行父类方法，获得self.apis/self.apis_copy/self.value
        super(Yjzt, self).__init__(apis_copy, apis, *args, **kwargs)  # 执行父类方法，获得self.apis/self.apis_copy

    def before_search(self):
        self._before_search()  # 此时self.before_waiting_for_search中就有了最基本的内容
        condition_tb = Yjzt.params_parse_tb(self.apis.copy())
        condition_hb = Yjzt.params_parse_hb(self.apis.copy())

        condition_tb_container = self.before_waiting_for_search[0]["conditions"].copy()
        condition_hb_container = self.before_waiting_for_search[0]["conditions"].copy()
        condition_tb_container.append(condition_tb)
        condition_hb_container.append(condition_hb)

        # waiting_for_search = [{"conditions: [当前, 同比的上一阶段]"}, {"conditions: [当前, 环比的上一阶段]"}]
        self.before_waiting_for_search.append(self.before_waiting_for_search[0].copy())
        self.before_waiting_for_search[0]["conditions"] = condition_tb_container
        self.before_waiting_for_search[1]["conditions"] = condition_hb_container

        self.code, self.msg, self.waiting_for_search = Yjzt.get_waiting_for_search(self.before_waiting_for_search)


    def after_search(self):
        """
        self.db_results: [[df_my],[df_bmy],[df_jbmy]]
        :return:
        """
        # 获取结果
        self.db_results[0][0] = Extension.groupby_and_sum(self.db_results[0][0], self.value)
        self.db_results[0][1] = Extension.groupby_and_sum(self.db_results[0][1], self.value)
        self.db_results[1][0] = Extension.groupby_and_sum(self.db_results[1][0], self.value)
        self.db_results[1][1] = Extension.groupby_and_sum(self.db_results[1][1], self.value)

        if isinstance(self.db_results[0][0], pd.DataFrame) and self.db_results[0][0].shape[1] == 1 and self.db_results[0][0][self.value][0] is None:
            self.db_results[0][0] = np.int32(0)
        if isinstance(self.db_results[0][1], pd.DataFrame) and self.db_results[0][1].shape[1] == 1 and self.db_results[0][1][self.value][0] is None:
            self.db_results[0][1] = np.int32(0)
        if isinstance(self.db_results[1][0], pd.DataFrame) and self.db_results[1][0].shape[1] == 1 and self.db_results[1][0][self.value][0] is None:
            self.db_results[1][0] = np.int32(0)
        if isinstance(self.db_results[1][1], pd.DataFrame) and self.db_results[1][1].shape[1] == 1 and self.db_results[1][1][self.value][0] is None:
            self.db_results[1][1] = np.int32(0)

        df_tb, df_hb = Yjzt.calculate_tb_and_hb(self.db_results, self.apis_copy)

        self.apis_copy["value"] = "yjzt"
        if not isinstance(df_tb, pd.DataFrame) or not isinstance(df_hb, pd.DataFrame):
            res = "平稳"
            if abs(df_tb) > 0.2 or abs(df_hb) > 0.2:
                res = "告警"
            elif abs(df_tb) > 0.1 or abs(df_hb) > 0.1:
                res = "异常"
            self.df = pd.DataFrame({"yjzt": [res]})
            return

        df_tb = df_tb.rename(columns={self.value: "tb"})
        df_hb = df_hb.rename(columns={self.value: "hb"})
        on_list = list(df_hb.columns)
        on_list.remove("hb")
        # 如果on_list为空，说明不需要merge，只有一行，返回预警状态即可
        if not on_list:
            res = "平稳"
            if abs(df_tb["tb"][0]) > 0.2 or abs(df_hb["hb"][0]) > 0.2:
                res = "告警"
            elif abs(df_tb["tb"][0]) > 0.1 or abs(df_hb["hb"][0]) > 0.1:
                res = "异常"
            self.df = pd.DataFrame({"yjzt": [res]})
            return

        else:
            code, msg, df_tb = merge_initialized_table({"df": df_tb, "value": "tb"})  # 融合数据表：加 处理了day的初始化问题
            if code != 200:
                self.code = code
                self.msg = msg
                return
            code, msg, df_hb = merge_initialized_table({"df": df_hb, "value": "hb"})  # 融合数据表：加 处理了day的初始化问题
            if code != 200:
                self.code = code
                self.msg = msg
                return
            thb_df = pd.merge(df_tb, df_hb, how="left", on=on_list)

            def get_res(tb, hb):
                if abs(tb) > 0.2 or abs(hb) > 0.2:
                    return "告警"
                elif abs(tb) > 0.1 or abs(hb) > 0.1:
                    return "异常"
                return "平稳"

            # ycthb_df["yjzt"] = "平稳"
            thb_df["yjzt"] = thb_df.apply(lambda x: get_res(x["tb"], x["hb"]), axis=1)

            thb_df = thb_df.drop(['tb', 'hb'], axis=1)  # drop不会就地修改，创建副本返回
            self.df = thb_df

        
        
        # self.apis_copy["value"] = "yjzt"  # 不能放到前面，tb/hb解析的时候接受的db_results中的列名并没有改
        # res = "平稳"
        # if abs(df_tb) > 0.2 or abs(df_hb) > 0.2:
        #     res = "告警"
        # elif abs(df_tb) > 0.1 or abs(df_hb) > 0.1:
        #     res = "异常"
        # self.df = pd.DataFrame({"yjzt": [res]})
