import datetime

from layers.makeup_dataframe import merge_initialized_table
from libs.extensions import Extension
import pandas as pd
import numpy as np
from flask import g

from libs.extensions.tb import Tb


class Ycyjzt(Extension):
    """预测预警状态"""
    """
    计算公式：
        当同比或环比的绝对值超过20%即为告警，绝对值超过10%即为异常，否则为平稳
    """
    def __init__(self, apis_copy, apis, *args, **kwargs):
        # 执行父类方法，获得self.apis/self.apis_copy/self.value
        super(Ycyjzt, self).__init__(apis_copy, apis, *args, **kwargs)  # 执行父类方法，获得self.apis/self.apis_copy
        self.span = 0  # 预测的天数，解析后获得
        self.today = datetime.date.today()

        # self.process_predict_params()  # 解析参数
        # day_start = self.today - datetime.timedelta(days=self.span)
        # day_start = day_start.strftime("%Y-%m-%d %H:%M:%S")
        # day_end = self.today
        # day_end = day_end.strftime("%Y-%m-%d %H:%M:%S")
        # self.apis["day"] = f"{day_start},{day_end}"

    # before_search用的就是Tb中的before_search


    if isinstance(g.get("yctb_df", ""), pd.DataFrame) and isinstance(g.get("ychb_df", ""), pd.DataFrame):  # 如果之前算过同环比
        def before_search(self):
            return

        def after_search(self):
            self.apis_copy["value"] = "yjzt"
            yctb_df = g.get("yctb_df", "")
            ychb_df = g.get("ychb_df", "")

            on_list = list(ychb_df.columns)
            on_list.remove("hb")
            # 如果on_list为空，说明不需要merge，只有一行，返回预警状态即可
            if not on_list:
                res = "平稳"
                if abs(yctb_df["tb"][0]) > 0.2 or abs(ychb_df["hb"][0]) > 0.2:
                    res = "告警"
                elif abs(yctb_df["tb"][0]) > 0.1 or abs(ychb_df["hb"][0]) > 0.1:
                    res = "异常"
                self.df = pd.DataFrame({"yjzt": [res]})
                return

            else:
                code, msg, yctb_df = merge_initialized_table({"df": yctb_df, "value": "tb"})  # 融合数据表：加 处理了day的初始化问题
                if code != 200:
                    self.code = code
                    self.msg = msg
                    return
                code, msg, ychb_df = merge_initialized_table({"df": ychb_df, "value": "hb"})  # 融合数据表：加 处理了day的初始化问题
                if code != 200:
                    self.code = code
                    self.msg = msg
                    return
                ycthb_df = pd.merge(yctb_df, ychb_df, how="left", on=on_list)

                def get_res(tb, hb):
                    if abs(tb) > 0.2 or abs(hb) > 0.2:
                        return "告警"
                    elif abs(tb) > 0.1 or abs(hb) > 0.1:
                        return "异常"
                    return "平稳"

                # ycthb_df["yjzt"] = "平稳"
                ycthb_df["yjzt"] = ycthb_df.apply(lambda x: get_res(x["tb"], x["hb"]), axis=1)

                ycthb_df = ycthb_df.drop(['tb', 'hb'], axis=1)  # drop不会就地修改，创建副本返回
                self.df = ycthb_df


    else:

        def after_search(self):
            if isinstance(g.get("predict_df", ""), pd.DataFrame):  # 如果之前算过预测的df了，直接复用
                self.db_results[0][0] = g.get("predict_df")
            Tb.after_search(self)
            g.yctb_df = self.df

        def process_predict_params(self):
            if len(self.args) == 1:
                span = 7
                kwargs_span = self.kwargs.get("predict")  # kwargs里面的predict参数
                span_str = kwargs_span or self.args[0]    # args里面的第一个参数
                if str(span_str).endswith("d"):
                    span = int(self.args[0].strip("d"))
                self.span = span
            else:
                return