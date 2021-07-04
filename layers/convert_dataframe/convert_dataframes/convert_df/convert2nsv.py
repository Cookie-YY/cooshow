import numpy as np
import pandas as pd


def convert2nsv(dataframe, groupid=0):
    df = dataframe["df"]
    name = dataframe.get("name")
    value = dataframe.get("value")
    stack = dataframe.get("stack")
    main_name = dataframe.get("main_name")
    if isinstance(df, np.int64) or isinstance(df, np.float) or isinstance(df, int) or isinstance(df, float):
        df = pd.DataFrame({value: [df]})
    data = df.to_dict(orient='records')

    # 处理name和value【可处理一个数和name value对的情况】
    if name:   # 处理name问题
        [i.update({"name": i.pop(name)}) for i in data]
    if value:  # 处理value问题
        [i.update({"value": i.pop(value)}) for i in data]

    # 处理main_name问题
    if main_name and not stack and not name:  # 有main_name但是没有stack，说明只有name
        data[0]["name"] = main_name

    if stack:  # 处理堆叠问题
        data_stack = []
        [i.update({stack: i.get(stack, i.get("name"))}) for i in data]

        stack_list = [i.get(stack) for i in data]  # 内层嵌套的内容
        from utils.get_unilist import get_unilist
        stack_uni = get_unilist(stack_list)  # 内层嵌套的内容去重
        main_list = [i.get("name") for i in data]  # 外层包裹的内容
        main_uni = get_unilist(main_list)  # 外层包裹的内容去重
        if name == stack:
            mapping = {f"value_g{groupid}_{1}": main_name}
        else:
            mapping = {f"value_g{groupid}_{stack_index + 1}": stack_uni[stack_index] for stack_index in range(len(stack_uni))}
        for main_one in main_uni:
            dic_one = {"name": main_one}
            for value_index, stack_one in enumerate(stack_uni):
                if name == stack:  # 是为了处理原来只是name&value，不堆叠，但是制定了extra_index，最终需要堆叠的情况，所以即使自己就是一维的键值对也需要改成嵌套形式
                    value_index = 0
                    stack_value = [tar_one.get("value") for tar_one in data if  # 核心：找到name是这个，stack是这个的value值
                                   tar_one.get("name") == main_one and tar_one.get(name) == stack_one]
                else:  # 正常情况
                    stack_value = [tar_one.get("value") for tar_one in data if  # 核心：找到name是这个，stack是这个的value值
                                   tar_one.get("name") == main_one and tar_one.get(stack) == stack_one]
                if stack_value:
                    dic_one[f"value_g{groupid}_{value_index + 1}"] = stack_value[0]

            data_stack.append(dic_one)
        return {"code": 200, "msg": "success", "map": mapping, "data": data_stack}
    return {"code": 200, "msg": "success", "data": data}
