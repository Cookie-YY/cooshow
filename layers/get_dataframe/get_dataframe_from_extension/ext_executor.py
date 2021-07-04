from flask import g


def ext_executor(ext):
    # before_search/search/after_search

    # before_search
    ext.before_search()  # search 前准备
    if ext.code != 200:
        return ext.code, ext.msg, {}
    if str(g.get("index_idx")) == g.get("debug", "").strip("sql"):
        return 999, "debug", getattr(ext, "sql")
    # search
    ext.search()  # search 查询 获得ext.db_results
    if ext.code != 200:
        return ext.code, ext.msg, {}
    g.db_results = ext.db_results
    # after_search
    ext.after_search()  # search 后聚合 获得ext.df
    if ext.code != 200:
        return ext.code, ext.msg, {}
    g.df = ext.df                                  # 保存db_results
    return ext.code, ext.msg, {"df": ext.df, "apis_copy": ext.apis_copy}
