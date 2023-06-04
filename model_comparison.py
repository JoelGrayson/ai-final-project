from load_data import load_split_data, continuous2binary
from preprocessing.dist.names import names

from models.binary import decision_trees, gaussian_naive_bayes, knn, logistic_regression, random_forest, support_vector_classifier
from models.binary.evaluate import evaluate as binary_evaluate
from models.continuous import linear_regression, bernoulli_naive_bayes, support_vector_regression
from models.continuous.evaluate import evaluate as continuous_evaluate


print('# 2010-2012 Evaluation')
data=load_split_data(names['2010-2012'])

print('## Continuous')
print('\n### Linear Regression')
y_pred=linear_regression.classify(data)
continuous_evaluate(data['y_test'], y_pred)
print('\n### Support Vector Regression')
y_pred=support_vector_regression.classify(data, C=10)
continuous_evaluate(data['y_test'], y_pred)

print('## Binary')
data=continuous2binary(data)
print('\n### Logistic Regression')
y_pred=logistic_regression.classify(data, C=1e-8)
binary_evaluate(data['y_test'], y_pred)
print('\n### Decision Trees')
y_pred=decision_trees.classify(data)
binary_evaluate(data['y_test'], y_pred)
print('\n### Random Forest')
y_pred=random_forest.classify(data)
binary_evaluate(data['y_test'], y_pred)
print('\n### KNN')
y_pred=knn.classify(data)
binary_evaluate(data['y_test'], y_pred)
print('\n### Naive-Bayes')
y_pred=gaussian_naive_bayes.classify(data)
binary_evaluate(data['y_test'], y_pred)
print('\n### Bernoulli Naive Bayes')
y_pred=bernoulli_naive_bayes.classify(data)
binary_evaluate(data['y_test'], y_pred)
print('\n### Support Vector Classifier')
y_pred=support_vector_classifier.classify(data, C=100)
binary_evaluate(data['y_test'], y_pred)


print('\n\n# 2020 Evaluation')
data=load_split_data(names['2020'])

print('## Continuous')
print('\n### Linear Regression')
y_pred=linear_regression.classify(data)
continuous_evaluate(data['y_test'], y_pred)
print('\n### Support Vector Regression')
y_pred=support_vector_regression.classify(data, C=10)
continuous_evaluate(data['y_test'], y_pred)

print('## Binary')
data=continuous2binary(data)
print('\n### Logistic Regression')
y_pred=logistic_regression.classify(data, C=1e-6)
binary_evaluate(data['y_test'], y_pred)
print('\n### Decision Trees')
y_pred=decision_trees.classify(data)
binary_evaluate(data['y_test'], y_pred)
print('\n### Random Forest')
y_pred=random_forest.classify(data)
binary_evaluate(data['y_test'], y_pred)
print('\n### KNN')
y_pred=knn.classify(data)
binary_evaluate(data['y_test'], y_pred)
print('\n### Naive-Bayes')
y_pred=gaussian_naive_bayes.classify(data)
binary_evaluate(data['y_test'], y_pred)
print('\n### Bernoulli Naive Bayes')
y_pred=bernoulli_naive_bayes.classify(data)
binary_evaluate(data['y_test'], y_pred)
print('\n### Support Vector Classifier')
y_pred=support_vector_classifier.classify(data, C=100)
binary_evaluate(data['y_test'], y_pred)

