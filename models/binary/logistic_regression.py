from sklearn.linear_model import LogisticRegression

def classify(data):
    X_val, y_val, X_train, y_train, X_test, y_test=data

    model=LogisticRegression() #classifier model
    
    model.fit(X_train, y_train)
    # Probabilistic
    y_pred=model.predict(X_test)
    return y_pred


