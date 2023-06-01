from load_data import load_data
from models.probabilistic import linear_regression
from models.probabilistic.evaluate import evaluate as probabilistic_evaluate
from models.binary import logistic_regression
from models.binary.evaluate import evaluate as binary_evaluate
from load_data import continuous2binary

data=continuous2binary(load_data())
y_pred=logistic_regression.classify(data)
binary_evaluate(data[5], y_pred)

