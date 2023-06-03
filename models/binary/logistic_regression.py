from sklearn.linear_model import LogisticRegression

def classify(data, C=1):
    model=LogisticRegression(C=C, max_iter=3000) #classifier model
    
    model.fit(data['X_train'], data['y_train'])
    # Probabilistic
    y_pred=model.predict(data['X_test'])
    return y_pred


