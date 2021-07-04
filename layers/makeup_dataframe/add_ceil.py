def add_ceil(dataframe):
    df = dataframe["df"]
    ceil = dataframe.get("ceil")
    ceil_value = dataframe.get("ceil_value")
    value = dataframe.get("value")
    df[value] = df[value].apply(lambda x: ceil_value if x >= ceil else x)
    return df
