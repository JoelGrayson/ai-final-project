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
from load_data import load_data
from models.continuous.evaluate import evaluate as continuous_evaluate
from maps.render_map import merge_fips, render_map
import pandas as pd

from sklearn.svm import SVR
ten_X, ten_y, ten_fips=load_data('2010-2012')
twenty_X, twenty_y, twenty_fips=load_data('2020')

# make ten_X and twenty_X only have the same columns/features
twenty_X=twenty_X.drop(columns=['DP04_0047E', 'DP04_0072E', 'DP04_0088E', 'DP04_0100E', 'DP04_0107E', 'DP04_0132E', 'DP04_0142E', 'DP04_0143E', 'DP04_0036PE', 'DP04_0047PE', 'DP04_0072PE', 'DP04_0080PE', 'DP04_0090PE', 'DP04_0093PE', 'DP04_0102PE', 'DP04_0110PE', 'DP04_0117PE', 'DP04_0132PE', 'DP04_0133PE', 'DP04_0141PE', 'DP04_0142PE']) #not found in 2020, but found in 2010-2012
ten_X=ten_X[twenty_X.columns]


model=SVR(C=10, max_iter=3000)
model.fit(ten_X, ten_y)
# Continuous
twenty_pred=pd.DataFrame({ 'party': model.predict(twenty_X) })['party']

render_map('2020-predicted-from-2010-2012', merge_fips(twenty_fips, twenty_pred), True, True)

continuous_evaluate(twenty_y, twenty_pred)



