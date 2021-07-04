from flask import g

from libs.extensions import Extension
import pandas as pd

from settings.gdxf.extensions.mylv.base_sql_map import get_base_sql_map
from utils.qh_processor import get_qh_level

DEBUG = False


def get_sql_map(flag):
    if flag:
        base_sql_map = {
            "1-1-全": "1_2",
        }
    else:
        base_sql_map = get_base_sql_map()
    sql_map = {
        # 区划分布 --> 全部 --> 信访部门 【一个数】 省级
        "mylv_qh_all_xfbm_shej": (
            f"select (sum(a.my)+sum(a.jbmy))/sum(a.ypj) as mylv from {base_sql_map['1-1-全']} as a",
            ["mylv"]),
        # 区划分布 --> 全部 --> 信访部门 【一个数】 市级
        "mylv_qh_all_xfbm_shij": (
            f"select (a.my+a.jbmy)/a.ypj as mylv from {base_sql_map['1-1-全']} as a where a.region_name='{{Cqh}}'",
            ["mylv"]),
        # 区划分布 --> 全部 --> 信访部门 【一个数】 县级
        "mylv_qh_all_xfbm_xj": (
            f"select (a.my+a.jbmy)/a.ypj as mylv from {base_sql_map['2-1-全']} as a where a.region_name='{{Cqh}}'",
            ["mylv"]),

        # 区划分布 -->全部--> 信访部门 -->地图【name/value】 省级
        "mylv_qh_all_xfbm_allshej": (
            f"select a.region_name as qh,(a.my+a.jbmy)/a.ypj as mylv from {base_sql_map['1-1-全']} as a",
            ["qh", "mylv"]),
        # 区划分布 -->全部--> 信访部门 -->地图【name/value】 市级
        "mylv_qh_all_xfbm_allshij": (
            f"select a.region_name as qh,(a.my+a.jbmy)/a.ypj as mylv from {base_sql_map['2-1-全']} as a",
            ["qh", "mylv"]),

        # 区划分布 --> 全部 --> 责任单位 【一个数】 省级
        "mylv_qh_all_zrdw_shej": (
            f"select (sum(a.my)+sum(a.jbmy))/sum(a.ypj) as mylv from {base_sql_map['1-2-全']} as a",
            ["mylv"]),
        # 区划分布 --> 全部 --> 责任单位 【一个数】 市级
        "mylv_qh_all_zrdw_shij": (
            f"select (a.my+a.jbmy)/a.ypj as mylv from {base_sql_map['1-2-全']} as a where a.region_name='{{Cqh}}'",
            ["mylv"]),
        # 区划分布 --> 全部 --> 责任单位 【一个数】 县级
        "mylv_qh_all_zrdw_xj": (
            f"select (a.my+a.jbmy)/a.ypj as mylv from {base_sql_map['2-2-全']} as a where a.region_name='{{Cqh}}'",
            ["mylv"]),

        # 区划分布 -->全部--> 责任单位 -->地图？【name/value】 省级
        "mylv_qh_all_zrdw_allshej": (
            f"select a.region_name as qh,(a.my+a.jbmy)/a.ypj as mylv from {base_sql_map['1-2-全']} as a",
            ["qh", "mylv"]),
        # 区划分布 -->全部--> 责任单位 -->地图？【name/value】 市级
        "mylv_qh_all_zrdw_allshij": (
            f"select a.region_name as qh,(a.my+a.jbmy)/a.ypj as mylv from {base_sql_map['2-2-全']} as a",
            ["qh", "mylv"]),

        # 区划分布 --> 信访形式 --> 信访部门 【一个数】 省级
        "mylv_qh_xfxs_xfbm_shej": (
            f"select (sum(a.my)+sum(a.jbmy))/sum(a.ypj) as mylv from {base_sql_map['1-1-形式']} as a",
            ["mylv"]),
        # 区划分布 --> 信访形式 --> 信访部门 【一个数】 市级
        "mylv_qh_xfxs_xfbm_shij": (
            f"select (a.my+a.jbmy)/a.ypj as mylv from {base_sql_map['1-1-形式']} as a where a.region_name='{{Cqh}}'",
            ["mylv"]),
        # 区划分布 --> 信访形式 --> 信访部门 【一个数】 县级
        "mylv_qh_xfxs_xfbm_xj": (
            f"select (a.my+a.jbmy)/a.ypj as mylv from {base_sql_map['2-1-形式']} as a where a.region_name='{{Cqh}}'",
            ["mylv"]),

        # 区划分布 -->信访形式--> 信访部门 -->地图【name/value】 省级
        "mylv_qh_xfxs_xfbm_allshej": (
            f"select a.region_name as qh,(a.my+a.jbmy)/a.ypj as mylv from {base_sql_map['1-1-形式']} as a",
            ["qh", "mylv"]),
        # 区划分布 -->信访形式--> 信访部门 -->地图【name/value】 市级
        "mylv_qh_xfxs_xfbm_allshij": (
            f"select a.region_name as qh,(a.my+a.jbmy)/a.ypj as mylv from {base_sql_map['2-1-形式']} as a",
            ["qh", "mylv"]),

        # 区划分布 --> 信访形式--> 责任单位 【一个数】 省级
        "mylv_qh_xfxs_zrdw_shej": (
            f"select (sum(a.my)+sum(a.jbmy))/sum(a.ypj)as mylv from {base_sql_map['1-2-形式']} as a",
            ["mylv"]),
        # 区划分布 --> 信访形式--> 责任单位 【一个数】 市级
        "mylv_qh_xfxs_zrdw_shij": (
            f"select (a.my+a.jbmy)/a.ypj as mylv from {base_sql_map['1-2-形式']} as a where a.region_name='{{Cqh}}'",
            ["mylv"]),
        # 区划分布 --> 信访形式--> 责任单位 【一个数】 县级
        "mylv_qh_xfxs_zrdw_xj": (
            f"select (a.my+a.jbmy)/a.ypj as mylv from {base_sql_map['2-2-形式']} as a where a.region_name='{{Cqh}}'",
            ["mylv"]),

        # 区划分布 -->信访形式--> 责任单位 -->地图？【name/value】 省级
        "mylv_qh_xfxs_zrdw_allshej": (
            f"select a.region_name as qh,(a.my+a.jbmy)/a.ypj as mylv from {base_sql_map['1-2-形式']} as a",
            ["qh", "mylv"]),
        # 区划分布 -->信访形式--> 责任单位 -->地图？【name/value】 市级
        "mylv_qh_xfxs_zrdw_allshij": (
            f"select a.region_name as qh,(a.my+a.jbmy)/a.ypj as mylv from {base_sql_map['1-2-形式']} as a",
            ["qh", "mylv"]),

        # 信访部门 -->全部--> 【三种情况】 省级
        "mylv_xfbm_all_shejnums": (
            f"SELECT case a.jbmy when a.jbmy then '基本满意' end as myqk,sum(a.jbmy) as 'xfjc' FROM {base_sql_map['1-1-全']} as a UNION SELECT case a.my when a.my then '满意' end as myqk ,sum(a.my) as 'xfjc'  FROM {base_sql_map['1-1-全']} as a UNION SELECT case a.bmy when a.bmy then '不满意' end as myqk ,sum(a.bmy) as 'xfjc' FROM {base_sql_map['1-1-全']} as a",
            ["myqk", "xfjc"]),
        # 信访部门 -->全部--> 【三种情况】 市级
        "mylv_xfbm_all_shijnums": (
            f"SELECT case a.jbmy when a.jbmy then '基本满意' end as myqk,a.jbmy as 'xfjc' FROM {base_sql_map['1-1-全']} as a WHERE a.region_name='{{Cqh}}' UNION SELECT case a.my when a.my then '满意' end as myqk ,a.my as 'xfjc'  FROM {base_sql_map['1-1-全']} as a WHERE a.region_name='{{Cqh}}' UNION SELECT case a.bmy when a.bmy then '不满意' end as myqk ,a.bmy as 'xfjc' FROM {base_sql_map['1-1-全']} as a where a.region_name='{{Cqh}}'",
            ["myqk", "xfjc"]),
        # 信访部门 -->全部--> 【三种情况】 县级
        "mylv_xfbm_all_xjnums": (
            f"SELECT case a.jbmy when a.jbmy then '基本满意' end as myqk,a.jbmy as 'xfjc' FROM {base_sql_map['2-1-全']} as a WHERE a.region_name='{{Cqh}}' UNION SELECT case a.my when a.my then '满意' end as myqk ,a.my as 'xfjc'  FROM {base_sql_map['2-1-全']} as a WHERE a.region_name='{{Cqh}}' UNION SELECT case a.bmy when a.bmy then '不满意' end as myqk ,a.bmy as 'xfjc' FROM {base_sql_map['2-1-全']} as a where a.region_name='{{Cqh}}'",
            ["myqk", "xfjc"]),

        # 信访部门 -->信访形式--> 【三种情况】 省级
        "mylv_xfbm_xfxs_shejnums": (
            f"SELECT case a.jbmy when a.jbmy then '基本满意' end as myqk,sum(a.jbmy) as 'xfjc' FROM {base_sql_map['1-1-形式']} as a UNION SELECT case a.my when a.my then '满意' end as myqk ,sum(a.my) as 'xfjc'  FROM {base_sql_map['1-1-形式']} as a UNION SELECT case a.bmy when a.bmy then '不满意' end as myqk ,sum(a.bmy) as 'xfjc' FROM {base_sql_map['1-1-形式']} as a",
            ["myqk", "xfjc"]),
        # 信访部门 -->信访形式--> 【三种情况】 市级
        "mylv_xfbm_xfxs_shijnums": (
            f"SELECT case a.jbmy when a.jbmy then '基本满意' end as myqk,a.jbmy as 'xfjc' FROM {base_sql_map['1-1-形式']} as a WHERE a.region_name='{{Cqh}}' UNION SELECT case a.my when a.my then '满意' end as myqk ,a.my as 'xfjc'  FROM {base_sql_map['1-1-形式']} as a WHERE a.region_name='{{Cqh}}' UNION SELECT case a.bmy when a.bmy then '不满意' end as myqk ,a.bmy as 'xfjc' FROM {base_sql_map['1-1-形式']} as a where a.region_name='{{Cqh}}'",
            ["myqk", "xfjc"]),
        # 信访部门 -->信访形式--> 【三种情况】 县级
        "mylv_xfbm_xfxs_xjnums": (
            f"SELECT case a.jbmy when a.jbmy then '基本满意' end as myqk,a.jbmy as 'xfjc' FROM {base_sql_map['2-1-形式']} as a WHERE a.region_name='{{Cqh}}' UNION SELECT case a.my when a.my then '满意' end as myqk ,a.my as 'xfjc'  FROM {base_sql_map['2-1-形式']} as a WHERE a.region_name='{{Cqh}}' UNION SELECT case a.bmy when a.bmy then '不满意' end as myqk ,a.bmy as 'xfjc' FROM {base_sql_map['2-1-形式']} as a where a.region_name='{{Cqh}}'",
            ["myqk", "xfjc"]),

        # 信访部门排名用地图

        # 责任单位 --> 全部 --> 【三种情况】 省级
        "mylv_zrdw_all_shejnums": (
            f"SELECT case a.jbmy when a.jbmy then '基本满意' end as myqk,sum(a.jbmy) as 'xfjc' FROM {base_sql_map['1-2-全']} as a UNION SELECT case a.my when a.my then '满意' end as myqk ,sum(a.my) as 'xfjc'  FROM {base_sql_map['1-2-全']} as a UNION SELECT case a.bmy when a.bmy then '不满意' end as myqk ,sum(a.bmy) as 'xfjc' FROM {base_sql_map['1-2-全']} as a",
            ["myqk", "xfjc"]),
        # 责任单位 --> 全部 --> 【三种情况】 市级
        "mylv_zrdw_all_shijnums": (
            f"SELECT case a.jbmy when a.jbmy then '基本满意' end as myqk,a.jbmy as 'xfjc' FROM {base_sql_map['1-2-全']} as a WHERE a.region_name='{{Cqh}}' UNION SELECT case a.my when a.my then '满意' end as myqk ,a.my as 'xfjc'  FROM {base_sql_map['1-2-全']} as a WHERE a.region_name='{{Cqh}}' UNION SELECT case a.bmy when a.bmy then '不满意' end as myqk ,a.bmy as 'xfjc' FROM {base_sql_map['1-2-全']} as a where a.region_name='{{Cqh}}'",
            ["myqk", "xfjc"]),
        # 责任单位 --> 全部 --> 【三种情况】 县级
        "mylv_zrdw_all_xjnums": (
            f"SELECT case a.jbmy when a.jbmy then '基本满意' end as myqk,a.jbmy as 'xfjc' FROM {base_sql_map['2-2-全']} as a WHERE a.region_name='{{Cqh}}' UNION SELECT case a.my when a.my then '满意' end as myqk ,a.my as 'xfjc'  FROM {base_sql_map['2-2-全']} as a WHERE a.region_name='{{Cqh}}' UNION SELECT case a.bmy when a.bmy then '不满意' end as myqk ,a.bmy as 'xfjc' FROM {base_sql_map['2-2-全']} as a where a.region_name='{{Cqh}}'",
            ["myqk", "xfjc"]),

        # 责任单位 --> 全部 --> 排名（省级）19个
        "mylv_zrdw_all_allshej": (
            f"select a.company_name as qh,(a.my+a.jbmy)/a.ypj as mylv from {base_sql_map['1-3-全']} as a",
            ["qh", "mylv"]),
        # 责任单位 --> 全部 --> 排名(市级)
        "mylv_zrdw_all_allshij": (
            f"select a.region_name as qh,(a.my+a.jbmy)/a.ypj as mylv from {base_sql_map['2-2-全']} as a",
            ["qh", "mylv"]),

        # 责任单位 --> 信访形式 --> 【三种情况】 省级
        "mylv_zrdw_xfxs_shejnums": (
            f"SELECT case a.jbmy when a.jbmy then '基本满意' end as myqk,sum(a.jbmy) as 'xfjc' FROM {base_sql_map['1-2-形式']} as a UNION SELECT case a.my when a.my then '满意' end as myqk ,sum(a.my) as 'xfjc'  FROM {base_sql_map['1-2-形式']} as a UNION SELECT case a.bmy when a.bmy then '不满意' end as myqk ,sum(a.bmy) as 'xfjc' FROM {base_sql_map['1-2-形式']} as a",
            ["myqk", "xfjc"]),
        # 责任单位 --> 信访形式 --> 【三种情况】 市级
        "mylv_zrdw_xfxs_shijnums": (
            f"SELECT case a.jbmy when a.jbmy then '基本满意' end as myqk,a.jbmy as 'xfjc' FROM {base_sql_map['1-2-形式']} as a WHERE a.region_name='{{Cqh}}' UNION SELECT case a.my when a.my then '满意' end as myqk ,a.my as 'xfjc'  FROM {base_sql_map['1-2-形式']} as a WHERE a.region_name='{{Cqh}}' UNION SELECT case a.bmy when a.bmy then '不满意' end as myqk ,a.bmy as 'xfjc' FROM {base_sql_map['1-2-形式']} as a where a.region_name='{{Cqh}}'",
            ["myqk", "xfjc"]),
        # 责任单位 --> 信访形式 --> 【三种情况】 县级
        "mylv_zrdw_xfxs_xjnums": (
            f"SELECT case a.jbmy when a.jbmy then '基本满意' end as myqk,a.jbmy as 'xfjc' FROM {base_sql_map['2-2-形式']} as a WHERE a.region_name='{{Cqh}}' UNION SELECT case a.my when a.my then '满意' end as myqk ,a.my as 'xfjc'  FROM {base_sql_map['2-2-形式']} as a WHERE a.region_name='{{Cqh}}' UNION SELECT case a.bmy when a.bmy then '不满意' end as myqk ,a.bmy as 'xfjc' FROM {base_sql_map['2-2-形式']} as a where a.region_name='{{Cqh}}'",
            ["myqk", "xfjc"]),

        # 责任单位 --> 信访形式 --> 排名（省级）19个
        "mylv_zrdw_xfxs_allshej": (
            f"select a.company_name as qh,(a.my+a.jbmy)/a.ypj as mylv from {base_sql_map['1-3-形式']} as a where a.xfxs='{{xfxs}}'",
            ["qh", "mylv"]),
        # 责任单位 --> 信访形式 --> 排名(市级)
        "mylv_zrdw_xfxs_allshij": (
            f"select a.region_name as qh,(a.my+a.jbmy)/a.ypj as mylv from {base_sql_map['2-2-形式']} as a",
            ["qh", "mylv"]),
    }
    return sql_map


class Mylv(Extension):
    """满意率"""
    """
    计算公式：使用已提供的SQL语句进行计算
    """

    def __init__(self, apis_copy, apis, *args, **kwargs):
        self.sql, self.columns = None, None
        super(Mylv, self).__init__(apis_copy, apis)  # 执行父类方法，获得self.apis/self.apis_copy

    def before_search(self):
        self.df = pd.DataFrame([None], columns=["mylv"])
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
        if sql_item in ["mylv_zrdw_all_allshej", "mylv_zrdw_xfxs_allshej"]:
            if g.get('reqdicts_before_pt').get('Cqh') == '广东省':
                qh_list = ['广东省住房和城乡建设厅', '广东省交通运输厅', '广东省水利厅', '广东省农业农村厅', '广东省卫生健康委员会', '广东省国资委', '广东省市场监督管理局',
                           '广东省应急管理厅', '广东省地方金融监督管理局', '广东省公安厅', '广东省民政厅', '广东省司法厅', '广东省人力资源和社会保障厅', '广东省生态环境厅',
                           '广东省教育厅', '广东省自然资源厅', '广东省科技厅', '广东省商务厅', '广东省退役军人事务厅']
                g.modified_initialization.update({'qh': qh_list})
                sql, self.columns = sql_map[sql_item]
            else:
                sql, self.columns = sql_map[sql_item]
        else:
            sql, self.columns = sql_map[sql_item]
        self.apis_copy['value'] = 'mylv'
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
