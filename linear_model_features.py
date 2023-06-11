from sklearn.linear_model import LinearRegression
from load_data import load_data, load_split_data
from preprocessing.abbr2feature import abbr2feature

data=load_split_data('2020')

model=LinearRegression() #classifier model
model.fit(data['X_train'], data['y_train'], data['X_train'].total_votes)

print('Intercept', model.intercept_) #starting point baseline

for i, abbr_colname in enumerate(data['X_train'].columns):
    if abbr_colname=='total_votes':
        continue
    colname=abbr2feature[abbr_colname]

    show_colname=' > '.join(colname.split('!!')[1:]) #otherwise, TMI

    print(f'{model.coef_[i]:>14.6f}   {show_colname} ({abbr_colname})')

