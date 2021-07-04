from libs.extensions import Extension
import pandas as pd

from settings.gdxf.extensions.aqdflv.get_base_sql_map import get_base_sql_map

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
            f"select a.aqdf/(a.aqdf+a.cqdf+a.wdf+a.cqwdf) as aqdflv from {base_sql_map['3-2-全']} as a where a.region_name='广东省'",
            ["aqdflv"]),
        # 区划分布 --> 全部 --> 总体 【一个数】 市级
        "aqdflv_qh_all_shij": (
            f"select a.aqdf/(a.aqdf+a.cqdf+a.wdf+a.cqwdf) as aqdflv from {base_sql_map['3-4-全']} as a where a.region_name='广东市'",
            ["aqdflv"]),
        # 区划分布 --> 信访形式 --> 总体 【一个数】 省级
        "aqdflv_qh_xfxs_shej": (
            f"select a.aqdf/(a.aqdf+a.cqdf+a.wdf+a.cqwdf) as aqdflv from {base_sql_map['3-2-形式']} as a where a.region_name='广东省'",
            ["aqdflv"]),
        # 区划分布 --> 信访形式 --> 总体 【一个数】 市级
        "aqdflv_qh_xfxs_shij": (
            f"select a.aqdf/(a.aqdf+a.cqdf+a.wdf+a.cqwdf) as aqdflv from {base_sql_map['3-4-形式']} as a where a.region_name='广东市'",
            ["aqdflv"]),

        # 地图
        # 区划分布 --> 全部 --> 总体 【name/value】 省级
        "aqdflv_qh_all_allshej": (
            f"select a.region_name as 'qh',a.aqdf/(a.aqdf+a.cqdf+a.wdf+a.cqwdf) as aqdflv from {base_sql_map['3-2-全']} as a where a.region_name !='广东省'",
            ["qh", "aqdflv"]),
        # 区划分布 --> 全部 --> 总体 【name/value】 市级
        "aqdflv_qh_all_allshij": (
            f"select a.region_name as 'qh',a.aqdf/(a.aqdf+a.cqdf+a.wdf+a.cqwdf) as aqdflv from {base_sql_map['3-4-全']} as a",
            ["qh", "aqdflv"]),
        # 区划分布 --> 信访形式 --> 总体 【name/value】 省级
        "aqdflv_qh_xfxs_allshej": (
            f"select a.region_name as 'qh',a.aqdf/(a.aqdf+a.cqdf+a.wdf+a.cqwdf) as aqdflv from {base_sql_map['3-2-形式']} as a where a.region_name !='广东省'",
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
        self.df = pd.DataFrame([None], columns=["aqdflv"])

    def search(self):
        # self.apis_copy["xfjc"] = "jssllv"

        sql_list = self.apis_copy['ext'].split('/')
        Cqh_sql_map = {}
        for item in sql_list:
            if 'shej' in item:
                Cqh_sql_map['shej_02'] = item
            elif 'shij' in item:
                Cqh_sql_map['shij_02'] = item
            elif 'xj' in item:
                Cqh_sql_map['xj_02'] = item
            else:
                Cqh_sql_map['all'] = item

        # if g.get('before_param_trans')['bmjb'] == '省级':
        #     bmjb = 'shej_02'
        # elif g.get('before_param_trans')['bmjb'] == '市级':
        #     bmjb = 'shi_02'
        # elif g.get('before_param_trans')['bmjb'] == '县级':
        #     bmjb = 'xj_02'
        # else:
        #     bmjb = 'all'
        #
        # if bmjb:
        #     sql_item = Cqh_sql_map[bmjb] if bmjb in Cqh_sql_map else Cqh_sql_map['all']
        # else:
        #     Cqh_level = get_qh_level(g.get('before_param_trans')['Cqh'])
        #     sql_item = Cqh_sql_map[Cqh_level] if Cqh_level in Cqh_sql_map else Cqh_sql_map['all']

        sql_item = sql_list[0]
        sql_map = get_sql_map(DEBUG)
        # 按期答复率为3-4（市）3-2（省）

        from utils.db_connection import fx_engine
        from utils.results2df import results2df

        sql, columns = sql_map[sql_item]
        self.apis_copy['value'] = 'aqdflv'

        from flask import g
        results = fx_engine.execute(sql.format(**g.get("reqdicts_before_pt")).format(**self.apis_copy))
        data = results2df(results, columns)
        self.df = data

    def after_search(self):
        return
