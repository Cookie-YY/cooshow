from libs.extensions import Extension
import pandas as pd
import numpy as np


class Hb(Extension):
    """环比"""

    def __init__(self, apis_copy, apis, *args, **kwargs):
        # 执行父类方法，获得self.apis/self.apis_copy/self.value
        super(Hb, self).__init__(apis_copy, apis, *args, **kwargs)

    def before_search(self):
        self._before_search()  # 此时self.before_waiting_for_search中就有了最基本的内容
        condition_hb = Hb.params_parse_hb(self.apis.copy())

        condition_hb_container = self.before_waiting_for_search[0]["conditions"].copy()
        condition_hb_container.append(condition_hb)

        self.before_waiting_for_search[0]["conditions"] = condition_hb_container

        self.code, self.msg, self.waiting_for_search = Hb.get_waiting_for_search(self.before_waiting_for_search)

    def after_search(self):
        """
        self.db_results: [db_results[0][0]]
        :return:
        """
        # 获取结果
        self.db_results[0][0] = Extension.groupby_and_sum(self.db_results[0][0], self.value)
        self.db_results[0][1] = Extension.groupby_and_sum(self.db_results[0][1], self.value)

        if isinstance(self.db_results[0][0], pd.DataFrame) and self.db_results[0][0].shape[1] == 1 and self.db_results[0][0][self.value][0] is None:
            self.db_results[0][0] = np.int32(0)
        if isinstance(self.db_results[0][1], pd.DataFrame) and self.db_results[0][1].shape[1] == 1 and self.db_results[0][1][self.value][0] is None:
            self.db_results[0][1] = np.int32(0)

        df_hb = Hb.calculate_tb_or_hb(self.db_results, self.apis_copy)

        self.apis_copy["value"] = "hb"
        df_hb = df_hb.rename(columns={self.value: "hb"}) if isinstance(df_hb, pd.DataFrame) else pd.DataFrame({"hb": [df_hb]})

        self.df = df_hb