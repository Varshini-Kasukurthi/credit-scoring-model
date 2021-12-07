
""""
Takes care of null values.
if any null value ? do the magic : return the initial/original dataframe
"""""
def replace_values_and_print_final_dataframe_look(dataframe):
    # 'NaN'
    if dataframe.isnull().values.any():
        dataframe["REASON"].fillna(value="DebtCon", inplace=True)
        dataframe["JOB"].fillna(value="Other", inplace=True)
        dataframe["DEROG"].fillna(value=0, inplace=True)
        dataframe["DELINQ"].fillna(value=0, inplace=True)

        dataframe.fillna(value=dataframe.mean(), inplace=True)
    
        return dataframe
    else:
        return dataframe    


""""
Takes care of feature selection
Does more on making improvement on our model.
Do some corellation with logistic regression algorithm
We shall use Pearson correlation factor pearson in this case.
"""""
def feature_selection(dataframe):
    dataframe.corr(method='pearson') 
    features_sets = ["LOAN", "DEROG", "DELINQ"]
    return [dataframe, features_sets]
