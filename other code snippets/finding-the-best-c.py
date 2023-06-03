print('## Logistic Regression')
for pow in range(-10, 10, 1):
    C=10**pow
    y_pred=logistic_regression.classify(data, C)
    print('C', C)
    probabilistic_evaluate(data['y_test'], y_pred)

