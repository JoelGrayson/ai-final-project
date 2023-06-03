# ABOUT: 2020 ACS and Voting Information
import pandas as pd
from helpers.county_name2fips import county_name2fips
from helpers.merge_votes_and_acs import merge_acs_and_votes
from helpers.preprocess_acs import preprocess_acs


def data_2020():
    acs=preprocess_acs('./src/2020/ACS/data.csv')

    # Votes
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
    curr_total_votes=0
    for index, row in votes.iterrows():
        if row.fips!=curr_fips: #moving to next row
            percentage_dems=curr_dem_votes/(curr_rep_votes+curr_dem_votes) # type: ignore
                #excludes third-party candidates
            fips_and_party_lst.append([curr_fips, percentage_dems, curr_total_votes])
            curr_fips=row.fips #update curr_fips to next fips
            curr_total_votes=0
        
        curr_total_votes+=row.total_votes
        if row.party=='DEM':
            curr_dem_votes=row.total_votes
        if row.party=='REP':
            curr_rep_votes=row.total_votes


    fips_and_party=pd.DataFrame(fips_and_party_lst, columns=['fips', 'party', 'total_votes']).astype({ 'fips': str, 'party': float, 'total_votes': int })


    # Merge
    merged=merge_acs_and_votes(acs, fips_and_party)

    # Make fips and party at the front
    old_index=list(merged.columns)
    old_index.remove('fips')
    old_index.remove('party')
    old_index.remove('total_votes')
    new_index=['fips', 'party', 'total_votes', *old_index]
    merged.reindex(columns=new_index)

    # Export
    merged.to_csv('./dist/2020-acs-and-votes.csv', index=False, columns=new_index)

