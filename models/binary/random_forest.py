from sklearn.ensemble import RandomForestClassifier #decision trees as an ensemble

def classify(data):
    model=RandomForestClassifier()
    model.fit(data['X_train'], data['y_train'], data['X_train'].total_votes)
    y_pred=model.predict(data['X_test'])
    return y_pred

