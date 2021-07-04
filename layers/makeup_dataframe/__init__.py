import pandas as pd

from layers.makeup_dataframe.add_ceil import add_ceil
from layers.makeup_dataframe.merge_initialized_table import merge_initialized_table
from layers.makeup_dataframe.order_limit import order_limit, name_stack_limit
from layers.makeup_dataframe.add_unit import add_unit
from flask import g


def makeup_dataframe(dataframe):
    """
    0. 时间格式化
    1. 排  序 / 补  零
    2. order / limit
    3. value 的单位
    4. 设置数值上限
    """

    # for dataframe in dataframe_list:
    if isinstance(dataframe["df"], pd.DataFrame):
        name = dataframe.get("name")
        stack = dataframe.get("stack")
        value = dataframe.get("value")

        # 时间格式化
        from utils.time_format import df_formated_time
        df = df_formated_time(dataframe["df"], time_format=dataframe.get("time_format"))
        dataframe["df"] = df

        # 排序补零：
        from app import app
        if dataframe.get("full") == "true" \
                and dataframe.get("name", "") not in app.config.get("DISABLE_FULL_WHEN_NAME", []) \
                and dataframe.get("value", "") not in app.config.get("DISABLE_FULL_WHEN_VALUE", []):
            code, msg, df = merge_initialized_table(dataframe)  # 融合数据表：加 处理了day的初始化问题
            if code != 200:
                return 400, msg, {}
            dataframe["df"] = df

        # 重新排序+limit
        if (dataframe.get("order") or dataframe.get("limit")) and "," not in dataframe.get("name"):
            df = order_limit(dataframe)
            dataframe["df"] = df

        # name_limit
        if dataframe.get("name_limit"):
            df = name_stack_limit(dataframe, "name_limit", name, value)
            dataframe["df"] = df

        # stack_limit
        if dataframe.get("stack_limit"):
            df = name_stack_limit(dataframe, "stack_limit", stack, value)
            dataframe["df"] = df

        # 添加单位
        if dataframe.get("unit"):
            df = add_unit(dataframe)
            dataframe["df"] = df

        # 设置上限
        if dataframe.get("ceil"):
            df = add_ceil(dataframe)
            dataframe["df"] = df

        # 删掉None数据[此时如果还有None]
        df = dataframe.get("df")
        if isinstance(df, pd.DataFrame) and df.shape[0]==1 and df.iloc[0,0]=="None":
            dataframe["df"] = pd.DataFrame()

    return 200, "success", dataframe


if __name__ == '__main__':
    pass
