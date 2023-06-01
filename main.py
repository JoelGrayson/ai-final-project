from load_data import load_data
import models.linear_probabilistic_classification as prob

data=load_data()
y_pred=prob.classify(data)
prob.evaluate(data[5], y_pred)
