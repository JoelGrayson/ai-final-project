from load_data import load_data, load_split_data, continuous2binary
from maps.render_map import merge_fips, render_map
from models.continuous import linear_regression
from models.continuous.evaluate import evaluate as continuous_evaluate
from models.binary import logistic_regression
from models.binary.evaluate import evaluate as binary_evaluate

# Actual
## 2020 (continuous and binary)
X, y, fips=load_data('2020')
merged=merge_fips(fips, y)
render_map('2020-actual', merged)
merged=merge_fips(fips, y.round())
render_map('2020-actual-binary', merged)

## 2016
X, y, fips=load_data('2010-2012')
merged=merge_fips(fips, y)
render_map('2016-actual', merged)
merged=merge_fips(fips, y.round())
render_map('2016-actual-binary', merged)


# Predicted
## 2020
# data=continuous2binary(load_split_data(names['2020']))
# y_pred=logistic_regression.classify(data)
# binary_evaluate(data['y_test'], y_pred)
# render_map('2020-predicted', merge_fips(data['fips_test'], data['y_test']))
# render_map('2020-actual', merge_fips(data['fips_test'], data['y_test']))

## 2016

