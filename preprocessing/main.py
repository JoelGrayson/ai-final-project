import pandas as pd

# pd.set_option('display.max_columns', 50)
# pd.set_option('display.max_rows', 50)

##### 2020 ACS and Voting Information #####
# ACS
acs=pd.read_csv(f'./src/2020/ACS/data.csv', dtype=object)
acs=acs.drop([0]) #drop first row
# acs=acs.drop(columns=['NAME']) #drop first row
# acs=acs.astype('int32') #convert all columns to int32
cols_to_drop=filter(lambda x: x[-1]!='E', acs.columns) #keep only estimates, not margin of errors or notes
acs=acs.drop(columns=cols_to_drop)
acs=acs.rename(columns={'NAME': 'id'}) #{county name}, {state name} in place of FIPS unique county identifier


# Votes
"""
Ideal format
* id
* party float where 0 for republican, 1 for democrat
    Mnemonic: republicans want less government and democrats want more
    This number is just the ratio of republican:democratic voters, not including other parties
* % turnout (0-1)
"""
votes=pd.read_csv('./src/2020/votes/president_county_candidate.csv', dtype=object)
votes.insert(0, 'id', votes.county+', '+votes.state)
votes=votes.rename(columns={ 'party': 'og_party' })
votes=votes.drop(columns=['state', 'county', 'candidate'])
votes.won=votes.won.astype(bool) # 'True' -> True
# votes.loc[votes.]


# Merge
merged=pd.merge(votes, acs, on='id', how='inner') #if a county is missing from either, it will be dropped


# Export
acs.to_csv(f'./dist/2020-ACS-data.csv', index=False)

