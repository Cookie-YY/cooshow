import os

from flask import g  # 用于存放变化后的init_dicts
from libs.param_trans import ParamTrans
import pandas as pd


class PT(ParamTrans):
    # 获得 qh2sheshixj/qh_include_sub/qh_godown
    def __init__(self, apis_copy):
        super(PT, self).__init__(apis_copy)   # 得到self.apis_copy

    def wx_map(self, *args, **kwargs):
        xfxs = self.apis_copy.get("xfxs", "")
        if xfxs == "网信":
            update_dict = {"OR-xfxs": "!来信,!来访"}
            self.apis_copy.update(update_dict)
        return self

    @staticmethod
    def _init_file_reader(file):
        from app import app
        # file = "shejxfbm+shijxfbm+xjxfbm" if flag == "xfbm" else "qh+zrdw"
        path = app.config.get("INITIALIZATION_FILE_PATH")
        sep = app.config.get("INITIALIZATION_FILE_SEP", "\t")
        return pd.read_csv(os.path.join(path, file), sep=sep)

    def xfbm_godown(self, *args, **kwargs):
        xfbm = PT._init_file_reader("shejxfbm+shijxfbm+xjxfbm")
        target = self.apis_copy.get("xfbm")
        if target:
            childxfbm = []
            if target in xfbm["shejxfbm"].tolist():
                childxfbm = xfbm["shijxfbm"].tolist()
            elif target in xfbm["shijxfbm"].tolist():
                childxfbm = xfbm["xjxfbm"][xfbm["shijxfbm"] == target].tolist()
            elif target in xfbm["xjxfbm"].tolist():
                childxfbm = [target]
            from utils.get_unilist import get_unilist
            childxfbm = get_unilist(childxfbm)
            g.modified_initialization.update({"xfbm": childxfbm})
            self.apis_copy.update({"name": "xfbm", "IN-xfbm": ",".join(childxfbm)})
        return self

    def zrdw_godown(self, *args, **kwargs):
        # 责任单位go_down没有g.modified_initialization.update({"zrdw": childzrdw})
        if self.apis_copy.get("Cqh"):
            zrdw_list = ['广东省住房和城乡建设厅', '广东省交通运输厅', '广东省水利厅', '广东省农业农村厅', '广东省卫生健康委员会',
                         '广东省国资委', '广东省市场监督管理局', '广东省应急管理厅', '广东省地方金融监督管理局', '广东省公安厅',
                         '广东省民政厅', '广东省司法厅', '广东省人力资源和社会保障厅', '广东省生态环境厅', '广东省教育厅',
                         '广东省自然资源厅', '广东省科技厅', '广东省商务厅', '广东省退役军人事务厅']
            if self.apis_copy.get("Cqh") != "广东省":
                zrdw = PT._init_file_reader("qh+zrdw")
                qh = self.apis_copy.get("Cqh")
                zrdw_list = zrdw["zrdw"][zrdw["qh"] == qh].tolist()
            g.modified_initialization.update({"zrdw": zrdw_list})
            self.apis_copy.pop("zrdw", "")
            self.apis_copy["name"] = "zrdw"
            self.apis_copy.update({"name": "zrdw", "IN-zrdw": ",".join(zrdw_list)})
        return self

    def djjg_qhauth(self, *args, **kwargs):
        """
        登记机构的饼图的权限控制:
            国家: 只有省级的能看
            省级：只有省级的能看
            市级：省级/市级的能看      省级看所有的市  市级看自己的
            县级：省级/市级/县级能看    省级看所有县   市级看自己的县   县级看自己
        """
        from utils.qh_processor import get_qh_include_sub
        from utils.get_unilist import get_unilist
        if g.get("level_auth_name"):
            qh_list = get_unilist(get_qh_include_sub(g.get("level_auth_name")))
            qh_list = [f"'{i}'" for i in qh_list]
            self.apis_copy["sql_qhauth_other"] = {"djjg_qh": f"qh in ({','.join(qh_list)})"}
        table = self.apis_copy.get("table", "")
        qh = self.apis_copy.get("Cqh", "")
        if "djjg" in table and "qh" in table:
            self.apis_copy["djjg"] = args[0]

            self.apis_copy["IN-Cqh"] = ",".join(get_unilist(get_qh_include_sub(qh)))
        return self

    def xfbm_qhauth(self, *args, **kwargs):
        """
        额外修改 部门级别时  需要让extension过程从apis_copy中拿bmjb
        只会传递xfbm, 需要根据g变量的权限去看xfbm是否超限[g.level_auth可以拿到qh名称]
            如果超限返回设定好的信访部门[表里面唯一]
        使用时在xfbm_godown的前面
        """
        qh_ceiling = g.get("level_auth_name")
        if qh_ceiling:
            xfbm = PT._init_file_reader("shejxfbm+shijxfbm+xjxfbm")
            target = self.apis_copy.get("xfbm")
            from utils.qh_processor import get_qh_levelindex
            qh_ceiling_index = get_qh_levelindex(qh_ceiling)
            if target in xfbm["shejxfbm"].tolist():
                xfbm_qh_index = 0
            elif target in xfbm["shijxfbm"].tolist():
                xfbm_qh_index = 1
            else:
                xfbm_qh_index = 2
            if xfbm_qh_index < qh_ceiling_index:
                xfbm_list = xfbm.iloc[:,qh_ceiling_index][xfbm.iloc[:,qh_ceiling_index].str.contains(qh_ceiling)].tolist()
                if len(set(xfbm_list)) == 1:
                    self.apis_copy["xfbm"] = xfbm_list[0]
                # self.apis_copy["xfbm"] = qh_ceiling+"信访局"
                if args:
                    if args[0] == "信访部门":
                        bmjb = ["省级", "市级", "县级"][qh_ceiling_index]
                        g.reqdicts_before_pt.update({"bmjb": bmjb})
                        self.apis_copy["bmjb"] = bmjb

        return self

    def zrdw_qhauth(self, *args, **kwargs):
        """
        传递zrdw和Cqh，可以根据Cqh判断zrdw是否超限，如果超限返回设定好的责任单位
        使用时在zrdw_godown的前面
        """
        qh_ceiling = self.apis_copy.get("Cqh")
        if qh_ceiling:
            zrdw = PT._init_file_reader("qh+zrdw")
            target = self.apis_copy.get("zrdw")
            qh = zrdw["qh"][zrdw["zrdw"] == target].tolist()
            if len(set(qh)) == 1:
                from utils.qh_processor import get_qh_with_auth
                qh_with_auth = get_qh_with_auth(qh[0], qh_ceiling)
                res = zrdw["zrdw"][zrdw["qh"] == qh_with_auth].reset_index(drop=True)
                res_bool = res.str.contains("住房和城乡建设").reset_index(drop=True)
                res = res[res_bool].tolist()
                if res:
                    self.apis_copy["zrdw"] = res[0]
        return self

    def xfbmsearch_qhauth(self, *args, **kwargs):
        """
        信访部门搜索弹窗的权限: 只能显示同一级别的这个局和下属的局
        根据 g.get("level_auth_name") 获取名字    配合jb参数完成过滤
        """
        qh_ceiling = g.get("level_auth_name")
        if qh_ceiling:
            from utils.qh_processor import get_qh_include_sub
            from libs.devdebug import DevDubug
            code, msg, xfbm_search = DevDubug.get_specific_table(table="search_xfbm_jb")
            qh_list = get_qh_include_sub(qh_ceiling)
            qh_re_list = [f".*{i}.*" for i in qh_list]
            xfbm_list = xfbm_search["xfbm"][xfbm_search["xfbm"].str.match("|".join(qh_re_list))].tolist()
            self.apis_copy["IN-xfbm"] = ",".join(list(set(xfbm_list)))
        return self

    def zrdwsearch_qhauth(self, *args, **kwargs):
        """
        责任单位搜索弹窗的权限: 只能显示同一级别的和下属的责任单位
        直接从Cqh需要在 qh_ceiling和其下属里面   配合jb完成筛选
        """
        qh_ceiling = g.get("level_auth_name")
        if qh_ceiling:
            from utils.qh_processor import get_qh_include_sub
            qh_list = get_qh_include_sub(qh_ceiling)
            self.apis_copy["IN-Cqh"] = ",".join(list(set(qh_list)))
        return self

    def find_qh_from_xfbm(self, *args, **kwargs):
        keyword_map = {'shej': '省', 'shij': '市', 'xj': ['县', '区', '镇']}
        xfbm = self.apis_copy.get("xfbm")
        if not xfbm:
            Cqh = g.get("level_auth_name")
        else:
            shej_index = xfbm.find('省')
            shij_index = xfbm.find('市')
            xj_index = [xfbm.find(k) for k in keyword_map['xj'] if k in xfbm] + [-1]
            xj_index = xj_index[0]

            shej_str = xfbm[:shej_index + 1]
            shij_str = xfbm[shej_index + 1: shij_index + 1]
            xj_str = xfbm[shej_index + 1:xj_index + 1] if shij_index < 0 else xfbm[shij_index + 1:xj_index + 1]

            Cqh = xj_str or shij_str or shej_str

        self.apis_copy["Cqh"] = Cqh
        return self

    def is_ga(self, *args, **kwargs):
        if "hy" in self.apis_copy.get("table", ""):
            if self.apis_copy.pop("is_ga", "") == "false":
                self.apis_copy["hy"] = "!公安"
        return self

