from load_data import load_data
import pandas as pd
from maps.render_map import merge_fips, render_map

# Continuous
from sklearn.svm import SVR
from models.continuous.evaluate import evaluate as continuous_evaluate
# Binary
from sklearn.ensemble import RandomForestClassifier #decision trees as an ensemble
from models.binary.evaluate import evaluate as binary_evaluate



ten_X, ten_y, ten_fips=load_data('2010-2012')
twenty_X, twenty_y, twenty_fips=load_data('2020')
# make ten_X and twenty_X only have the same columns/features
twenty_X=twenty_X.drop(columns=['DP04_0047E', 'DP04_0072E', 'DP04_0088E', 'DP04_0100E', 'DP04_0107E', 'DP04_0132E', 'DP04_0142E', 'DP04_0143E', 'DP04_0036PE', 'DP04_0047PE', 'DP04_0072PE', 'DP04_0080PE', 'DP04_0090PE', 'DP04_0093PE', 'DP04_0102PE', 'DP04_0110PE', 'DP04_0117PE', 'DP04_0132PE', 'DP04_0133PE', 'DP04_0141PE', 'DP04_0142PE']) #not found in 2020, but found in 2010-2012
ten_X=ten_X[twenty_X.columns]

# Actual
## 2020 (continuous and binary)
render_map('2020-actual', merge_fips(twenty_fips, twenty_y))
render_map('2020-actual-binary', merge_fips(twenty_fips, twenty_y.round()))

## 2016
render_map('2016-actual', merge_fips(ten_fips, ten_y))
render_map('2016-actual-binary', merge_fips(ten_fips, ten_y.round()))


# Predicted
# Continuous
model=SVR(C=1, max_iter=5000) #found as the best C for this data
model.fit(ten_X, ten_y)
twenty_pred=pd.DataFrame({ 'party': model.predict(twenty_X) })['party']
continuous_evaluate(twenty_y, twenty_pred)

render_map('2020-predicted-continuous', merge_fips(twenty_fips, twenty_pred), True, True)


# Binary
model=RandomForestClassifier()
model.fit(ten_X, ten_y.round())
twenty_pred=pd.DataFrame({ 'party': model.predict(twenty_X) })['party']

binary_evaluate(twenty_y.round(), twenty_pred.round())

render_map('2020-predicted-binary', merge_fips(twenty_fips, twenty_pred.round()), True, True)

