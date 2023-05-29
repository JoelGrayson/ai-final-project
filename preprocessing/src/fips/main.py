import pandas as pd
from state_abbreviations import state_abbreviations

df=pd.read_csv('./src/fips-codes-and-county-names.csv', dtype={
    'fips': int,
    'name': str,
    'state': str
})
df=df.rename(columns={ 'name': 'county_name' })
df=df.dropna(how='any') #removes state and country names
df.insert(1, 'name', df.county_name+', '+df.state.map(lambda abbr:state_abbreviations[abbr]))
df=df.drop(columns=['state', 'county_name'])

df.to_csv('./dist/county-names-to-fips.csv', index=False)
