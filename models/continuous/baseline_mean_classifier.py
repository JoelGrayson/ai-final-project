import pandas as pd
import numpy as np

def classify(data):
    mean_val=data['y_train'].mean()
    y_pred=np.ones(shape=data['y_test'].shape)*mean_val
    return pd.Series(y_pred)

