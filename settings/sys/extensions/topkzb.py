from libs.extension import Extension
import pandas as pd

class Topkzb(Extension):
    """前k个占比"""
    """
    返回前k个的占比: 只有一个数字  value改成zb
    """
    def __init__(self, apis_copy, apis, *args, **kwargs):
        # 执行父类方法，获得self.apis/self.apis_copy/self.value
        super(Topkzb, self).__init__(apis_copy, apis, *args, **kwargs)

    def after_search(self):
        """
        self.db_results: [db_results[0][0]]
        :return:
        """
        # 获取结果
        df_zb = Extension.groupby_and_sum(self.db_results[0][0], self.value)

        if len(self.args) == 1:
            if self.args[0] == "":
                return {}
                # df_zb[self.value] = df_zb[self.value].apply(lambda x: x or 0) / (df_zb[self.value].sum())
            else:
                # 这里可以不止支持返回一个数字的格式
                # 可以是name/stack 的格式  按照name分组，每组的前10个stack
                total = df_zb[self.value].sum()
                topK = int(self.args[0])
                df_zb = df_zb.sort_values([self.value], ascending=False).head(topK)
                try:
                    topKratio = df_zb[self.value].sum() / total
                except:
                    topKratio = 0
                df_zb = pd.DataFrame({"zb": [topKratio]})
            # df_zb = df_zb.rename(columns={self.value: "zb"})
            self.apis_copy["value"] = "zb"
            self.apis_copy.pop("name", "")
        else:
            return {}

        self.df = df_zb
