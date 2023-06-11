import pandas as pd

colnames=pd.read_csv('preprocessing/src/2020/ACS/column-metadata.csv')
# Exported
abbr2feature=colnames.set_index('Column Name', inplace=False)['Label'].to_dict() #index='Column Name')
