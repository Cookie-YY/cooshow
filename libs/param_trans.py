from flask import g
import pandas as pd
import os


class ParamTrans:
    def __init__(self, apis_copy):
        self.apis_copy = apis_copy

    @staticmethod
    def _init_file_reader(file):
        from app import app
        # file = "shejxfbm+shijxfbm+xjxfbm" if flag == "xfbm" else "qh+zrdw"
        path = app.config.get("INITIALIZATION_FILE_PATH")
        sep = app.config.get("INITIALIZATION_FILE_SEP", "\t")
        return pd.read_csv(os.path.join(path, file), sep=sep)

    def qh2sheshixj(self, *args, **kwargs):
        table = self.apis_copy.get("table", "")
        qh = self.apis_copy.get("Cqh", "")     # 此时的qh已经是经过权限过滤的了
        qh_ceiling = g.get("level_auth_name")
        # 如果有权限控制直接把sql_qh_auth写成ceiling【防止那种接口不传Cqh的可能(在sql_qhauth中可以拿到ceiling的权限)】
        if qh_ceiling:
            sql_sqlauth_qh = f"qh = '{qh_ceiling}'"
            from utils.qh_processor import get_qh_level
            qh_level = get_qh_level(qh_ceiling)  # xj_02时 只有xj_02=xx县 没有shij_02
            sql_sqlauth_sheshixj = f"{qh_level} = '{qh_ceiling}'"

            if "qh" in table:
                update_dict = {"sql_qhauth_auto": sql_sqlauth_qh, "sql_qhauth_qh": sql_sqlauth_qh}
            elif "shej" in table or "shij" in table or "xj" in table:
                update_dict = {"sql_qhauth_auto": sql_sqlauth_sheshixj, "sql_qhauth_sheshixj": sql_sqlauth_sheshixj}
            else:
                update_dict = {"sql_qhauth_qh": sql_sqlauth_qh, "sql_qhauth_sheshixj": sql_sqlauth_sheshixj}
            self.apis_copy.update(update_dict)

        # 正常的转换操作，通过转换得到的qh也会再次作用在sql_qhauth上
        if qh:
            if "qh" in table:
                sql_sqlauth_qh = f"qh = '{qh}'"
                update_dict = {"sql_qhauth_auto": sql_sqlauth_qh, "sql_qhauth_qh": sql_sqlauth_qh}
            elif "shej" in table or "shij" in table or "xj" in table:  # 这里不能删除Cqh，其他的pt还要用，最后统一删除
                from utils.qh_processor import get_qh_level
                qh_level = get_qh_level(qh)  # xj_02时 只有xj_02=xx县 没有shij_02
                sql_sqlauth_sheshixj = f"{qh_level} = '{qh}'"
                update_dict = {qh_level: qh, "sql_qhauth_auto": sql_sqlauth_sheshixj, "sql_qhauth_sheshixj": sql_sqlauth_sheshixj}
            else:
                return self
            self.apis_copy.update(update_dict)
        return self

    def qh_include_sub(self, *args, **kwargs):
        # full的问题
        qh = self.apis_copy.get("Cqh", "")
        table = self.apis_copy.get("table", "")
        if qh and "qh" in table:
            from utils.qh_processor import get_qh_include_sub
            from utils.get_unilist import get_unilist
            qh_include_sub = get_unilist(get_qh_include_sub(qh))
            update_dict = {"IN-Cqh": ",".join(qh_include_sub)}
            self.apis_copy.update(update_dict)
        return self

    def qh_godown(self, *args, **kwargs):
        # full的问题
        table = self.apis_copy.get("table", "")
        qh = self.apis_copy.get("Cqh", "")
        from utils.qh_processor import get_qh_sub
        from utils.get_unilist import get_unilist
        child_qh = get_qh_sub(qh, "next")
        child_qh = get_unilist(child_qh)
        if "shej" in table or "shij" in table or "xj" in table:
            qh = self.apis_copy.get("Cqh", "")
            from utils.qh_processor import get_qh_godown
            qh_child_level = get_qh_godown(qh)
            update_dict = {"name": qh_child_level}
            g.modified_initialization.update({qh_child_level: child_qh})
        elif "qh" in table:
            update_dict = {"name": "qh", "IN-Cqh": ",".join(child_qh)}
            g.modified_initialization.update({"qh": child_qh})
            # waittodo: full的事
        elif table == "":  #  没有写table，走transformer，按照qh in table处理
            qh = self.apis_copy.get("Cqh", "")
            from utils.qh_processor import get_qh_sub
            from utils.get_unilist import get_unilist
            child_qh = get_qh_sub(qh, "next")
            child_qh = get_unilist(child_qh)
            update_dict = {"name": "qh", "IN-Cqh": ",".join(child_qh)}
            g.modified_initialization.update({"qh": child_qh})
        else:
            return self
        self.apis_copy.update(update_dict)
        return self

    def year_range(self, *args, **kwargs):
        # param_trans在parse_now之后
        # param_trans在g.reqdicts_before_pt之前（g.reqdicts_before_pt有start和end）
        # self.apis_copy需要有[2018,2020]  // 搜索/排序补零
        year = self.apis_copy.get("year")
        if year.isdigit() and len(args) == 1:
            start = int(year) - int(args[0])
            condition = f"{start},{year}"
            self.apis_copy["year"] = condition
            g.reqdicts_before_pt.update({"start": str(start), "end": str(year)})
        return self

    def year2day(self, *args, **kwargs):
        year = self.apis_copy.get("year")
        if year:
            self.apis_copy["day"] = f"[{year}-01-01,{year}-12-31]"
            self.apis_copy.pop("year", "")
        return self

    def xj2shij(self, *args, **kwargs):
        if not self.apis_copy.get("xj_02", "") and self.apis_copy.get("table", ""):
            tbl = self.apis_copy.get("table", "")
            tbl = tbl.replace("xj", "shij")
            self.apis_copy["table"] = tbl
        return self

    def before_finish(self, *args, **kwargs):
        # 1. 存在qh 但 区划体系是  shej/shij/xj时，删除qh
        qh = self.apis_copy.get("Cqh", "")
        table = self.apis_copy.get("table", "") or self.apis_copy.get("qh", "")  # 可能不是用table的方式 使用拼接方式写的数据表
        if qh and ("shej" in table or "shij" in table or "xj" in table):
            self.apis_copy.pop("Cqh", "")

        # 存在带有IN-条件或者OR-条件时，删除  剩下的内容  如  存在IN-Cqh时 删除Cqh
        wait_for_del = [i for i in self.apis_copy if i.startswith("IN-") or i.startswith("OR-")]
        wait_for_del = [i.split("-")[1] for i in wait_for_del]
        for i in wait_for_del:
            self.apis_copy.pop(i, "")


        # # 2. 存在qh_godown 并且 table中含有qh时，删除Cqh
        # param_trans = self.apis_copy.get("param_trans", "")
        # table = self.apis_copy.get("table", "")
        # if "qh_godown" in param_trans and "qh" in table:
        #     self.apis_copy.pop("Cqh", "")
        #
        # # 3. 存在qh_include_sub 并且 table中含有qh时，删除Cqh
        # param_trans = self.apis_copy.get("param_trans", "")
        # table = self.apis_copy.get("table", "")
        # if "qh_include_sub" in param_trans and "qh" in table:
        #     self.apis_copy.pop("Cqh", "")
        #
        # # waittodo: 存在IN-Cqh  时  删除Cqh

