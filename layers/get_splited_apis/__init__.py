def get_splited_apis(realm, index, request_args):
    """
    输入：查询参数
    返回：api列表
    """
    ",分隔多个group"
    ";分隔一个group下多个多个条件"
    ":分隔操作符和操作的具体内容"
    "@分隔执行操作的主体和操作的动作"
    "extra_index=lx@to:xfxs;index@to:xfj_zb,year@math:-1"
    extra_index = request_args.pop("extra_index", "")
    base_dict = {"realm": realm, "index": index}

    # 这里的main_name兼容三个，当main_name不写默认每一个stack都可以找到自己的main
    # 1. main_name = 信访件次,件次占比,信访人次,人次占比
    # 2. main_name = 总数,
    # 3. main_name = ,1          1用于占位，逗号前的指标自己有name，逗号后的指标自己也有name，但不能再不写了
    main_name = request_args.pop("main_name", ",,").split(",")
    # 初始化，并放入第一个api
    base_dict.update(request_args)
    request_args_set = [base_dict]
    # 得到多个group：extra_grouplist: [["lx:to-xfxs;index:to-xfj_zb"], ["year:math_+1"]]

    if extra_index:
        # extra_index里面可能有day@to:[now-50,now]逗号   【可以先把中括号的逗号替换掉，最后再替换回来】
        # http://127.0.0.1:3389/api/xf/?table=xf_xfj_cd_xj_xfjc&name=day&stack=day&day=[now-50,now]&extra_index=transformer@to:predict(7d+p=1+d=1+q=0+realdata_show=50d);day@to:[now-200,now]&Cqh=广东省
        num_comma = extra_index.count(",")
        should_minus = extra_index.count("[")
        extra_grouplist = [i for i in extra_index.split(",", num_comma - should_minus)]
        # 开始遍历获得所有的额外条件
        for group in extra_grouplist:  # group = ["lx@to:xfxs;index@to:xfj_zb"]
            # 每个group要得到一个request_args字典
            request_args_for_each_group = base_dict.copy()  # 基础的参数
            # main_name = "总数"
            for condition in group.split(";"):  # condition = "lx:to-xfxs"
                'condition = "lx@to:xfxs"'
                # condition = condition.replace("=", "@to:")   # 语法糖: 如果写了=就是@to:
                target, operation = condition.split("@", 1)
                operation = operation if ":" in operation else operation+":"
                operator, op_content = operation.split(":", 1)
                # target:     表名：busin/index/timetype/qh/lx
                #                  name/value
                #             字段：year/month
                # operator：   增/改[目标-用于修改表名]：to
                #              增/改[过程-用于修改字段]：math
                #              删：drop
                # op_content:  如果drop：          op_content为空
                #              如果to且target是表名：op_content是要更改的内容
                #              如果to且target是字段：op_content是-1之类的操作
                if operator == "to":      # lx@to:xfxs
                    request_args_for_each_group[target] = op_content
                elif operator == "drop":  # lx@drop
                    request_args_for_each_group.pop(target, "")
                elif operator == "math":  # year@math:-1
                    from utils.parse_compute import parse_compute
                    code, msg, result = parse_compute(f"{request_args_for_each_group[target]}{op_content}")
                    if code != 200:
                        return code, msg, {}
                    request_args_for_each_group[target] = result
                else:
                    return 400, "unsupported operator", {}
            request_args_set.append(request_args_for_each_group)
        return 200, "success", dict(zip(main_name, request_args_set))
    return 200, "success", {main_name[0]: {**request_args, **base_dict}}


if __name__ == '__main__':
    """
    ?timetype=cy&lx=xfxs_cfxfbz&name=cfxfbz&value=xfjc&stack=cfxfbz&extra_index=value@to:zb,index@to:xfrc_zb;value@to:xfrc,index@to:xfrc_zb;value@to:zb&main_name=信访件次,件次占比,信访人次,人次占比&xfxs=drop&year=2020
"""
    request_args = {"timetype": "cy",
                    "lx": "xfxs_cfxfbz",
                    "name": "cfxfbz",
                    "value": "xfjc",
                    "stack": "cfxfbz",
                    "extra_index": "value@to:zb,index@to:xfrc_zb;value@to:xfrc,index@to:xfrc_zb;value@to:zb;year@math:-1",
                    "main_name": "信访件次,件次占比,信访人次,人次占比",
                    "xfxs": "drop",
                    "year": "2020"}
    code, msg, test = get_splited_apis("xf", "xfj", request_args)
    print(code)
    print(msg)
    for k, v in test.items():
        print(k, v)
