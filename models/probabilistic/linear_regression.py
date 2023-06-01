from sklearn.linear_model import LinearRegression
from numpy import exp #allows applying exp to a vector

def sigmoid(x): #from stackoverflow.com/questions/3985619/how-to-calculate-a-logistic-sigmoid-function-in-python
    return 1/(1+exp(-x))

def classify(data):
    X_val, y_val, X_train, y_train, X_test, y_test=data

    model=LinearRegression() #classifier model
    model.fit(X_train, y_train)
    # Probabilistic
    y_pred=model.predict(X_test)
    y_pred=sigmoid(y_pred) #keep it between 0-1
    return y_pred


