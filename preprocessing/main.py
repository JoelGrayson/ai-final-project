import pandas as pd

pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 50)

for years in ['2020', '2010']:
    df=pd.read_csv(f'./src/{years}/ACS/data.csv', dtype=object)
    cols_to_drop=filter(lambda x: x[-1]=='A', df.columns)
    df=df.drop(columns=cols_to_drop)
    df.to_csv(f'./dist/{years}-ACS-data.csv', index=False)

