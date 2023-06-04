from sklearn.neural_network import MLPRegressor

def classify(data, hidden_layer_sizes, max_iter):
    nn=MLPRegressor(hidden_layer_sizes=hidden_layer_sizes, max_iter=max_iter)
    nn.fit(data['X_train'], data['y_train'])
    y_pred=nn.predict(data['X_test'])
    return y_pred

