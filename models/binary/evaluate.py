from sklearn.metrics import mean_squared_error, accuracy_score, precision_score, recall_score
# accuracy_score - see what percentage were accurate

def evaluate(y_test, y_pred):
    print('MSE', mean_squared_error(y_test, y_pred))
    print('Accuracy Score', accuracy_score(y_test, y_pred))
    print('Precision', precision_score(y_test, y_pred))
    print('Recall', recall_score(y_test, y_pred))

