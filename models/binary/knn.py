from sklearn.neighbors import KNeighborsClassifier

def classify(data):
    clf=KNeighborsClassifier(n_neighbors=20)
    clf.fit(data['X_train'], data['y_train'])
    y_pred=clf.predict(data['X_test'])
    return y_pred
