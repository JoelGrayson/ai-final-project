import pandas as pd

df=pd.read_csv('preprocessing/dist/2020-acs-and-votes.csv')
colnames=pd.read_csv('preprocessing/src/2020/ACS/column-metadata.csv')

features=df.columns
abbr2feature=colnames.set_index('Column Name', inplace=False)['Label'].to_dict() #index='Column Name')
for feature in features:
    if feature in abbr2feature:
        print(abbr2feature[feature])

