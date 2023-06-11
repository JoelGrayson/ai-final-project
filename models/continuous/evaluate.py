from sklearn.metrics import mean_squared_error
from math import sqrt

def evaluate(y_test, y_pred):
    print('MSE', mean_squared_error(y_test, y_pred))
    print('Mean Error', sqrt(mean_squared_error(y_test, y_pred)))

