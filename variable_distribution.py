
import matplotlib.pyplot as plot

def variable_distribution_count(dataframe):
    variables_array = ['BAD', 'REASON', 'JOB', 'DEROG',
                       'DELINQ', 'NINQ']
    variable_count_array = []
    for variable in variables_array:
        value_count = dataframe[variable].value_counts()

        variable_count_array.append(value_count)

    return variable_count_array

def variable_diagramatic_visualize(dataframe):
    variables_array = ['BAD', 'LOAN', 'MORTDUE', 'VALUE', 'REASON', 'JOB', 'YOJ', 'DEROG',
                       'DELINQ', 'CLAGE', 'NINQ', 'CLNO', 'DEBTINC']
    for variable in variables_array:
        if variable == 'BAD':
            dataframe['BAD'].value_counts().plot(kind="barh") 
        if variable == 'LOAN':
            dataframe["LOAN"].plot.hist(bins=20, figsize=(15, 7.5)) 
        if variable == 'DEBTINC':
            dataframe["DEBTINC"].plot.hist(bins=20, figsize=(15, 5))
        if variable == 'CLAGE':
            dataframe["CLAGE"].plot.hist(bins=20, figsize=(15, 7.5))
        if variable == 'CLNO':
            dataframe["CLNO"].plot.hist(bins=20, figsize=(15, 5))
        if variable == 'VALUE':
            dataframe["VALUE"].plot.hist(bins=80, figsize=(15, 7.5))
        if variable == 'MORTDUE':
            dataframe["MORTDUE"].plot.hist(bins=40, figsize=(15, 7.5))
        if variable == 'YOJ':
            dataframe["YOJ"].plot.hist(bins=20, figsize=(15, 7.5))
