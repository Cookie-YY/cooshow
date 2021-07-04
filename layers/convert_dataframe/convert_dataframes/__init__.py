
"""
加入判断：生成数据还是图表
    实现方法就是把所有需要的数字，放到parse_data(app的那个入口函数)跑一遍
    图表: 在convert层做  graph=bar     show=data   |   pic   |   show=code
    show=data/pic/code              pic/code[需要指定type=num/bar/line/pie/map]  和 colors    BLUE
"""
from layers.convert_dataframe.convert_dataframes.convert_df import convert_df
from layers.convert_dataframe.convert_dataframes.convert_dfs import convert_dfs


def convert_dataframes(data_frame_list):
    if len(data_frame_list) == 1:  # 只对一个df做转换
        results = convert_df(data_frame_list[0])
        if results.get("code") != 200:
            return results.get("code"), results.get("msg"), {}
    else:                          # 对多个df做转换
        code, msg, results = convert_dfs(data_frame_list)
        if code != 200:
            return code, msg, {}
    return 200, "success", results
