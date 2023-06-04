from load_data import load_split_data, continuous2binary
from preprocessing.dist.names import names

from models.binary import decision_trees, knn, logistic_regression, naive_bayes, random_forest, support_vector_machines
from models.probabilistic import linear_regression
from models.probabilistic.evaluate import evaluate as probabilistic_evaluate
from models.binary.evaluate import evaluate as binary_evaluate


print('# 2010-2012 Evaluation')
data=continuous2binary(load_split_data(names['2010-2012']))
print('\n## Linear Regression')
y_pred=linear_regression.classify(data)
probabilistic_evaluate(data['y_test'], y_pred)
print('\n## Logistic Regression')
y_pred=logistic_regression.classify(data, C=1e-8)
binary_evaluate(data['y_test'], y_pred)
print('\n## Support Vector Machines')
y_pred=support_vector_machines.classify(data, C=100)
binary_evaluate(data['y_test'], y_pred)
print('\n## Decision Trees')
y_pred=decision_trees.classify(data)
binary_evaluate(data['y_test'], y_pred)
print('\n## Random Forest')
y_pred=random_forest.classify(data)
binary_evaluate(data['y_test'], y_pred)
print('\n## KNN')
y_pred=knn.classify(data)
binary_evaluate(data['y_test'], y_pred)
print('\n## Naive-Bayes')
y_pred=naive_bayes.classify(data)
binary_evaluate(data['y_test'], y_pred)

print('\n\n# 2020 Evaluation')
data=continuous2binary(load_split_data(names['2020']))
print('\n## Linear Regression')
y_pred=linear_regression.classify(data)
probabilistic_evaluate(data['y_test'], y_pred)
print('\n## Logistic Regression')
y_pred=logistic_regression.classify(data, C=1e-6)
binary_evaluate(data['y_test'], y_pred)
print('\n## Support Vector Machines')
y_pred=support_vector_machines.classify(data, C=100)
binary_evaluate(data['y_test'], y_pred)
print('\n## Decision Trees')
y_pred=decision_trees.classify(data)
binary_evaluate(data['y_test'], y_pred)
print('\n## Random Forest')
y_pred=random_forest.classify(data)
binary_evaluate(data['y_test'], y_pred)
print('\n## KNN')
y_pred=knn.classify(data)
binary_evaluate(data['y_test'], y_pred)
print('\n## Naive-Bayes')
y_pred=naive_bayes.classify(data)
binary_evaluate(data['y_test'], y_pred)

