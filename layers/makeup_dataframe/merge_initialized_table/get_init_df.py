import pandas as pd
import itertools


def get_init_df(re_list, no_re_list, re_col, no_re_col):
    # 直接解包re_list,no_re_list就可以处理完有关系的列
    # 对于no_re_col中的每一项 需要查出它的可能取值范围
    product_list = list(itertools.product(*re_list, *no_re_list))
    # print(product_list)
    processed_product_list = unzip_tool(product_list)
    # print(processed_product_list)
    dataframe = pd.DataFrame(processed_product_list, columns=re_col + no_re_col)
    # print(dataframe)
    return dataframe


def unzip_tool(product_list):
    # [["北京市", "海淀区"], "性别"]  ==> ["北京市", "海淀区", "性别"]
    # 转化为str，直接字符串把括号去了，然后用逗号分割返回
    product_str = str(product_list)
    processed_product_str = '[' + product_str.replace('[', '').replace(']', '') + ']'
    processed_product_list = eval(processed_product_str)
    return processed_product_list
