import numpy as np
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
import pandas as pd
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir, 'Data', 'Purchase Data', 'Wagholi_buy.csv')
dataset = pd.read_csv(csv_file_path)

rent = dataset.pop("Price")

wagholi_purchase = RandomForestRegressor(n_estimators=375, max_depth=46, random_state=10, max_features='log2', min_samples_split=4, min_samples_leaf=1, bootstrap=True)

wagholi_purchase.fit(dataset,rent)
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir, 'Data', 'Purchase Data', 'test_buy.csv')
test = pd.read_csv(csv_file_path)

# print(wagholi_purchase.predict(test))

# dataset = pd.read_csv("Wagholi_sale_final.csv")
#
# rent = dataset.pop("Price")
#
# X_train,X_test,y_train, y_test = train_test_split(dataset,rent,test_size=0.2,random_state=10)
#
# rf_regressor = RandomForestRegressor()
#
# param_dist = {
#     'n_estimators': [int(x) for x in np.linspace(start=300, stop=600, num=5)],
#     'max_features': ['log2'],
#     'max_depth': [int(x) for x in np.linspace(5, 60, num=5)],
#     'min_samples_split': [4],
#     'min_samples_leaf': [1],
#     'bootstrap': [True]
# }
#
# random_search = RandomizedSearchCV(
#     rf_regressor,
#     param_distributions=param_dist,
#     n_iter=100,
#     cv=5,
#     scoring='neg_mean_absolute_error',
#     random_state=42,
#     verbose = 2
# )
#
# random_search.fit(X_train, y_train)
#
# print("Best Parameters: ", random_search.best_params_)
# print("Best Negative Mean Absolute Error: ", random_search.best_score_)
#
# y_pred = random_search.best_estimator_.predict(X_test)
#
# mse = mean_squared_error(y_test, y_pred)
# mae = mean_absolute_error(y_test,y_pred)
# mape = mean_absolute_percentage_error(y_test,y_pred)
# print("Mean Squared Error on Test Set: ", mse)
# print("Mean absolute error:",mae)
# print("MAPE:",mape)