from scipy.sparse import data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
import error_visualization
import numpy
from matplotlib import pyplot as plot
import variable_manipulation


def data_split(dataframe):
    # wiping away the features; BAD,JOB,REASON from the inumpyut features set
    # since its common, its nice to do away with them.
    # x_feature_sets = dataframe.drop(columns=["BAD", "JOB", "REASON"]) ##can be used without correlation
    # y_feature_sets = dataframe["BAD"] ##can be used without correlation
    correlated_dataframe = variable_manipulation.feature_selection(dataframe)[0]
    feature_sets_selected = variable_manipulation.feature_selection(dataframe)[1]
    
    x_feature_sets = correlated_dataframe[feature_sets_selected] #LOAN
    y_feature_sets = correlated_dataframe['BAD']

    # Spliting the data into test and train sets
    x_training, x_test, y_training, y_test = train_test_split(x_feature_sets, y_feature_sets, test_size=0.33, random_state=1)
    return [x_training, x_test, y_training, y_test]


def threshold_change(dataframe):
    x_train = data_split(dataframe)[0]
    x_test = data_split(dataframe)[1]
    y_train = data_split(dataframe)[2]
    y_test = data_split(dataframe)[3]

    logistic_regression = LogisticRegression()

    logistic_regression.fit(x_train, y_train)
    y_pred_proba = logistic_regression.predict_proba(x_test)

    # The output of a Logistic regression model is a probability. We can select a threshold value. 
    # If the probability is greater than this threshold value, 
    # the event is predicted to happen otherwise it is predicted not to happen. 
    # A confusion or classification matrix compares the actual outcomes to the predicted outcomes(Predicted array)
    thresholds = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

    plot.figure(figsize=(5, 5))

    j = 1
    for i in thresholds:
        y_test_predictions_high_recall = y_pred_proba[:, 1] >= i

        plot.subplot(3, 3, j)
        j += 1

        # Compute confusion matrix
        cnf_matrix = confusion_matrix(y_test, y_test_predictions_high_recall)
        numpy.set_printoptions(precision=2)

        rec1 = recall_score(y_test, y_test_predictions_high_recall)
        acc = 1.0*(cnf_matrix[0, 0]+cnf_matrix[1, 1])/(cnf_matrix[0, 0]+cnf_matrix[1, 0]+cnf_matrix[1, 1]+cnf_matrix[0, 1])
        print("Recall metric in the testing dataset: ", rec1)
        print("Accuracy score for the testing dataset: ", acc)
       
        # Plot non-normalized confusion matrix
        class_names = [0, 1]
        error_visualization.error_visualize(cnf_matrix, classes=class_names, title='Threshold >= %s' % i)
        
    print("")   
    plot.show()

def set_up_model(dataframe):
    x_training = data_split(dataframe)[0]
    x_test = data_split(dataframe)[1]
    y_training = data_split(dataframe)[2]
    y_test = data_split(dataframe)[3]

    logreg_basic = LogisticRegression()

    # Training the basic logistic regression model with training set
    # fit() does the training.
    logreg_basic.fit(x_training, y_training)

    
    # Coef. A regression coefficient describes the size and direction of the 
    # relationship between a predictor and the response variable. 
    # Coefficients are the numbers by which the values of the term are multiplied in a 
    # regression equation.
    # Revise on the Logistic regression equations.
    # https://en.wikipedia.org/wiki/Logistic_regression
    # Printing the coefficients
    print("intercept ")
    print(logreg_basic.intercept_)
    print("")
    print("coefficients ")
    print(logreg_basic.coef_)

    # Predicting the output of the test cases using the algorithm created above
    y_predictions = logreg_basic.predict(x_test)

    print(y_predictions)

    # Validating the algorithm using various Performance metrics 
    print("")
    a1 = accuracy_score(y_test, y_predictions)
    f1 = f1_score(y_test, y_predictions, average="macro")
    p1 = precision_score(y_test, y_predictions, average="macro")
    r1 = recall_score(y_test, y_predictions, average="macro")

    print("accuracy score : ", a1)
    print("f1 score : ", f1)
    print("precision score : ", p1)
    print("recall score : ", r1)

    return [logreg_basic, y_predictions]

def apply_error_matrix_algorithm(dataframe):
    y_test = data_split(dataframe)[3]
    y_predictions = set_up_model(dataframe)[1]

    error_matrix = confusion_matrix(y_test, y_predictions)
    numpy.set_printoptions(precision=2) #Test 

    # Plot non-normalized confusion matrix
    # classes can be said to be the dataframe variables
    plot.figure()
    error_visualization.error_visualize(error_matrix, classes=["BAD", "GOOD"], title='Confusion matrix - Logistic Regression Algorithm')

    plot.show()


