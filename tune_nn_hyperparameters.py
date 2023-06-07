from load_data import load_split_data, continuous2binary

from sklearn.model_selection import cross_val_score
from models.continuous import neural_network
from models.continuous.evaluate import evaluate as continuous_evaluate

# Scientific notation -> normal
import pandas as pd
pd.set_option('display.float_format', str)


data=load_split_data('2010-2012')
y_pred=neural_network.classify(data, hidden_layer_sizes=(20, 10), max_iter=3000)
continuous_evaluate(data['y_test'], y_pred)

