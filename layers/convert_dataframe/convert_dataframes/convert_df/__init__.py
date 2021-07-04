from layers.convert_dataframe.convert_dataframes.convert_df.convert2embedding import convert2embedding
from layers.convert_dataframe.convert_dataframes.convert_df.convert2graph import convert2graph
from layers.convert_dataframe.convert_dataframes.convert_df.convert2nsv import convert2nsv
from layers.convert_dataframe.convert_dataframes.convert_df.convert2table import convert2table


def convert_df(dataframe, groupid=0):
    # table格式
    if "," in dataframe.get("name", "") and "dq_after" in dataframe.get("transformer", ""):
        results = convert2table()

    # embedding格式
    elif "," in dataframe.get("name", ""):
        results = convert2embedding(dataframe)

    # graph格式(js code)
    elif "graph_type" in dataframe:
        results = convert2graph()

    # name/stack/value 格式
    else:
        results = convert2nsv(dataframe, groupid)
    return results
