from load_data import load_split_data, continuous2binary
from preprocessing.dist.names import names

from models.binary import logistic_regression, support_vector_machines
from models.probabilistic import linear_regression
from models.probabilistic.evaluate import evaluate as probabilistic_evaluate
from models.binary.evaluate import evaluate as binary_evaluate


print('# 2010-2012 Evaluation')
data=continuous2binary(load_split_data(names['2010-2012']))
print('\n## Linear Regression')
y_pred=linear_regression.classify(data)
probabilistic_evaluate(data['y_test'], y_pred)
print('\n## Logistic Regression')
y_pred=logistic_regression.classify(data, C=1e-7)
binary_evaluate(data['y_test'], y_pred)
print('\n## Support Vector Machines')
y_pred=support_vector_machines.classify(data, C=100)
binary_evaluate(data['y_test'], y_pred)

print('\n\n# 2020 Evaluation')
data=continuous2binary(load_split_data(names['2020']))
print('\n## Linear Regression')
y_pred=linear_regression.classify(data)
probabilistic_evaluate(data['y_test'], y_pred)
print('\n## Logistic Regression')
y_pred=logistic_regression.classify(data, C=1e-8)
binary_evaluate(data['y_test'], y_pred)
print('\n## Support Vector Machines')
y_pred=support_vector_machines.classify(data, C=100)
binary_evaluate(data['y_test'], y_pred)
