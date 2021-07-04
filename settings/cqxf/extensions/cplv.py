from libs.extensions import Extension
import pandas as pd
import numpy as np


class Cplv(Extension):
    """参评率"""
    """
    计算公式：使用指标库中表相除计算
        分子：所选时间段内评价为满意+基本满意件次
        分母：所选时间段内评价为满意+基本满意+不满意件次
    例：
        xf_xfjg_cd_bmjb_qh_xfbm_xfxs_ypjjc
        xf_xfjg_cd_bmjb_qh_xfbm_xfxs_cqwpjjc
    """
    def __init__(self, apis_copy, apis, *args, **kwargs):
        # 执行父类方法，获得self.apis/self.apis_copy/self.value
        super(Cplv, self).__init__(apis_copy, apis, *args, **kwargs)

    def before_search(self):
        table = self.apis_copy.get("table", "")
        name = self.apis_copy.get("name", "")
        stack = self.apis_copy.get("stack", "")
        # value = self.apis_copy.get("value", "")

        # 处理目标字段
        target = table.split("_")[-1]
        base = "_".join(table.split("_")[:-1])
        self.value_yp = target.replace("cqwpjjc", "ypjjc")
        self.value_wp = target.replace("ypjjc", "cqwpjjc")

        # 处理 table
        table_yp = f"{base}_{self.value_yp}"
        table_wp = f"{base}_{self.value_wp}"

        # 处理 columns
        columns_yp = f"{name},{stack},{self.value_yp}"
        columns_wp = f"{name},{stack},{self.value_wp}"

        before_waiting_for_search = [
            {"table": table_yp, "columns": columns_yp, "conditions": [self.apis]},
            {"table": table_wp, "columns": columns_wp, "conditions": [self.apis]},
        ]

        self.code, self.msg, self.waiting_for_search = Extension.get_waiting_for_search(before_waiting_for_search)

    def after_search(self):
        """
        self.db_results: [[df_yp],[df_wp]]
        :return:
        """
        # 获取结果
        df_yp = Extension.groupby_and_sum(self.db_results[0][0], self.value_yp)
        df_wp = Extension.groupby_and_sum(self.db_results[1][0], self.value_wp)
        self.apis_copy["value"] = "cplv"
        if isinstance(df_yp, pd.DataFrame) and isinstance(df_wp, pd.DataFrame):
            # 融合
            df_yp[self.value_yp] = df_yp[self.value_yp].apply(lambda x: 0 if x is None else x)
            df_wp[self.value_wp] = df_wp[self.value_wp].apply(lambda x: 0 if x is None else x)

            columns = list(df_yp.columns)
            columns.remove(self.value_yp)
            if not columns:
                value = (df_yp[self.value_yp][0]) / (df_yp[self.value_yp][0] + df_wp[self.value_wp][0])
                # value = 0 if np.isnan(value) else value
                self.df = pd.DataFrame({"cplv": [value]})
            else:
                temp = pd.merge(df_yp, df_wp, on=columns, how="outer")
                temp = temp.fillna(0)
                # 计算
                df_yp["cplv"] = (temp[self.value_yp])/(temp[self.value_yp]+temp[self.value_wp])
                # 处理计算结果
                df_yp.drop(self.value_yp, axis=1, inplace=True)
                # df = df_yp.replace(np.nan, 0)
                # df = df.replace([np.inf, -np.inf], 0)
                self.df = df_yp
            # self.final_res = {"df": df, "apis_copy": self.apis_copy}
        else:
            df_yp = 0 if isinstance(df_yp, pd.DataFrame) else df_yp
            df_wp = 0 if isinstance(df_wp, pd.DataFrame) else df_wp
            value = df_yp / (df_yp + df_wp)
            self.df = pd.DataFrame({"cplv": [value]})
            # self.final_res = {"df": pd.DataFrame({"cplv": [value]}), "apis_copy": self.apis_copy}