from itertools import cycle

import pandas as pd

color_series_list = ""


def stack(d):
    result = {}
    for key, value in d.items():
        target = result  # 可变类型操作target实际上也会操作result
        for k in key[:-1]:  # 遍历到最后一项前 因为最后一项需要和value拼接
            target = target.setdefault(k, {})  # target会返回k键的值的一个引用，可以对引用进行添加形成嵌套
        target[key[-1]] = value  # 拼接value
    return result


def df_to_stacked_dict(df: pd.DataFrame) -> dict:
    d = df.to_dict(orient='index')
    res = stack(d)
    return res


# 2. 生成朴素嵌套字典: 没有颜色，没有限制，没有上级的求和
def multi_stack_produce(dataframe, s_columns=None):
    if not s_columns:  # 没有需要堆叠的列直接出去
        return
    df = dataframe
    df = df.set_index(s_columns)
    res = df_to_stacked_dict(df)
    return res


# 3. 上色+上级求和【递归主体】
def df_to_sunburst_chart(res, i):
    """
    思路:递归 先把所有最小粒度的按类别塞进{children:[]}中
    """
    global color_series_list
    sub_level_color_generator = sub_level_color(i, color_series_list)
    tmp = []
    total_copy = 0
    for k, v in res.items():
        total = 0
        if type(v) is int or type(v) is float:
            return v, v
        if type(v) is dict:
            v, tmp_total = df_to_sunburst_chart(v, i)
            total = total + tmp_total
            total_copy = total_copy + total
            if type(v) is int or type(v) is float:
                tmp_item = {'name': k, 'value': v, 'itemStyle': {'color': next(sub_level_color_generator)}}
            else:
                tmp_item = {'name': k, 'value': total, 'children': v,
                            'itemStyle': {'color': next(sub_level_color_generator)}}

            tmp.append(tmp_item)
    return tmp, total_copy


# 3. 上色+上级求和【颜色生成器】
def top_level_color(color_series_list):
    return cycle(k[0] for k in color_series_list), cycle(i for i in range(len(color_series_list)))


def sub_level_color(i, color_series_list):
    if i >= len(color_series_list):
        i = 0
    return cycle([color_series_list[i][1], color_series_list[i][2]])  # 用第2个和第3个颜色做间隔


# 3. 上色+上级求和
def df_to_colored_sunburst_chart(res):
    """
    :param res: dict 堆叠后的dict
    """
    global color_series_list
    top_level_color_generator, top_level_index_generator = top_level_color(color_series_list)

    tmp = []
    for k, v in res.items():
        total = 0
        if type(v) is int or type(v) is float:
            return v, v
        if type(v) is dict:
            v, tmp_total = df_to_sunburst_chart(v, next(top_level_index_generator))
            total = total + tmp_total
            if type(v) is int or type(v) is float:
                tmp_item = {'name': k, 'value': v}
            else:
                tmp_item = {'name': k, 'value': total, 'children': v,
                            'itemStyle': {'color': next(top_level_color_generator)}}
            tmp.append(tmp_item)
    return tmp


# 　转为堆叠字典前先用这个函数处理df
#  df:DataFrame s_columns:name按逗号分完的list sort_type:排序方式 limit_num:limit的数字
def stack_order_limit(df, s_columns, sort_type, limit_num):
    root_item = s_columns[0]
    sort_type = False if 'desc' in sort_type else True  # 升降序确定
    df_cols = df.columns.values
    value = [i for i in df_cols if i not in s_columns]
    df_copy = df.groupby(root_item, as_index=False)[[value[0]]].sum()

    sorted_df = df_copy.sort_values(by=value[0], axis=0, ascending=sort_type, inplace=False)
    limited_sorted_df = sorted_df.head(int(limit_num))
    filter_item = limited_sorted_df[root_item]
    df1 = df[df[root_item].isin(filter_item)]
    return df1


# 之后拿到limit+order层来做
def order(res, order_):
    is_reverse = True if "desc" in order_ else False  # 升降序确定
    res.sort(key=lambda t: t['value'], reverse=is_reverse)
    return res


# 之后拿到limit+order层来做
def limit(res, limit_):
    limit_ = limit_ if int(limit_) < len(res) else len(res)
    return res[:int(limit_)]


# 入口函数
def convert2embedding(dataframe):
    # 0. 拿到颜色
    from app import app
    global color_series_list
    color_series_list = app.config.get("COLOR_SERIES", {}).get("Embedding")
    if not color_series_list:
        return {"code": 400, "msg": "COLOR_SERIES must be assigned", "data": {}}
    # 1. 拿到df 和 所有需要嵌套的列
    df, s_cols_list = dataframe.get("df"), dataframe.get('name').split(',')
    df = stack_order_limit(df, s_cols_list, dataframe.get('order'),dataframe.get('limit'))
    # 2. 生成朴素嵌套字典: 没有颜色，没有限制，没有上级的求和
    res = multi_stack_produce(df, s_columns=s_cols_list)
    # 3. 上色+上级求和
    res = df_to_colored_sunburst_chart(res)  # 上色+算父亲的值
    # 4. 限制: order+limit
    if dataframe.get('order'):  # order
        res = order(res, dataframe.get('order'))
    if dataframe.get('limit'):  # limit
        res = limit(res, dataframe.get('limit'))
    return {"code": 200, "msg": "success", "data": res}
