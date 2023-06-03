import pandas as pd

def preprocess_acs(filepath):
    acs=pd.read_csv(filepath, dtype=object, na_values=['(X)', 'N', '-', 'median-', '100-', '**', '***', '*****', 'null'])

    acs.drop([0], inplace=True) #drop first row, which is column metadata

    acs.insert(0, 'fips', acs.GEO_ID.map(lambda x : x[9:])) #identifier

    cols_to_drop=filter(lambda x: (x[-1]!='E' or x=='NAME') and x!='fips', acs.columns) #keep only estimates, not margin of errors or notes. Keep fips
    acs.drop(columns=cols_to_drop, inplace=True)

    # remove all columns that have an missing data symbols specified in /preprocessing/src/2020/ACS/table-notes.html
    acs.dropna(axis=1, inplace=True)
    for column in acs.columns:
        if column!='fips': #all numeric data except fips, which is a string
            acs[column]=acs[column].astype(float)

    return acs

