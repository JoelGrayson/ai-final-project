from sklearn.metrics import mean_squared_error, accuracy_score, precision_score, recall_score, log_loss
from math import sqrt

def evaluate(y_test, y_pred, include_precision_and_recall=True):
    print('MSE', mean_squared_error(y_test, y_pred))
    print('Mean Error', sqrt(mean_squared_error(y_test, y_pred)))
    print('Log Loss', log_loss(y_test, y_pred))
    print('Accuracy Score', accuracy_score(y_test, y_pred)) #see what percentage were accurate
    if include_precision_and_recall:
        print('Precision', precision_score(y_test, y_pred))
        print('Recall', recall_score(y_test, y_pred))

