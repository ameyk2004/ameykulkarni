from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error, r2_score, mean_absolute_error
import pandas as pd
import numpy as np
import os

# Get the directory of the current Python script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the CSV file
csv_file_path = os.path.join(current_dir, 'Data', 'Rent Data', 'Baner_Final.csv')

dataset = pd.read_csv(csv_file_path)
rent = dataset.pop("Rent")

baner_model = RandomForestRegressor(n_estimators=511, max_depth=6, random_state=10, max_features='sqrt', min_samples_split=2, min_samples_leaf=1, bootstrap=True)

baner_model.fit(dataset.drop(["Furnishing"],axis = 1),rent)

test = pd.read_csv(csv_file_path)

# print(baner_model.predict(test))

# X_train,X_test,y_train, y_test = train_test_split(dataset.drop(["Furnishing"],axis=1),rent,test_size=0.2,random_state=10)
# # Define the Random Forest Regressor
# rf_regressor = RandomForestRegressor()
#
# # Define the parameter grid for randomized search
# param_dist = {
#     'n_estimators': [int(x) for x in np.linspace(start=400, stop=600, num=10)],
#     'max_features': ['log2','sqrt'],
#     'max_depth': [int(x) for x in np.linspace(5, 20, num=10)],
#     'min_samples_split': [2],
#     'min_samples_leaf': [1],
#     'bootstrap': [True]
# }
#
# # Create the RandomizedSearchCV object
# random_search = RandomizedSearchCV(
#     rf_regressor,
#     param_distributions=param_dist,
#     n_iter=100,  # Number of parameter settings that are sampled
#     cv=5,  # Number of cross-validation folds
#     scoring='neg_mean_absolute_error',  # Use mean squared error as the scoring metric
#     random_state=42,
#     verbose = 1
# )
#
# # Fit the RandomizedSearchCV object to the data
# random_search.fit(X_train, y_train)
#
# # Print the best parameters and best score
# print("Best Parameters: ", random_search.best_params_)
# print("Best Negative Mean Absolute Error: ", random_search.best_score_)
#
# # Make predictions on the test set using the best baner_model
# y_pred = random_search.best_estimator_.predict(X_test)
#
# # Evaluate the performance on the test set
# mse = mean_squared_error(y_test, y_pred)
# mae = mean_absolute_error(y_test,y_pred)
# mape = mean_absolute_percentage_error(y_test,y_pred)
# print("Mean Squared Error on Test Set: ", mse)
# print("Mean absolute error:",mae)
# print("MAPE:",mape)

#Fasos
#QUINTO
