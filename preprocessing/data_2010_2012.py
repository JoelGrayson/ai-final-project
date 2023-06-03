# ACS is from 2010
# Election votes are from 2012

import pandas as pd
from helpers.county_name2fips import county_name2fips
from helpers.merge_votes_and_acs import merge_acs_and_votes
from helpers.preprocess_acs import preprocess_acs


def data_2010_2012():
    acs=preprocess_acs('./src/2010/ACS/data.csv')

    # Votes
    votes=pd.read_csv('./src/2012/votes-by-county.csv', dtype={ 'per_dem': float, 'per_gop': float })\
        .dropna(axis=0, how='any')\
        .rename(columns={ 'votes_total': 'total_votes' })

    # Proper fips
    votes.insert(
        0,
        'fips',
        votes.combined_fips.map(lambda val : f'0{val}' if val<10000 else str(val)) #1000 -> '01000'
    )

    # Party
    votes.insert(1, 'party', votes.per_dem/(votes.per_dem+votes.per_gop))

    # Columns
    votes.sort_values('fips', inplace=True) #make sure the fips are grouped together
    votes.drop(columns=['combined_fips', 'per_dem', 'per_gop', 'votes_dem', 'votes_gop', 'county_name', 'state_abbr'], inplace=True)


    # Merge
    merged=merge_acs_and_votes(acs, votes)

    # Make fips and party at the front
    old_index=list(merged.columns)
    old_index.remove('fips')
    old_index.remove('party')
    old_index.remove('total_votes')
    new_index=['fips', 'party', 'total_votes', *old_index]
    merged.reindex(columns=new_index)


    # Export
    merged.to_csv('./dist/2010-acs-and-2012-votes.csv', index=False, columns=new_index)



