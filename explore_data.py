
def explore_data_information(dataframe):
    dataframe_size = dataframe.shape
    data_description = dataframe.describe()
    data_info = dataframe.info()
    dataframe_columns = dataframe.columns
    return [dataframe_size, data_description, data_info, dataframe_columns]




