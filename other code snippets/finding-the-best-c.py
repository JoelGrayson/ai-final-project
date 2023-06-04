print('Evaluating C')
for pow in range(-10, 10, 1):
    C=10**pow
    print('C', C)
    support_vector_machines.evaluate_hyperparameters(data, C)


exit(65) #stop the rest of the code from running

