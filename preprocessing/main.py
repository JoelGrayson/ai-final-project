import pandas as pd
from convert_fips_county_name import county_name_to_fips, fips_to_county_name

# pd.set_option('display.max_columns', 50)
# pd.set_option('display.max_rows', 50)


##### 2020 ACS and Voting Information #####
# ACS
acs=pd.read_csv(f'./src/2020/ACS/data.csv', dtype=object, na_values=['(X)', 'N', '-', 'median-', '100-', '**', '***', '*****', 'null'])

acs.drop([0], inplace=True) #drop first row, which is column metadata

acs.insert(0, 'FIPS', acs.GEO_ID.map(lambda x : int(x[9:]))) #identifier

cols_to_drop=filter(lambda x: (x[-1]!='E' or x=='NAME') and x!='FIPS', acs.columns) #keep only estimates, not margin of errors or notes. Keep FIPS
acs.drop(columns=cols_to_drop, inplace=True)

# remove all columns that have an missing data symbols specified in /preprocessing/src/2020/ACS/table-notes.html
acs.dropna(axis=1, inplace=True)
acs=acs.astype(float) #all numeric data

# Votes
"""
Ideal format
* id
* party float where 0 for Republican, 1 for Democrat
    Mnemonic: Republicans want less government and Democrats want more
    This number is just the ratio of Republican:Democratic votes, not including other parties
* % turnout (0-1)
"""
votes=pd.read_csv('./src/2020/votes/president_county_candidate.csv', dtype=object)


# Convert to fips
votes.insert(0, 'fips', (votes.county+', '+votes.state).map(county_name_to_fips), True)
votes.dropna(axis=0, inplace=True, how='any')
votes.fips=votes.fips.astype(int)


# Convert to proper Republican/Democrat ratios

# votes.rename(columns={ 'party': 'og_party' }, inplace=True)
# votes.drop(columns=['state', 'county', 'candidate'], inplace=True)
# votes.won=votes.won.astype(bool) # 'True' -> True



# # Merge
# merged=pd.merge(acs, votes, left_on='FIPS', right_on='', how='inner') #if a county is missing from either, it will be dropped


# # Export
# acs.to_csv(f'./dist/2020-ACS-data.csv', index=False)

