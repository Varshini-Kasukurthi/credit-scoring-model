import pandas as pandas 

####
# reading the csv data in a dataframe format
# Param to be passed here:
#   ~csv path(must be correct path and the file must be the correct format.)
# ####
def dataframe_head(csv_path):
    dataframe = pandas.read_csv(csv_path)
    dataframe.head()
    
    return [dataframe, dataframe]


