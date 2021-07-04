from libs.extensions import Extension
import pandas as pd
from flask import g
from settings.gdxf.extensions.aqdflv.get_base_sql_map import get_base_sql_map
from utils.qh_processor import get_qh_level
DEBUG = True


def get_sql_map(flag):
    if flag:
        base_sql_map = {
            "3-4-全": "3_4",
            "3-4-形式": "3_4",
            "3-2-全": "3_2",
            "3-2-形式": "3_2"
        }
    else:
        base_sql_map = get_base_sql_map()
    sql_map = {
        # 区划分布 --> 全部 --> 总体 【一个数】 省级
        "aqdflv_qh_all_shej": (
            f"select a.aqdf/(a.aqdf+a.cqdf+a.wdf+a.cqwdf) as aqdflv from {base_sql_map['3-2-全']} as a where a.region_name='{{Cqh}}'",
            ["aqdflv"]),
        # 区划分布 --> 全部 --> 总体 【一个数】 市级
        "aqdflv_qh_all_shij": (
            f"select a.aqdf/(a.aqdf+a.cqdf+a.wdf+a.cqwdf) as aqdflv from {base_sql_map['3-4-全']} as a where a.region_name='{{Cqh}}'",
            ["aqdflv"]),
        # 区划分布 --> 信访形式 --> 总体 【一个数】 省级
        "aqdflv_qh_xfxs_shej": (
            f"select a.aqdf/(a.aqdf+a.cqdf+a.wdf+a.cqwdf) as aqdflv from {base_sql_map['3-2-形式']} as a where a.region_name='{{Cqh}}'",
            ["aqdflv"]),
        # 区划分布 --> 信访形式 --> 总体 【一个数】 市级
        "aqdflv_qh_xfxs_shij": (
            f"select a.aqdf/(a.aqdf+a.cqdf+a.wdf+a.cqwdf) as aqdflv from {base_sql_map['3-4-形式']} as a where a.region_name='{{Cqh}}'",
            ["aqdflv"]),

        # 地图
        # 区划分布 --> 全部 --> 总体 【name/value】 省级
        "aqdflv_qh_all_allshej": (
            f"select a.region_name as 'qh',a.aqdf/(a.aqdf+a.cqdf+a.wdf+a.cqwdf) as aqdflv from {base_sql_map['3-2-全']} as a",
            ["qh", "aqdflv"]),
        # 区划分布 --> 全部 --> 总体 【name/value】 市级
        "aqdflv_qh_all_allshij": (
            f"select a.region_name as 'qh',a.aqdf/(a.aqdf+a.cqdf+a.wdf+a.cqwdf) as aqdflv from {base_sql_map['3-4-全']} as a",
            ["qh", "aqdflv"]),
        # 区划分布 --> 信访形式 --> 总体 【name/value】 省级
        "aqdflv_qh_xfxs_allshej": (
            f"select a.region_name as 'qh',a.aqdf/(a.aqdf+a.cqdf+a.wdf+a.cqwdf) as aqdflv from {base_sql_map['3-2-形式']} as a",
            ["qh", "aqdflv"]),
        # 区划分布 --> 信访形式 --> 总体 【name/value】 市级
        "aqdflv_qh_xfxs_allshij": (
            f"select a.region_name as 'qh',a.aqdf/(a.aqdf+a.cqdf+a.wdf+a.cqwdf) as aqdflv from {base_sql_map['3-4-形式']} as a",
            ["qh", "aqdflv"]),

    }
    return sql_map


class Aqdflv(Extension):
    """按期答复率"""
    """
    计算公式：使用已提供的SQL语句进行计算
    """

    def __init__(self, apis_copy, apis, *args, **kwargs):
        super(Aqdflv, self).__init__(apis_copy, apis)  # 执行父类方法，获得self.apis/self.apis_copy

    def before_search(self):
        sql_list = self.apis_copy['ext'].split('/')
        Cqh_sql_map = {'shej_02': {'all': None, 'xfxs': None}, 'shij_02': {'all':None,'xfxs':None}, 'xj_02': {'all':None,'xfxs':None}, 'all': {'all':None,'xfxs':None}}
        for item in sql_list:
            if 'xfxs' in item:
                Cqh_sql_map['all']['xfxs'] = item  # 把省级写入默认的all中，cqh出错也能兼容
                if 'shej' in item:
                    Cqh_sql_map['shej_02']['xfxs'] = item
                elif 'shij' in item:
                    Cqh_sql_map['shij_02']['xfxs'] = item
                elif 'xj' in item:
                    Cqh_sql_map['xj_02']['xfxs'] = item

            else:
                Cqh_sql_map['all']['all'] = item
                if 'shej' in item:
                    Cqh_sql_map['shej_02']['all'] = item
                elif 'shij' in item:
                    Cqh_sql_map['shij_02']['all'] = item
                elif 'xj' in item:
                    Cqh_sql_map['xj_02']['all'] = item

        from flask import g
        xfxs = g.get('reqdicts_before_pt').get('xfxs')
        # 根据级别进不同的sql
        if xfxs:
            Cqh_level = get_qh_level(g.get('reqdicts_before_pt').get('Cqh'))
            sql_item = Cqh_sql_map[Cqh_level]['xfxs'] if Cqh_level in Cqh_sql_map else Cqh_sql_map['all']['xfxs']
        else:
            Cqh_level = get_qh_level(g.get('reqdicts_before_pt').get('Cqh'))
            sql_item = Cqh_sql_map[Cqh_level]['all'] if Cqh_level in Cqh_sql_map else Cqh_sql_map['all']['all']

        sql_map = get_sql_map(DEBUG)
        # 按期答复率为3-4（市）3-2（省）
        self.sql, self.columns = sql_map[sql_item]
        reqdicts_before_pt = g.get("reqdicts_before_pt")
        reqdicts_before_pt.pop("zrdw", "")
        sql_format = self.apis_copy.copy()
        sql_format.update(reqdicts_before_pt)
        self.sql = self.sql.format(**sql_format)

    def search(self):
        self.apis_copy['value'] = 'aqdflv'
        from utils.db_connection import fx_engine
        from utils.results2df import results2df
        results = fx_engine.execute(self.sql)
        data = results2df(results, self.columns)
        self.df = data

    def after_search(self):
        return
