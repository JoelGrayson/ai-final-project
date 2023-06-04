from sklearn.naive_bayes import BernoulliNB

# Uses Bayes' theorem. Naive because it assumes that the features are completely independent (no correlations).

def classify(data):
    model=BernoulliNB()
    model.fit(data['X_train'], data['y_train'])
    y_pred=model.predict(data['X_test'])
    return y_pred

