from libs.extension import Extension


class Zb(Extension):
    """占比"""
    """
    目前仅支持分组求和
    """
    def __init__(self, apis_copy, apis, *args, **kwargs):
        # 执行父类方法，获得self.apis/self.apis_copy/self.value
        super(Zb, self).__init__(apis_copy, apis, *args, **kwargs)

    def after_search(self):
        """
        self.db_results: [db_results[0][0]]
        :return:
        """
        # 获取结果
        df_zb = Extension.groupby_and_sum(self.db_results[0][0], self.value)

        if len(self.args) == 1:
            if self.args[0] == "":
                df_zb[self.value] = df_zb[self.value].apply(lambda x: x or 0) / (df_zb[self.value].sum())
            else:
                former, later = self.args[0].split("/")
                tmp = df_zb[later].map(
                    lambda x: df_zb.loc[df_zb[later] == x, [self.value]].sum().squeeze())  # 按later类型计算value列的和，squeeze()取标量
                df_zb[self.value] = df_zb[self.value] / tmp
            df_zb = df_zb.rename(columns={self.value: "zb"})
            self.apis_copy["value"] = "zb"
        else:
            return {}

        self.df = df_zb









def parse_zb(df_list, apis_copy):
    """
    @zb的情况
    1. @zb:ejnr/yjnr
    2. @zb:yjnr/yjnr     # 相当于分子是 xfjc  分母是所有的 xfjc 求和
    # 3. @zb:yjnr        # 相当于 yjnr/yjnr   这里必须保证是 name
    4. @zb               # 相当于 $name / $name

    最后返回一个df
    """
    transformer = apis_copy.get("transformer")
    name = apis_copy.get("name")
    value = apis_copy.get("value")
    zb = transformer.get("@zb")
    if zb == "":      # 各个 name 在总数中的占比
        former, later = name, name
    elif "/" in zb:   # name 列 在 later中的占比
        former, later = zb.split("/")
    else:             # 只有一个值，name 列 对应的占比
        former, later = zb, zb

    # 计算
    df = df_list[0][0]
    if former == later:  #
        # 说明只有两列（一列是需要 groupby 的列: former 列，第二列是需要求和的列: value 列）
        df[value] = df[value]/(df[value].sum())
    else:
        t = df[later].map(lambda x: df.loc[df[later] == x, [value]].sum().squeeze())  # 按later类型计算value列的和，squeeze()取标量
        df[value] = df[value] / t

    return df
