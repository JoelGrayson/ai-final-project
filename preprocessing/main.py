import pandas as pd
from county_name2fips import county_name2fips

# pd.set_option('display.max_columns', 50)
# pd.set_option('display.max_rows', 50)


##### 2020 ACS and Voting Information #####
# ACS
acs=pd.read_csv(f'./src/2020/ACS/data.csv', dtype=object, na_values=['(X)', 'N', '-', 'median-', '100-', '**', '***', '*****', 'null'])

acs.drop([0], inplace=True) #drop first row, which is column metadata

acs.insert(0, 'fips', acs.GEO_ID.map(lambda x : x[9:])) #identifier

cols_to_drop=filter(lambda x: (x[-1]!='E' or x=='NAME') and x!='fips', acs.columns) #keep only estimates, not margin of errors or notes. Keep fips
acs.drop(columns=cols_to_drop, inplace=True)

# remove all columns that have an missing data symbols specified in /preprocessing/src/2020/ACS/table-notes.html
acs.dropna(axis=1, inplace=True)
for column in acs.columns:
    if column!='fips': #all numeric data except fips, which is a string
        acs[column]=acs[column].astype(float)


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
votes.insert(0, 'fips', (votes.county+', '+votes.state).map(county_name2fips), True)
votes.dropna(axis=0, inplace=True, how='any')
votes.won=votes.won.astype(bool) # 'True' -> True
votes.fips=votes.fips.astype(str) # '01000'
votes.total_votes=votes.total_votes.astype(int)
votes.sort_values('fips', inplace=True) #make sure the fips are grouped together


# Convert to proper Republican/Democrat ratios
"""
Pseudocode
Create another votes dataframe
go through votes, keeping track of the democratic:republican ratio
Once the fips code changes, go back one index to change the 
"""
# Current fips-related variables
fips_and_party_lst=[] #fips and party

curr_fips=votes.iloc[0].fips #first fips
curr_dem_votes=None
curr_rep_votes=None
for index, row in votes.iterrows():
    if row.fips!=curr_fips: #moving to next row
        percentage_dems=curr_dem_votes/(curr_rep_votes+curr_dem_votes) # type: ignore
            #excludes third-party candidates
        fips_and_party_lst.append([curr_fips, percentage_dems])
        curr_fips=row.fips #update curr_fips to next fips
    
    if row.party=='DEM':
        curr_dem_votes=row.total_votes
    if row.party=='REP':
        curr_rep_votes=row.total_votes


fips_and_party=pd.DataFrame(fips_and_party_lst, columns=['fips', 'party']).astype({ 'fips': str, 'party': float })


# Merge
merged=pd.merge(acs, fips_and_party, on='fips', how='inner') #if a county is missing from either, it will be dropped


# Export
merged.to_csv(f'./dist/2020-acs-and-votes.csv', index=False)

