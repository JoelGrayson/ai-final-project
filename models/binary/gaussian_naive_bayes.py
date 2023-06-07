from sklearn.naive_bayes import GaussianNB

# Uses Bayes' theorem. Naive because it assumes that the features are completely independent (no correlations).

def classify(data):
    model=GaussianNB()
    model.fit(data['X_train'], data['y_train'], data['X_train'].total_votes)
    y_pred=model.predict(data['X_test'])
    return y_pred

