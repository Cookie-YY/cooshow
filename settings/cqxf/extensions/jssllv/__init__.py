from flask import g

from libs.extensions import Extension
import pandas as pd

from settings.gdxf.extensions.jssllv.base_sql_map import get_base_sql_map
from utils.qh_processor import get_qh_level

DEBUG = True


def get_sql_map(flag):
    if flag:
        base_sql_map = {
            "1-2-形式": "1_2",
            "1-4-形式": "1_4",
            "2-2-形式": "2_2",
            "2-4-形式": "2_4",
            "1-5-形式": "1_5",
            "1-6-形式": "1_6",
            '2-5-形式': '2_5',
            "1-2-全": "1_2",
            "1-4-全": "1_4",
            "2-2-全": "2_2",
            "2-4-全": "2_4",
            "1-5-全": "1_5",
            "1-6-全": "1_6",
            '2-5-全': '2_5'
        }
    else:
        base_sql_map = get_base_sql_map()
    sql_map = {
        # 区划分布 --> 全部 --> 信访部门 （省） 【一个数】
        "jssllv_qh_all_xfbm_shej": (
            f"select a.jssl/a.zs as jssllv from {base_sql_map['1-2-全']} as a where a.region_name='{{Cqh}}'",
            ["jssllv"]),
        # 区划分布 --> 全部 --> 信访部门 （省） 【三种情况】 *
        "jssllv_qh_all_xfbm_shej_nums": (
            f"SELECT case a.jssl when a.jssl then '及时受理' end as slqk,a.jssl as 'xfjc' FROM {base_sql_map['1-2-全']} as a WHERE a.region_name='{{Cqh}}' UNION SELECT case a.cqsl when a.cqsl then '超期受理' end as slqk ,a.cqsl as 'xfjc' FROM {base_sql_map['1-2-全']} as a WHERE a.region_name='{{Cqh}}' UNION SELECT case a.cqwsl when a.cqwsl then '超期未受理' end as slqk ,a.cqwsl as 'xfjc' FROM {base_sql_map['1-2-全']} as a where a.region_name='{{Cqh}}'",
            ["slqk", "xfjc"]),
        # 区划分布 --> 全部 --> 信访部门 （xx市） 【一个数】
        "jssllv_qh_all_xfbm_shij": (
            f"select a.jssl/a.zs as jssllv from {base_sql_map['1-4-全']} as a where a.region_name='{{Cqh}}'",
            ["jssllv", "xfjc"]),
        # 区划分布 --> 全部 --> 信访部门 （xx市） 【三种情况】 *
        "jssllv_qh_all_xfbm_shij_nums": (
            f"SELECT case a.jssl when a.jssl then '及时受理' end as slqk,a.jssl as 'xfjc' FROM {base_sql_map['1-4-全']} as a WHERE a.region_name='{{Cqh}}' UNION SELECT case a.cqsl when a.cqsl then '超期受理' end as slqk ,a.cqsl as 'xfjc'  FROM {base_sql_map['1-4-全']} as a WHERE a.region_name='{{Cqh}}' UNION SELECT case a.cqwsl when a.cqwsl then '超期未受理' end as slqk ,a.cqwsl as 'xfjc' FROM {base_sql_map['1-4-全']} as a where a.region_name='{{Cqh}}'",
            ["slqk", "xfjc"]),
        # 区划分布 --> 全部 --> 信访部门 （各个市） 【name/value】
        "jssllv_qh_all_xfbm_allshij": (
            f"select a.region_name as qh,a.jssl/a.zs as jssllv from {base_sql_map['1-4-全']} as a",
            ["qh", "jssllv"]),
        # 区划分布 --> 全部 --> 信访部门 （某个市的某个县） 【value】
        "jssllv_qh_all_xfbm_xj": "",
        # 区划分布 --> 全部 --> 信访部门 （某个市的各个县） 【name/value】
        "jssllv_qh_all_xfbm_allxj": "",
        # 区划分布 --> 全部 --> 责任单位 （省） 【一个数】
        "jssllv_qh_all_zrdw_shej": (
            f"select a.jssl/a.zs as jssllv from {base_sql_map['2-2-全']} as a where a.region_name='{{Cqh}}'",
            ["jssllv"]),
        # 区划分布 --> 全部 --> 责任单位 （省） 【三种情况】 *
        "jssllv_qh_all_zrdw_shej_nums": (
            f"SELECT case a.jssl when a.jssl then '及时受理' end as slqk,a.jssl as 'xfjc' FROM {base_sql_map['2-2-全']} as a WHERE a.region_name='{{Cqh}}' UNION SELECT case a.cqsl when a.cqsl then '超期受理' end as slqk ,a.cqsl as 'xfjc' FROM {base_sql_map['2-2-全']} as a WHERE a.region_name='{{Cqh}}' UNION SELECT case a.cqwsl when a.cqwsl then '超期未受理' end as slqk ,a.cqwsl as 'xfjc' FROM {base_sql_map['2-2-全']} as a where a.region_name='{{Cqh}}'",
            ["slqk", "xfjc"]),
        # 区划分布 --> 全部 --> 责任单位 （xx市） 【一个数】
        "jssllv_qh_all_zrdw_shij": (
            f"select a.jssl/a.zs as jssllv from {base_sql_map['2-4-全']} as a where a.region_name='{{Cqh}}'",
            ["slqk", "jssllv"]),
        # 区划分布 --> 全部 --> 责任单位 （xx市） 【三种情况】 *
        "jssllv_qh_all_zrdw_shij_nums": (
            f"SELECT case a.jssl when a.jssl then '及时受理' end as slqk,a.jssl as 'xfjc' FROM {base_sql_map['2-4-全']} as a WHERE a.region_name='{{Cqh}}' UNION SELECT case a.cqsl when a.cqsl then '超期受理' end as slqk ,a.cqsl as 'xfjc'  FROM {base_sql_map['2-4-全']} as a WHERE a.region_name='{{Cqh}}' UNION SELECT case a.cqwsl when a.cqwsl then '超期未受理' end as slqk ,a.cqwsl as 'xfjc' FROM {base_sql_map['2-4-全']} as a where a.region_name='{{Cqh}}'",
            ["slqk", "xfjc"]),
        # 区划分布 --> 全部 --> 责任单位 （各个市） 【name/value】
        "jssllv_qh_all_zrdw_allshij": (
            f"select a.region_name as qh,a.jssl/a.zs as jssllv from {base_sql_map['2-4-全']} as a",
            ["qh", "jssllv"]),
        # 区划分布 --> 全部 --> 责任单位 （某个市的某个县） 【value】
        # 区划分布 --> 全部 --> 责任单位 （某个市的各个县） 【name/value】

        # 区划分布 --> 信访形式 --> 信访部门 （省） 【一个数】
        "jssllv_qh_xfxs_xfbm_shej": (
            f"select a.jssl/a.zs as jssllv from {base_sql_map['1-2-形式']} as a where a.region_name = '{{Cqh}}' and a.xfxs='{{xfxs}}'",
            ["jssllv"]),
        # 区划分布 --> 信访形式 --> 信访部门 （xx市） 【一个数】
        "jssllv_qh_xfxs_xfbm_shij": (
            f"select a.jssl/a.zs as jssllv from {base_sql_map['1-4-形式']} as a where a.region_name = '{{Cqh}}' and a.xfxs='{{xfxs}}'",
            ["jssllv"]),
        # 区划分布 --> 信访形式 --> 信访部门 （各个市） 【name/value】
        "jssllv_qh_xfxs_xfbm_allshij": (
            f"select a.region_name as qh,a.jssl/a.zs as jssllv from {base_sql_map['1-4-形式']} as a where a.xfxs='{{xfxs}}'",
            ["qh", "jssllv"]),
        # 区划分布 --> 信访形式 --> 信访部门 （某个市的某个县） 【value】
        # 区划分布 --> 信访形式 --> 信访部门 （某个市的各个县） 【name/value】

        # 区划分布 --> 信访形式 --> 责任单位 （省） 【一个数】
        "jssllv_qh_xfxs_zrdw_shej": (
            f"select a.jssl/a.zs as jssllv from {base_sql_map['2-2-形式']} as a where a.region_name = '{{Cqh}}' and a.xfxs='{{xfxs}}'",
            ["jssllv"]),
        # 区划分布 --> 信访形式 --> 责任单位 （xx市） 【一个数】
        "jssllv_qh_xfxs_zrdw_shij": (
            f"select a.jssl/a.zs as jssllv from {base_sql_map['2-4-形式']} as a where a.region_name = '{{Cqh}}' and a.xfxs='{{xfxs}}'",
            ["jssllv"]),
        # 区划分布 --> 信访形式 --> 责任单位 （各个市） 【name/value】
        "jssllv_qh_xfxs_zrdw_allshij": (
            f"select a.region_name as qh,a.jssl/a.zs as jssllv from {base_sql_map['2-4-形式']} as a where a.xfxs='{{xfxs}}'",
            ["qh", "jssllv"]),
        # 区划分布 --> 信访形式 --> 责任单位 （某个市的某个县） 【value】
        # 区划分布 --> 信访形式 --> 责任单位 （某个市的各个县） 【name/value】

        # 信访部门 --> 全部 （省信访局的三种情况）【name/value】-------- 结果需要转置
        "jssllv_xfbm_all_shej_nums": (
            f"SELECT case a.jssl when a.jssl then '及时受理' end as slqk,a.jssl as 'xfjc' FROM {base_sql_map['1-5-全']} as a  WHERE a.company_name = '{{xfbm}}' UNION SELECT case a.cqsl when a.cqsl then '超期受理' end as slqk ,a.cqsl as 'xfjc'  FROM {base_sql_map['1-5-全']} as a  WHERE a.company_name = '{{xfbm}}' UNION SELECT case a.cqwsl when a.cqwsl then '超期未受理' end as slqk ,a.cqwsl as 'xfjc' FROM {base_sql_map['1-5-全']} as a WHERE a.company_name = '{{xfbm}}'",
            ["slqk", "xfjc"]),
        # 信访部门 --> 全部 （省信访局的及时受理率）【一个数】
        "jssllv_xfbm_all_shej_jssllv": (
            f"select a.jssl/a.zs as jssllv from {base_sql_map['1-5-全']} as a where a.company_name = '{{xfbm}}' ",
            ["jssllv"]),
        # 信访部门 --> 全部 （某个市信访局的三种情况）【name/value】-------- 结果需要转置
        # 信访部门 --> 全部 （某个市信访局的三种情况）【name/value】-------- 结果需要转置
        "jssllv_xfbm_all_shij_nums": (
            f"SELECT case a.jssl when a.jssl then '及时受理' end as slqk,a.jssl as 'xfjc' FROM {base_sql_map['1-6-全']} as a WHERE a.company_name = '{{xfbm}}' UNION SELECT case a.cqsl when a.cqsl then '超期受理' end as slqk ,a.cqsl as 'xfjc'  FROM {base_sql_map['1-6-全']} as a WHERE a.company_name = '{{xfbm}}'UNION SELECT case a.cqwsl when a.cqwsl then '超期未受理' end as slqk ,a.cqwsl as 'xfjc' FROM {base_sql_map['1-6-全']} as a WHEREa.company_name = '{{xfbm}}' ",
            ["slqk", "xfjc"]),  # 信访部门 --> 全部 （某个市信访局的及时受理率）【一个数】
        "jssllv_xfbm_all_shij_jssllv": (
            f"select a.jssl/a.zs as jssllv from {base_sql_map['1-6-全']} as a where a.company_name = '{{xfbm}}'",
            ["jssllv"]),

        # 信访部门 --> 信访形式 （省信访局的三种情况）【name/value】-------- 结果需要转置
        # 信访部门 --> 信访形式 （省信访局的三种情况）【name/value】-------- 结果需要转置
        "jssllv_xfbm_xfxs_shej_nums": (
            f"SELECT case a.jssl when a.jssl then '及时受理' end as slqk,a.jssl as 'xfjc' FROM {base_sql_map['1-5-形式']} as a WHERE a.company_name = '{{xfbm}}' UNION SELECT case a.cqsl when a.cqsl then '超期受理' end as slqk ,a.cqsl as 'xfjc'  FROM {base_sql_map['1-5-形式']} as a WHERE a.company_name = '{{xfbm}}'UNION SELECT case a.cqwsl when a.cqwsl then '超期未受理' end as slqk ,a.cqwsl as 'xfjc' FROM {base_sql_map['1-5-形式']} as a WHERE a.company_name = '{{xfbm}}'",
            ["slqk", "xfjc"]),  # 信访部门 --> 信访形式 （省信访局的及时受理率）【一个数】
        "jssllv_xfbm_xfxs_shej_jssllv": (
            f"select a.jssl/a.zs as jssllv from {base_sql_map['1-5-形式']} as a where a.company_name = '{{xfbm}}' and a.xfxs='{{xfxs}}'",
            ["jssllv"]),
        # 信访部门 --> 信访形式 （某个市信访局的三种情况）【name/value】-------- 结果需要转置
        # 信访部门 --> 信访形式 （某个市信访局的三种情况）【name/value】-------- 结果需要转置
        "jssllv_xfbm_xfxs_shij_nums": (
            f"SELECT case a.jssl when a.jssl then '及时受理' end as slqk,a.jssl as 'xfjc' FROM {base_sql_map['1-6-形式']} as a WHERE a.company_name = '{{xfbm}}' UNION SELECT case a.cqsl when a.cqsl then '超期受理' end as slqk ,a.cqsl as 'xfjc'  FROM {base_sql_map['1-6-形式']} as a WHERE a.company_name = '{{xfbm}}'UNION SELECT case a.cqwsl when a.cqwsl then '超期未受理' end as slqk ,a.cqwsl as 'xfjc' FROM {base_sql_map['1-6-形式']} as a WHERE a.company_name = '{{xfbm}}'",
            ["slqk", "xfjc"]),
        # 信访部门 --> 信访形式 （某个市信访局的及时受理率）【一个数】
        "jssllv_xfbm_xfxs_shij_jssllv": (
            f"select a.jssl/a.zs as jssllv from {base_sql_map['1-6-形式']} as a where a.company_name = '{{xfbm}}' and a.xfxs='{{xfxs}}'",
            ["jssllv"]),

        # 信访部门 --> 全部 --> 排名（省下辖的所有信访局的排名）【name/value】
        "jssllv_xfbm_all_shej_list": (
            f"select a.company_name as xfbm,a.jssl/a.zs as jssllv from {base_sql_map['1-5-全']} as a",
            ["xfbm", "jssllv"]),
        # 信访部门 --> 信访形式 --> 排名（省下辖的所有信访局的排名）【name/value】
        "jssllv_xfbm_xfxs_shej_list": (
            f"select a.company_name as xfbm,a.jssl/a.zs as jssllv from {base_sql_map['1-5-形式']} as a where a.xfxs='{{xfxs}}'",
            ["xfbm", "jssllv"]),
        # 信访部门 --> 全部 --> 排名（市下辖的所有信访局的排名）【name/value】
        "jssllv_xfbm_all_shij_list": (
            f"select a.company_name as xfbm,a.jssl/a.zs as jssllv from {base_sql_map['1-6-全']} as a",
            ["xfbm", "jssllv"]),
        # 信访部门 --> 信访形式 --> 排名（市下辖的所有信访局的排名）【name/value】
        "jssllv_xfbm_xfxs_shij_list": (
            f"select a.company_name as xfbm,a.jssl/a.zs as jssllv from {base_sql_map['1-6-形式']} as a where a.xfxs='{{xfxs}}'",
            ["xfbm", "jssllv"]),

        # 责任单位 --> 全部 （某一个责任单位的三种情况）【name/value】-------- 结果需要转置
        # 责任单位 --> 全部 （某一个责任单位的三种情况）【name/value】-------- 结果需要转置
        "jssllv_zrdw_all_nums": (
            f"SELECT case a.jssl when a.jssl then '及时受理' end as slqk,a.jssl as 'xfjc' FROM {base_sql_map['2-5-全']} as a WHERE a.company_name='{{zrdw}}' UNION SELECT case a.cqsl when a.cqsl then '超期受理' end as slqk ,a.cqsl as 'xfjc'  FROM {base_sql_map['2-5-全']} as a  WHERE a.company_name='{{zrdw}}' UNION SELECT case a.cqwsl when a.cqwsl then '超期未受理' end as slqk ,a.cqwsl as 'xfjc' FROM {base_sql_map['2-5-全']} as a where a.company_name='{{zrdw}}'",
            ["slqk", "xfjc"]),
        # 责任单位 --> 全部 （某一个责任单位的及时受理率）【一个数】
        "jssllv_zrdw_all_jssllv": (
            f"select a.jssl/a.zs as jssllv from {base_sql_map['2-5-全']} as a where a.company_name='{{zrdw}}'",
            ["jssllv"]),
        # 责任单位 --> 信访形式 （某一个责任单位的三种情况）【name/value】-------- 结果需要转置
        "jssllv_zrdw_xfxs_nums": (
            f"SELECT case a.jssl when a.jssl then '及时受理' end as slqk,a.jssl as 'xfjc' FROM {base_sql_map['2-5-形式']} as a WHERE a.company_name='{{zrdw}}' UNION SELECT case a.cqsl when a.cqsl then '超期受理' end as slqk ,a.cqsl as 'xfjc'  FROM {base_sql_map['2-5-形式']} as a WHERE a.company_name='{{zrdw}}' UNION SELECT case a.cqwsl when a.cqwsl then '超期未受理' end as slqk ,a.cqwsl as 'xfjc' FROM {base_sql_map['2-5-形式']} as a where a.company_name='{{zrdw}}'",
            ["slqk", "xfjc"]),
        # 责任单位 --> 信访形式 （某一个责任单位的及时受理率）【一个数】
        "jssllv_zrdw_xfxs_jssllv": (
            f"select a.jssl/a.zs as jssllv from {base_sql_map['2-5-形式']} as a where a.company_name='{{zrdw}}'",
            ["jssllv"]),
        # 责任单位 --> 全部 --> 排名（某一个责任单位下辖的所有责任单位的排名）【name/value】--------- 当是省级的时候，需要对结果再次过滤
        "jssllv_zrdw_shej_all_list": (
            f"select  a.company_name as zrdw,a.jssl/a.zs as jssllv from {base_sql_map['2-5-全']} as a",
            ["zrdw", "jssllv"]),
        # 责任单位 --> 信访形式 --> 排名（某一个责任单位下辖的所有责任单位的排名）【name/value】
        "jssllv_zrdw_shej_xfxs_list": (
            f"select a.company_name as zrdw, a.jssl/a.zs as jssllv from {base_sql_map['2-5-形式']} as a",
            ["zrdw", "jssllv"]),

    }
    return sql_map


class Jssllv(Extension):
    """及时受理率"""
    """
    计算公式：使用已提供的SQL语句进行计算
    """

    def __init__(self, apis_copy, apis, *args, **kwargs):
        super(Jssllv, self).__init__(apis_copy, apis)  # 执行父类方法，获得self.apis/self.apis_copy

    def before_search(self):
        # self.apis_copy["xfjc"] = "jssllv"

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

        if sql_item in ["jssllv_zrdw_all_list", "jssllv_zrdw_xfxs_list"]:
            if g.get('reqdicts_before_pt').get('Cqh') == '广东省':
                sql, columns = sql_map[sql_item]
                sql = sql + " where a.company_name in ('广东省住房和城乡建设厅','广东省交通运输厅','广东省水利厅','广东省农业农村厅','广东省卫生健康委员会','广东省国资委','广东省市场监督管理局','广东省应急管理厅','广东省地方金融监督管理局','广东省公安厅','广东省民政厅','广东省司法厅','广东省人力资源和社会保障厅','广东省生态环境厅','广东省教育厅','广东省自然资源厅','广东省科技厅','广东省商务厅','广东省退役军人事务厅')"
            else:
                sql, columns = sql_map[sql_item]
        else:
            sql, columns = sql_map[sql_item]
        self.apis_copy['value'] = 'jssllv'
        if sql_item.endswith('nums'):
            self.apis_copy['value'] = 'xfjc'
        reqdicts_before_pt = g.get("reqdicts_before_pt")
        reqdicts_before_pt.pop("zrdw", "")
        sql_format = self.apis_copy.copy()
        sql_format.update(reqdicts_before_pt)
        self.sql = sql.format(**sql_format)
        self.columns = columns

    def search(self):
        from utils.db_connection import fx_engine
        from utils.results2df import results2df
        results = fx_engine.execute(self.sql)
        data = results2df(results, self.columns)
        self.df = data

    def after_search(self):
        return
