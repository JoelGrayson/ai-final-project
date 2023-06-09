from sklearn.tree import DecisionTreeClassifier

def classify(data):
    model=DecisionTreeClassifier()
    model.fit(data['X_train'], data['y_train'], data['X_train'].total_votes)
    y_pred=model.predict(data['X_test'])
    return y_pred

