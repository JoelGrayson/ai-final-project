from sklearn.svm import SVC

def classify(data, C=1.0):
    model=SVC(C=C, max_iter=3000)

    model.fit(data['X_train'], data['y_train'])
    # Probabilistic
    y_pred=model.predict(data['X_test'])
    return y_pred

