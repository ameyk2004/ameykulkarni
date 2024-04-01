import numpy as np
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
import pandas as pd
import os

# Load the dataset (you can replace this with your own dataset)
import os

# Get the directory of the current Python script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the CSV file
csv_file_path = os.path.join(current_dir, 'Data', 'Rent Data', 'kharadi_final.csv')
dataset = pd.read_csv(csv_file_path)

rent = dataset.pop("Rent")

# X_train,X_test,y_train, y_test = train_test_split(dataset.drop(["Furnishing"],axis=1),rent,test_size=0.2,random_state=10)

kharadi_model = RandomForestRegressor(n_estimators=400, max_depth=16, random_state=10, max_features='sqrt', min_samples_split=4, min_samples_leaf=2, bootstrap=True)

kharadi_model.fit(dataset.drop(["Furnishing"],axis = 1),rent)

# Get the directory of the current Python script
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir, 'Data', 'Rent Data', 'test.csv')
test = pd.read_csv(csv_file_path )

# print(kharadi_model.predict(test))