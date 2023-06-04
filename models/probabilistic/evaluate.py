from sklearn.metrics import mean_squared_error, log_loss

def evaluate(y_test, y_pred):
    print('MSE', mean_squared_error(y_test, y_pred))
    print('Log Loss', log_loss(y_test, y_pred))

