
#### 
# capp off some features
# Create new binary vaiables
# convert the nominal features, JOB & REASON into usable form 
#   and remove them from the data table
# Distort assymetric distribution of the feature YOJ,For that we can apply log of YOJ 
#   but since some of them are 0, we will use log(YOJ+constant)
#   (df["YOJ"] = df["YOJ"].apply(lambda t : np.log(t+1))
# 
# The function returns a new dataframe
# ####
def feature_transform(dataframe):
    dataframe.loc[dataframe["CLAGE"] >= 600, "CLAGE"] = 600
    dataframe.loc[dataframe["VALUE"] >= 400000, "VALUE"] = 400000
    dataframe.loc[dataframe["MORTDUE"] >= 300000, "MORTDUE"] = 300000
    dataframe.loc[dataframe["DEBTINC"] >= 100, "DEBTINC"] = 100

    dataframe["B_DEROG"] = (dataframe["DEROG"] >= 1)*1
    dataframe["B_DELINQ"] = (dataframe["DELINQ"] >= 1)*1

    dataframe["JOB"].unique()

    dataframe["REASON_1"] = (dataframe["REASON"] == "HomeImp")*1
    dataframe["REASON_2"] = (dataframe["REASON"] != "HomeImp")*1
    dataframe["JOB_1"] = (dataframe["JOB"] == "Other")*1
    dataframe["JOB_2"] = (dataframe["JOB"] == "Office")*1
    dataframe["JOB_3"] = (dataframe["JOB"] == "Sales")*1
    dataframe["JOB_4"] = (dataframe["JOB"] == "Mgr")*1
    dataframe["JOB_5"] = (dataframe["JOB"] == "ProfExe")*1
    dataframe["JOB_6"] = (dataframe["JOB"] == "Self")*1
    dataframe.drop(["JOB", "REASON"], axis=1, inplace=True)

    return dataframe