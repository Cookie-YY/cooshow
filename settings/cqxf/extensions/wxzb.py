from libs.extensions import Extension
import pandas as pd
import numpy as np


class Wxzb(Extension):
    """网信占比"""
    """
    计算公式：xfxs为网信的和其他数据的比较
    """
    def __init__(self, apis_copy, apis, *args, **kwargs):
        # 执行父类方法，获得self.apis/self.apis_copy/self.value
        super(Wxzb, self).__init__(apis_copy, apis, *args, **kwargs)
        self.apis_copy["tmp_search"] = "xfxs"  # search时增加一列

    def after_search(self):
        """
        self.db_results: [db_results[0][0]]
        :return:
        """
        # 获取结果
        self.apis_copy["value"] = "wxzb"
        df_wxzb = Extension.groupby_and_sum(self.db_results[0][0], self.value)

        groupby = f"{self.apis_copy['name']},{self.apis_copy['stack']}"
        from utils.get_unilist import get_unilist
        groupby = get_unilist(groupby.split(","))
        if groupby:
            df_wxzb[self.value] = (df_wxzb[self.value] / df_wxzb.groupby(groupby)[self.value].transform('sum'))
            df_wxzb = df_wxzb.loc[df_wxzb["xfxs"] == "网信", :]
            df_wxzb[self.value].astype(float)
            df_wxzb = df_wxzb.rename(columns={self.value: "wxzb"})
            df_wxzb = df_wxzb.drop(["xfxs"], axis=1)

            self.df = df_wxzb
        else:
            self.df = df_wxzb[self.value][df_wxzb["xfxs"] == "网信"] / df_wxzb[self.value].sum()
            self.df = pd.DataFrame({"wxzb": self.df})


