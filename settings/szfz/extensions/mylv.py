from libs.extensions import Extension
import pandas as pd
import numpy as np


class Mylv(Extension):
    """满意率"""
    """
    计算公式：使用指标库中表相除计算
        分子：所选时间段内评价为满意+基本满意件次
        分母：所选时间段内评价为满意+基本满意+不满意件次
    例：
        xf_xfjg_cd_bmjb_qh_xfbm_xfxs_myjc
        xf_xfjg_cd_bmjb_qh_xfbm_xfxs_bmyjc
        xf_xfjg_cd_bmjb_qh_xfbm_xfxs_jbmyjc

    """
    def __init__(self, apis_copy, apis, *args, **kwargs):
        # 执行父类方法，获得self.apis/self.apis_copy/self.value
        super(Mylv, self).__init__(apis_copy, apis, *args, **kwargs)

    def before_search(self):
        table = self.apis_copy.get("table", "")
        name = self.apis_copy.get("name", "")
        stack = self.apis_copy.get("stack", "")
        # value = self.apis_copy.get("value", "")

        # 处理目标字段
        target = table.split("_")[-1]
        base = "_".join(table.split("_")[:-1])
        self.value_my = target
        self.value_bmy = target.replace("myjc", "bmyjc")
        self.value_jbmy = target.replace("myjc", "jbmyjc")

        # 处理 table
        table_my = f"{base}_{self.value_my}"
        table_bmy = f"{base}_{self.value_bmy}"
        table_jbmy = f"{base}_{self.value_jbmy}"

        # 处理 columns
        columns_my = f"{name},{stack},{self.value_my}"
        columns_bmy = f"{name},{stack},{self.value_bmy}"
        columns_jbmy = f"{name},{stack},{self.value_jbmy}"

        #
        before_waiting_for_search = [
            {"table": table_my, "columns": columns_my, "conditions": [self.apis]},
            {"table": table_bmy, "columns": columns_bmy, "conditions": [self.apis]},
            {"table": table_jbmy, "columns": columns_jbmy, "conditions": [self.apis]}
        ]

        self.code, self.msg, self.waiting_for_search = Extension.get_waiting_for_search(before_waiting_for_search)

    def after_search(self):
        """
        self.db_results: [[df_my],[df_bmy],[df_jbmy]]
        :return:
        """
        # 获取结果
        df_my = Extension.groupby_and_sum(self.db_results[0][0], self.value_my)
        df_bmy = Extension.groupby_and_sum(self.db_results[1][0], self.value_bmy)
        df_jbmy = Extension.groupby_and_sum(self.db_results[2][0], self.value_jbmy)
        self.apis_copy["value"] = "mylv"
        if isinstance(df_my, pd.DataFrame) and isinstance(df_bmy, pd.DataFrame) and isinstance(df_jbmy, pd.DataFrame):
            # 融合
            df_my[self.value_my] = df_my[self.value_my].apply(lambda x: 0 if x is None else x)
            df_bmy[self.value_bmy] = df_bmy[self.value_bmy].apply(lambda x: 0 if x is None else x)
            df_jbmy[self.value_jbmy] = df_jbmy[self.value_jbmy].apply(lambda x: 0 if x is None else x)

            columns = list(df_my.columns)
            columns.remove(self.value_my)
            if not columns:
                value = (df_my[self.value_my][0] + df_jbmy[self.value_jbmy][0]) / (df_my[self.value_my][0] + df_jbmy[self.value_jbmy][0]+df_bmy[self.value_bmy][0])
                # value = 0 if np.isnan(value) else value
                self.df = pd.DataFrame({"mylv": [value]})
            else:
                temp = pd.merge(pd.merge(df_my, df_bmy, on=columns, how="outer"), df_jbmy, on=columns, how="outer")
                # 计算
                temp = temp.fillna(0)
                df_my["mylv"] = (temp[self.value_my]+temp[self.value_jbmy])/(temp[self.value_my]+temp[self.value_jbmy]+temp[self.value_bmy])

                # 处理计算结果
                df_my.drop(self.value_my, axis=1, inplace=True)
                # df = df_my.replace(np.nan, 0)
                # df = df.replace([np.inf, -np.inf], 0)
                self.df = df_my
        else:
            df_my = 0 if isinstance(df_my, pd.DataFrame) else df_my
            df_bmy = 0 if isinstance(df_bmy, pd.DataFrame) else df_bmy
            df_jbmy = 0 if isinstance(df_jbmy, pd.DataFrame) else df_jbmy

            value = (df_my+df_jbmy) / (df_my+df_jbmy+df_bmy)
            self.df = pd.DataFrame({"mylv": [value]})
            # self.final_res = {"df": pd.DataFrame({"mylv": [value]}), "apis_copy": self.apis_copy}
