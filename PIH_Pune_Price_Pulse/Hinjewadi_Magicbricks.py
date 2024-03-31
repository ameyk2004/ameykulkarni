from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import os

# import xgboost as xgb
# import csv

from sklearn.metrics import accuracy_score, mean_squared_error, mean_absolute_percentage_error, f1_score,roc_auc_score, r2_score, mean_absolute_error
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the CSV file
csv_file_path = os.path.join(current_dir, 'Data', 'Rent Data', 'Hinjewadi_Nov5.csv')

dataset = pd.read_csv(csv_file_path)

rent = dataset.pop("Rent")

# test = pd.read_csv("test.csv")

X_train,X_test,y_train, y_test = train_test_split(dataset.drop(["Furnishing"],axis=1),rent,test_size=0.2,random_state=10)

hinjewadi_model = RandomForestRegressor(n_estimators=555, max_depth=6, random_state=10, max_features='sqrt', min_samples_split=5, min_samples_leaf=1, bootstrap=True)

hinjewadi_model.fit(dataset.drop(["Furnishing"],axis=1),rent)

# hinjewadi_model.fit(dataset.drop(["Unfurnished","Semi-Furnished","Furnishing"],axis=1),rent )
#
# imp = hinjewadi_model.feature_importances_
#
# for i in imp:
#     print(i)

import os

# Get the directory of the current Python script
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir, 'Data', 'Rent Data', 'test.csv')
test = pd.read_csv(csv_file_path)

# y_pred = hinjewadi_model.predict(X_test)
#
# print(hinjewadi_model.predict(test))

# print(mean_absolute_error(y_test,y_pred))
# print(mean_absolute_percentage_error(y_test,y_pred))
# # print(accuracy_score(y_test,y_pred))
# print(r2_score(y_test,y_pred))