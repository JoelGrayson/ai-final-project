from load_data import load_data, load_raw_data
from load_data import continuous2binary

from models.probabilistic import linear_regression
from models.probabilistic.evaluate import evaluate as probabilistic_evaluate
from models.binary import logistic_regression
from models.binary.evaluate import evaluate as binary_evaluate

from maps.render_map import merge_fips, render_map


# data=continuous2binary(load_data())
# y_pred=logistic_regression.classify(data)
# binary_evaluate(data['y_test'], y_pred)
# render_map('2020-predicted', merge_fips(data['fips_test'], data['y_test']))
# render_map('2020-actual', merge_fips(data['fips_test'], data['y_test']))

# 2020 actual binary
X, y, fips=load_raw_data()
merged=merge_fips(fips, y.round())
render_map('2020-actual', merged)

# 2020 actual continuous
# data=load_raw_data()


