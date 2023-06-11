import pandas as pd
from preprocessing.abbr2feature import abbr2feature

df=pd.read_csv('preprocessing/dist/2020-acs-and-votes.csv')

features=df.columns
for feature in features:
    if feature in abbr2feature:
        # # All
        # print(abbr2feature[feature])

        # Some Detail
        features=abbr2feature[feature].split('!!')
        print(f'{features[0]}\t\t{features[1]}')

