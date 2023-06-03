import pandas as pd

def merge_acs_and_votes(acs, votes):
    '''
    ACS must be in the format:
        fips: number
        party: float where 0 for Republican, 1 for Democrat
            Mnemonic: Republicans want less government and Democrats want more
            This number is just the ratio of Republican:Democratic votes, not including other parties
    '''
    merged=pd.merge(acs, votes, on='fips', how='inner') #if a county is missing from either, it will be dropped
    return merged

