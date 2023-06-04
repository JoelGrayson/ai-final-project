import pandas as pd
import numpy as np

def classify(data):
    mode_val=data['y_train'].mode()[0]
    y_pred=np.ones(shape=data['y_test'].shape)*mode_val
    return pd.Series(y_pred)

