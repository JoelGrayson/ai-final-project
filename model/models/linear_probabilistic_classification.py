
from sklearn.linear_model import LinearRegression
from numpy import exp #allows applying exp to a vector

def sigmoid(x): #from stackoverflow.com/questions/3985619/how-to-calculate-a-logistic-sigmoid-function-in-python
    return 1/(1+exp(-x))


def linear_probabilistic_classification(X_val, y_val, X_train, y_train, X_test, y_test):
    model=LinearRegression() #classifier model
    model.fit(X_train, y_train)
    # Probabilistic
    y_pred=sigmoid(model.predict(X_test))

