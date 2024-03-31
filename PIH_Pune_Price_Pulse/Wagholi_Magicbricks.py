import numpy as np
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
import pandas as pd
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir, 'Data', 'Rent Data', 'wagholi_final.csv')
dataset = pd.read_csv(csv_file_path)

rent = dataset.pop("Rent")

wagholi_model = RandomForestRegressor(n_estimators=255, max_depth=25, random_state=10, max_features='log2', min_samples_split=4, min_samples_leaf=1, bootstrap=True)

wagholi_model.fit(dataset,rent)
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir, 'Data', 'Rent Data', 'test.csv')
test = pd.read_csv(csv_file_path)

# print(wagholi_model.predict(test))