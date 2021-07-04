from libs.extensions import Extension


class Groupby(Extension):
    """分组(求和)"""
    """
    目前仅支持分组求和
    """
    def __init__(self, apis_copy, apis, *args, **kwargs):
        # 执行父类方法，获得self.apis/self.apis_copy/self.value
        super(Groupby, self).__init__(apis_copy, apis, *args, **kwargs)

    def after_search(self):
        """
        self.db_results: [db_results[0][0]]
        :return:
        """
        # 获取结果
        if len(self.args) == 1:
            if self.args[0] == "sum" or self.args[0] == "":
                df_groupby = Extension.groupby_and_sum(self.db_results[0][0], self.value)
            else:
                return {}
        else:
            return {}

        self.df = df_groupby