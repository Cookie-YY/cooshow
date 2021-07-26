import datetime
import random

from flask import g

from libs.extension import Extension
import pandas as pd
import numpy as np
import statsmodels.api as sm
# from statsmodels.tsa.arima_model import ARIMA

from utils.init_date_valuelist import day_initialized


class Predict(Extension):
    """预测"""
    """
    after_search之后，会在g变量的predict_df中保存预测的df
    """
    # ext
    #   tb/hb/yjzt
    #   ext=include_before:                         涵盖之前的数据
    #   ext=only_predict：                          仅预测【默认】
    # 参数 ext_params-type@to:int
    #   type=int/float                              是否取整【默认int】
    #   p=1,d=1,q=1                                 预测的模型参数
    #   span=7d                                     预测的时长
    #   realdata_show=30d                           展示的时长（预测的时长是day参数）

    def __init__(self, apis_copy, apis, *args, **kwargs):
        # 执行父类方法，获得self.apis/self.apis_copy/self.value
        super(Predict, self).__init__(apis_copy, apis, *args, **kwargs)
        self.predict_unit = self.get_datetime_column()     # 增加一个搜索字段
        self.apis_copy["tmp_search"] = self.predict_unit   # 增加一个搜索字段
        self.span = self.process_predict_params()          # 预测的天数，解析后获得 整型
        today = datetime.date.today()
        begin_predict = today + datetime.timedelta(days=1)
        self.begin_predict = begin_predict.strftime("%Y-%m-%d")  # 得到开始预测的时间字符串
        end_predict = today + datetime.timedelta(days=self.span)
        self.end_predict = end_predict.strftime("%Y-%m-%d")      # 得到结束预测的时间字符串

    def after_search(self):
        """
        self.db_results:
        时间类型和预测的时间单位需要一致 (目前仅支持以天为单位)
        """
        df_beforepredict = Extension.groupby_and_sum(self.db_results[0][0], self.value)  # 找到search之后的结果

        # 2. groupby+预测   or   直接预测   [返回预测返回day+self.value]
        groupby = list(df_beforepredict.columns)
        groupby.remove(self.predict_unit)
        groupby.remove(self.value)
        if groupby:
            df = df_beforepredict.groupby(groupby).apply(lambda x: sum(self.predict_df(x)[self.value]))
            df = df.reset_index()
            df = df.rename(columns={0: self.value})
        else:
            # 传给预测函数的df必须只有两列：day/self.value
            df = self.predict_df(df_beforepredict)

        # 3.整理结果
        if self.apis_copy.get("name") == "day":
            pass
        elif not self.apis_copy.get("name"):
            df = pd.DataFrame({self.value: [df[self.value].sum()]})
        else:
            pass
        self.df = df
        g.predict_df = df

    def get_datetime_column(self):
        day_condition = self.apis_copy.get("day")
        date_condition = self.apis_copy.get("date")
        year_condition = self.apis_copy.get("year")
        if day_condition:
            return "day"
        if date_condition:
            return "date"
        if year_condition:
            return "year"
        return ""

    def predict_df(self, df):
        day_list = day_initialized(f"{self.begin_predict+' 00:00:00'},{self.end_predict+' 00:00:00'}")
        g.modified_initialization.update({"day": day_list})
        from app import app
        PREDICT_MIN_DATA = app.config.get("PREDICT_MIN_DATA", "")
        PREDICT_MIN_MULTI_DATA = app.config.get("PREDICT_MIN_MULTI_DATA", "")
        # 数量没有过阈值
        if (PREDICT_MIN_MULTI_DATA and df.shape[0] < PREDICT_MIN_MULTI_DATA*len(day_list)) or \
                (PREDICT_MIN_DATA and df.shape[0] < PREDICT_MIN_DATA):
            forecast = np.array([df[self.value].mean()] * self.span)  # 用mean值代替预测，个数和self.span一致

        # 过阈值了，开始预测
        else:
            forecast = self._predict_df(df)  # 预测个数和self.span一致
        if not self.kwargs.get("type") or self.kwargs.get("type") == "int":  # 是否需要对结果四舍五入取整
            forecast = np.around(forecast)
        # 结果处理
        return pd.DataFrame({self.value: forecast, "day": day_list})  # 当天的也算预测

    # 核心预测函数：目前仅支持天
    def _predict_df(self, df):
        # self.df_beforepredict (待预测的df)
        # predict_start, predict_end (经过处理的需要预测的时间跨度)

        # 整理查到的数据
        df = df[["day", self.value]]
        df.set_index('day', inplace=True)
        df = df.set_index(pd.to_datetime(df.index))
        pdates = pd.date_range(start=self.apis_copy.get("day").split(",")[0], end=self.apis_copy.get("day").split(",")[1])

        # 用于预测的数据中补零的策略
        df = df.reindex(pdates, fill_value=0)
        from app import app
        strategy, ratio = app.config["PREDICT_STRATEGY_FILL_NA"]
        if strategy == "mean":
            fill_na = df[self.value].mean()
            swag = fill_na * ratio
            df[self.value] = df[self.value].apply(lambda x: random.uniform(fill_na-swag, fill_na+swag) if x == 0 else x)

        # 如果外界指定参数，直接越过模型搜索
        p = int(self.kwargs.get("p", -1))  # 传递p和q就不用搜索了
        q = int(self.kwargs.get("q", -1))  # 传递p和q就不用搜索了
        d = self.kwargs.get("d") or 7      # 默认值是7
        if p == -1 or q == -1:
            (p, q) = (sm.tsa.arma_order_select_ic(df, max_ar=3, max_ma=3, ic='aic')['aic_min_order'])
        # 拟合模型
        model = sm.tsa.statespace.SARIMAX(df,
                                          order=(p, int(d), q),
                                          seasonal_order=(p, int(d), q, 7),
                                          enforce_stationarity=False,
                                          enforce_invertibility=False).fit()
        # 预测
        forecast = model.forecast(self.span)
        forecast = np.array(list(forecast))
        return np.where(forecast > 0, forecast, 0)

    def process_predict_params(self):
        span = 7
        if len(self.args) == 1:
            kwargs_span = self.kwargs.get("predict")  # kwargs里面的predict参数
            span_str = kwargs_span or self.args[0]    # args里面的第一个参数
            if str(span_str).endswith("d"):
                span = int(self.args[0].strip("d"))
        return span
        #     return span
        # else:
        #     return 7
        # return 7


