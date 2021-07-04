from flask import g

from libs.extensions import Extension
import pandas as pd

from settings.gdxf.extensions.wxzb.base_sql_map import get_base_sql_map
from utils.qh_processor import get_qh_level

DEBUG = False


def get_sql_map(flag):
    if flag:
        base_sql_map = {
            "1-1-全": "1_1",
        }
    else:
        base_sql_map = get_base_sql_map()
    sql_map = {
        # 区划分布 --> 全部 --> 总体 【一个数】 省级 需求和
        "wxzb_qh_all_xfbm_shej": (
            f"select sum(a.wxsl)/sum(a.zs) as wxzb from {base_sql_map['1-1-全']} as a",
            ["wxzb"]),
        # 区划分布 --> 全部 --> 总体 【一个数】 市级
        "wxzb_qh_all_xfbm_shij": (
            f"select a.wxsl/a.zs as wxzb from {base_sql_map['1-1-全']} as a where a.region_name='{{Cqh}}'",
            ["wxzb"]),
        # 区划分布 --> 全部 --> 总体 【一个数】 县级
        "wxzb_qh_all_xfbm_xj": (
            f"select a.wxsl/a.zs as wxzb from {base_sql_map['1-2-全']} as a where a.region_name='{{Cqh}}'",
            ["wxzb"]),

        # 区划分布 --> 全部 --> 地图 省级
        "wxzb_qh_allshej": (
            f"select a.region_name as qh,a.wxsl/a.zs as wxzb from {base_sql_map['1-1-全']} as a",
            ["qh", "wxzb"]),
        # 区划分布 --> 全部 --> 地图 市级
        "wxzb_qh_allshij": (
            f"select a.region_name as qh,a.wxsl/a.zs as wxzb from {base_sql_map['1-2-全']} as a",
            ["qh", "wxzb"]),

        # 信访部门 -->全部 --> 网信占比 【一个数】 用上面的
        # "wxzb_xfbm_all": (
        #     f"select a.wxsl/a.zs as wxzb from {base_sql_map['1-1-全']} as a where a.region_name='{{Cqh}}'",
        #     ["wxzb"]),

        # 信访部门 -->全部 --> 饼图 省级
        "wxzb_xfbm_shejnums": (
            f"SELECT case a.wxsl when a.wxsl then '网信' end as wxqk,sum(a.wxsl) as 'xfjc' FROM {base_sql_map['1-1-全']} as a UNION SELECT case a.wxsl when a.wxsl then '其他' end as wxqk ,(sum(a.zs) - sum(a.wxsl)) as 'xfjc'  FROM {base_sql_map['1-1-全']} as a",
            ["wxqk", "xfjc"]),
        # 信访部门 -->全部 --> 饼图 市级
        "wxzb_xfbm_shijnums": (
            f"SELECT case a.wxsl when a.wxsl then '网信' end as wxqk,a.wxsl as 'xfjc' FROM {base_sql_map['1-1-全']} as a WHERE a.region_name='{{Cqh}}' UNION SELECT case a.wxsl when a.wxsl then '其他' end as wxqk ,(a.zs - a.wxsl) as 'xfjc'  FROM {base_sql_map['1-1-全']} as a WHERE a.region_name='{{Cqh}}'",
            ["wxqk", "xfjc"]),
        # 信访部门 -->全部 --> 饼图 县级 待完成
        "wxzb_xfbm_xjnums": (
            f"SELECT case a.wxsl when a.wxsl then '网信' end as wxqk,a.wxsl as 'xfjc' FROM {base_sql_map['1-2-全']} as a WHERE a.region_name='{{Cqh}}' UNION SELECT case a.wxsl when a.wxsl then '其他' end as wxqk ,(a.zs - a.wxsl) as 'xfjc'  FROM {base_sql_map['1-2-全']} as a WHERE a.region_name='{{Cqh}}'",
            ["wxqk", "xfjc"]),

    }
    return sql_map


class Wxzb(Extension):
    """网信占比"""
    """
    计算公式：使用已提供的SQL语句进行计算
    """

    def __init__(self, apis_copy, apis, *args, **kwargs):
        self.sql, self.columns = None, None
        super(Wxzb, self).__init__(apis_copy, apis)  # 执行父类方法，获得self.apis/self.apis_copy

    def before_search(self):
        self.df = pd.DataFrame([None], columns=["wxzb"])
        sql_list = self.apis_copy['ext'].split('/')
        Cqh_sql_map = {'shej_02': {'xfxs': None, 'all': None}, 'shij_02': {'xfxs': None, 'all': None},
                       'xj_02': {'xfxs': None, 'all': None}, 'all': {'xfxs': None, 'all': None}}
        for item in sql_list:
            if 'xfxs' in item:
                if 'shej' in item:
                    Cqh_sql_map['shej_02']['xfxs'] = item
                    Cqh_sql_map['all']['xfxs'] = item if not Cqh_sql_map['all']['xfxs'] else Cqh_sql_map['all']['xfxs']
                elif 'shij' in item:
                    Cqh_sql_map['shij_02']['xfxs'] = item
                    Cqh_sql_map['all']['xfxs'] = item if not Cqh_sql_map['all']['xfxs'] else Cqh_sql_map['all']['xfxs']
                elif 'xj' in item:
                    Cqh_sql_map['xj_02']['xfxs'] = item
                    Cqh_sql_map['all']['xfxs'] = item if not Cqh_sql_map['all']['xfxs'] else Cqh_sql_map['all']['xfxs']
                else:
                    Cqh_sql_map['all']['xfxs'] = item
            else:
                if 'shej' in item:
                    Cqh_sql_map['shej_02']['all'] = item
                    Cqh_sql_map['all']['all'] = item if not Cqh_sql_map['all']['all'] else Cqh_sql_map['all']['all']
                elif 'shij' in item:
                    Cqh_sql_map['shij_02']['all'] = item
                    Cqh_sql_map['all']['all'] = item if not Cqh_sql_map['all']['all'] else Cqh_sql_map['all']['all']
                elif 'xj' in item:
                    Cqh_sql_map['xj_02']['all'] = item
                    Cqh_sql_map['all']['all'] = item if not Cqh_sql_map['all']['all'] else Cqh_sql_map['all']['all']
                else:
                    Cqh_sql_map['all']['all'] = item

        xfxs = g.get('reqdicts_before_pt').get('xfxs')

        if g.get('reqdicts_before_pt').get('bmjb', "") == '省级':
            bmjb = 'shej_02'
        elif g.get('reqdicts_before_pt').get('bmjb', "") == '市级':
            bmjb = 'shij_02'
        elif g.get('reqdicts_before_pt').get('bmjb', "") == '县级':
            bmjb = 'xj_02'
        else:
            bmjb = None

        if bmjb:
            if xfxs:
                sql_item = Cqh_sql_map[bmjb]['xfxs'] if Cqh_sql_map[bmjb]['xfxs'] else Cqh_sql_map['all']['xfxs']
            else:
                sql_item = Cqh_sql_map[bmjb]['all'] if Cqh_sql_map[bmjb]['all'] else Cqh_sql_map['all']['all']
        else:
            if xfxs:
                Cqh_level = get_qh_level(g.get('reqdicts_before_pt').get('Cqh'))
                sql_item = Cqh_sql_map[Cqh_level]['xfxs'] if Cqh_sql_map[Cqh_level]['xfxs'] else Cqh_sql_map['all'][
                    'xfxs']
            else:
                Cqh_level = get_qh_level(g.get('reqdicts_before_pt').get('Cqh'))
                sql_item = Cqh_sql_map[Cqh_level]['all'] if Cqh_sql_map[Cqh_level]['all'] else Cqh_sql_map['all']['all']
        sql_map = get_sql_map(DEBUG)
        sql, columns = None, None
        if sql_item in ["jssllv_zrdw_all_list", "jssllv_zrdw_xfxs_list"]:
            if g.get('reqdicts_before_pt').get('Cqh') == '广东省':
                sql, self.columns = sql_map[sql_item]
                sql = sql + " where a.company_name in ('广东省住房和城乡建设厅','广东省交通运输厅','广东省水利厅','广东省农业农村厅','广东省卫生健康委员会','广东省国资委','广东省市场监督管理局','广东省应急管理厅','广东省地方金融监督管理局','广东省公安厅','广东省民政厅','广东省司法厅','广东省人力资源和社会保障厅','广东省生态环境厅','广东省教育厅','广东省自然资源厅','广东省科技厅','广东省商务厅','广东省退役军人事务厅')"
            else:
                sql, self.columns = sql_map[sql_item]
        else:
            sql, self.columns = sql_map[sql_item]
        self.apis_copy['value'] = 'wxzb'
        if sql_item.endswith('nums'):
            self.apis_copy['value'] = 'xfjc'
        self.sql = sql.format(**g.get("reqdicts_before_pt")).format(**self.apis_copy)

    def search(self):

        from utils.db_connection import fx_engine
        from utils.results2df import results2df

        results = fx_engine.execute(self.sql)
        data = results2df(results, self.columns)
        self.df = data

    def after_search(self):
        return
