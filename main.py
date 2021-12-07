import data_preparation 
import explore_data
import variable_distribution
import variable_manipulation
import feature_transformation
import model

#we use pandas in this case.
original_csv_path = "public/csv/hmeq.csv"

# print dataframe
dataframe = data_preparation.dataframe_head(original_csv_path)[0]
print(dataframe)

# Data Visuals
data_visuals = explore_data.explore_data_information(dataframe) 
for data_visual in data_visuals:
    print(data_visual)

# Variable value count
variable_count_array = variable_distribution.variable_distribution_count(dataframe)
for variable_count in variable_count_array:
    print('Ready for variable count!')
    print(variable_count) 

# # manipulate dataframe by checking some conditions
imputed_dataframe = variable_manipulation.replace_values_and_print_final_dataframe_look(dataframe)
print(imputed_dataframe)

# # data info transformation
transformed_dataframe = feature_transformation.feature_transform(imputed_dataframe)
print(transformed_dataframe)

# ####
# #  model setup starts here
# #  Checking the perfomance of our algorithim.
# #  Data split is also done here!
# #  Uncomment this method call after running it. 
# #  To test and compare
# #    on the model performance, Then run the model after threshold changes.
# # ####
# model.apply_error_matrix_algorithm(transformed_dataframe)

####
# After Threshold change
# Compare the model in this case.
#   The values of recall and accuracy vary with the threshold selected.
#   Wise for the user to choose and decide on the threshold to use 
#       -this is basing your model on the accuracy performaces
#   By default, Threshold is always 0.5 
#       Advisable to use 0.5 as threshold for most cases(general cases)
# ####
model.threshold_change(transformed_dataframe)

