import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, accuracy_score
from numpy import exp #allows applying exp to a vector

def sigmoid(x): #from stackoverflow.com/questions/3985619/how-to-calculate-a-logistic-sigmoid-function-in-python
  return 1/(1+exp(-x))

"""
Models:
* LinearRegression
* Decision trees
* Neural Networks
* Support Vector Regressor
"""

### <CONFIG>
validation_size=.10 #used to find C
train_size=.60
### </>

df=pd.read_csv('../preprocessing/dist/2020-acs-and-votes.csv')\
    .drop(columns=['fips'])\
    .sample(frac=1) #shuffle


# Manual split
num_rows=df.shape[0]
validation_index=round(num_rows*train_size)
train_index=validation_index+round(num_rows*validation_size)

val_data=df[:validation_index]
train_data=df[validation_index:train_index]
test_data=df[train_index:]

def get_xy(rows):
    X=rows.drop(columns=['party'])
    y=rows.party
    return X, y

X_val,     y_val=get_xy(val_data)
X_train, y_train=get_xy(train_data)
X_test,   y_test=get_xy(test_data)


model=LinearRegression() #classifier model
model.fit(X_train, y_train)
# Probabilistic
y_pred=sigmoid(model.predict(X_test))

# logistic function
print(mean_squared_error(y_test, y_pred))

