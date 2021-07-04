import datetime

from libs.extensions import Extension
import pandas as pd
import numpy as np
from flask import g

from libs.extensions.tb import Tb


class Yctb(Tb):
    """预测同比"""
    """
    计算公式：
        必须跟在transformer=predict之后（从g中获取predict_df）
    """
    def __init__(self, apis_copy, apis, *args, **kwargs):
        # 执行父类方法，获得self.apis/self.apis_copy/self.value
        super(Yctb, self).__init__(apis_copy, apis, *args, **kwargs)  # 执行父类方法，获得self.apis/self.apis_copy
        self.span = 0  # 预测的天数，解析后获得
        self.today = datetime.date.today()

        self.process_predict_params()  # 解析参数
        day_start = self.today - datetime.timedelta(days=self.span)
        day_start = day_start.strftime("%Y-%m-%d %H:%M:%S")
        day_end = self.today
        day_end = day_end.strftime("%Y-%m-%d %H:%M:%S")
        self.apis["day"] = f"{day_start},{day_end}"

    # before_search用的就是Tb中的before_search

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