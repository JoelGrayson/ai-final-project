from load_data import load_data
from models.probabilistic import linear_regression

data=load_data()
y_pred=linear_regression.classify(data)
linear_regression.evaluate(data[5], y_pred)
