import numpy as np
import pandas as pd
from sqlalchemy.orm import Session


class Extension:
    """
    transformer 下的 extension的基类
    1. 定义了除了 transformer其他条件过滤的方法（继承就会有）
    2. 定义了获取所有表的方法，默认就是当前表（table参数）
    before_search方法:
        返回 waiting_for_search = [{"table":"", "ex_table":"", "columns": [], "conditions": []}, {}]
    after_search方法:
        返回 res = [[data_list1, data_list2],[]]
    """
    from layers.get_dataframe.params_check.params_check_real_table import get_real_table
    from layers.get_dataframe.params_parse import get_conditions

    from utils.sys_extensions.groupby import groupby_and_sum
    from utils.sys_extensions.params_parse_tb_hb import params_parse_tb, params_parse_hb
    from utils.sys_extensions.calculate_tb_hb import calculate_tb_and_hb, calculate_tb_or_hb

    def __init__(self, apis_copy, apis, *args, **kwargs):  # apis_copy中可以拿到ex_table
        """实现除了transformer其他的条件解析"""
        self.code = 200
        self.msg = "success"
        self.apis_copy = apis_copy
        self.apis = apis
        self.value = apis_copy.get("value")
        self.before_waiting_for_search = None  # 调用_before_search后获得【可以继承后，在已有的内容上增加内容】
        self.waiting_for_search = None         # 调用before_search后获得【用于查库】
        self.db_results = None                 # 调用search后获得【查询结果，用于之后的合并】
        self.df = None                         # 调用after_search后获得【作为最终结果】

        self.args = args
        self.kwargs = kwargs

    def _before_search(self):
        self.code, self.msg, real_table = Extension.get_real_table(self.apis_copy)
        if self.code != 200:
            return
        table, ex_table = real_table["table"], real_table["ex_table"]
        tmp_search = self.apis_copy['tmp_search'].split(',')
        columns = f"{self.apis_copy.get('name','')},{self.apis_copy['stack']},{self.value},{','.join(tmp_search)}"
        conditions = [self.apis]
        before_waiting_for_search = [
            {"table": table, "ex_table": ex_table, "columns": columns, "conditions": conditions},
        ]
        self.before_waiting_for_search = before_waiting_for_search
        # self.code, self.msg, self.waiting_for_search = Extension.get_waiting_for_search(before_waiting_for_search)


    def before_search(self):
        self._before_search()
        if self.code != 200:
            return
        self.code, self.msg, self.waiting_for_search = Extension.get_waiting_for_search(self.before_waiting_for_search)


    @staticmethod
    def _get_none_df(apis_copy):
        columns = [apis_copy.get("name", ""), apis_copy.get("stack", ""), apis_copy.get("value", "")]
        from utils.get_unilist import get_unilist
        columns = get_unilist(columns)
        nonedf = [[pd.DataFrame([[None] * len(columns)], columns=columns)]]
        return nonedf

    def search(self):
        """
        waiting_for_search: [
            {"table": "", "ex_table": ex_table, "columns": ["year", "month", "xfjc"], "conditions": [ [ ],[ ] ]},
            {"table": "", "ex_table": ex_table, "columns": ["year", "month", "xfjc"], "conditions": [ [ ],[ ] ]}
        ]
        """
        # self.code, self.msg, self.waiting_for_search = Extension.get_waiting_for_search(self.before_waiting_for_search)

        if not self.waiting_for_search:
            nonedf = Extension._get_none_df(self.apis_copy)
            self.db_results = nonedf
            return
        # 获取order, limit
        order, limit = self.apis_copy["direct_order"], self.apis_copy["direct_limit"]
        # 获取数据库连接
        from utils.db_connection import zb_engine
        session = Session(zb_engine)
        searched = []

        # 开始查库
        for search_one_table in self.waiting_for_search:  # 第一张表
            columns = search_one_table["columns"]
            ex_table = search_one_table["ex_table"]
            # 查找表格中的字段
            search_table = []
            for col in columns:
                hascol = hasattr(ex_table.columns, col)
                if not hascol:
                    from app import app
                    NOCOLUMN_ERROR = app.config.get("NOCOLUMN_ERROR", True)
                    if NOCOLUMN_ERROR:
                        self.code, self.msg = 400, f"NoSuchColumnError: The table {search_one_table['table']} has no specific columns [{col}]"
                    else:
                        nonedf = Extension._get_none_df(self.apis_copy)
                        self.code, self.msg, self.db_results = 200, f"The table {search_one_table['table']} has no specific columns [{col}]", nonedf
                    session.close()
                    return

            tar_vs = [getattr(ex_table.columns, i) for i in columns]
            # 当前表中的多组条件
            for conditions in search_one_table["conditions"]:  # 第一组条件
                results = session.query(*tar_vs).filter(*conditions)  # results直接print是sql语句
                if order:
                    if "-" in order:  # sqlalchemy新版本中order_by 的用法需要用字段.desc()
                        results = results.order_by(getattr(ex_table.columns, order.replace("-", "")).desc())
                    else:
                        results = results.order_by(order)
                if limit:
                    results = results.limit(limit)
                from utils.results2df import results2df
                data = results2df(results, columns, self.apis_copy)
                search_table.append(data)
            searched.append(search_table)
        session.close()
        self.db_results = searched
        # return 200, "success", searched

    def after_search(self):
        df = self.db_results[0][0]
        df = Extension.groupby_and_sum(df, self.value)
        df = df.replace(np.nan, 0)
        df = df.replace([np.inf, -np.inf], 0)
        self.df = df
        # self.final_res = {"df": df, "apis_copy": self.apis_copy}

    def reuse_df(self):
        pass

    @classmethod
    def get_waiting_for_search(cls, before_waiting_for_search):
        """
        :param before_waiting_for_search:  [
            {"table": table_my, "columns": columns_my, "conditions": [apis_copy]},
            {"table": table_bmy, "columns": columns_bmy, "conditions": [apis_copy]},
            {"table": table_jbmy, "columns": columns_jbmy, "conditions": [apis_copy]}
        ]
        :return: code, msg, waiting_for_search: [{"table":"", "ex_table":"", "columns": [], "conditions": []}, {}]
        """
        for_search_done = []
        for waiting_for_search_each in before_waiting_for_search:
            for_search_each_done = {}
            # 处理 table
            table = waiting_for_search_each["table"]
            for_search_each_done["table"] = table

            # 处理 ex_table
            ex_table = waiting_for_search_each.get("ex_table")
            if ex_table is None:
                db_engine = waiting_for_search_each.get("db_engine", "zb_db")
                code, msg, real_table = cls.get_real_table({"table": table, "db_engine": db_engine})
                if code != 200:
                    return code, msg, {}
                ex_table = real_table["ex_table"]
            for_search_each_done["ex_table"] = ex_table

            # 处理 columns
            columns = waiting_for_search_each["columns"]
            columns = [i for i in columns.split(",") if i]
            from utils.get_unilist import get_unilist
            for_search_each_done["columns"] = get_unilist(columns)

            # 处理conditions
            conditions_done = []
            conditions = waiting_for_search_each["conditions"]
            for condition in conditions:
                if not isinstance(condition, dict):  # 说明有多组condition
                    return 400, "ExtensionError: The condition must be list with some dicts", {}
                if isinstance(ex_table, str):
                    return 200, "ExtensionError: NoSuchTable", {}
                code, msg, parsed_condition = cls.get_conditions(ex_table, condition)
                if code != 200:
                    return code, msg, {}
                conditions_done.append(parsed_condition)

            for_search_each_done["conditions"] = conditions_done
            for_search_done.append(for_search_each_done)

        return 200, "success", for_search_done
