from sklearn.metrics import mean_squared_error

def evaluate(y_test, y_pred):
    print('MSE', mean_squared_error(y_test, y_pred))

