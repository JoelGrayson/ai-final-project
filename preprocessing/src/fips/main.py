import pickle
import pandas as pd
from state_abbreviations import state_abbreviations

df=pd.read_csv('./src/fips-codes-and-county-names.csv', dtype={
    'fips': str,
    'name': str,
    'state': str
})
df=df.rename(columns={ 'name': 'county_name' })
df=df.dropna(how='any') #removes state and country names
df.insert(1, 'name', df.county_name+', '+df.state.map(lambda abbr:state_abbreviations[abbr]))
df=df.drop(columns=['state', 'county_name'])

df.to_csv('./dist/county-names-to-fips.csv', index=False)

"""
Dictionary key-access is 6486 times faster according to my time test
>>> %timeit df[df.name=='Kent County, Delaware'].iloc[0].fips
299 µs
>>> %timeit fips2county_name[36061]
46.1 ns
"""
county_name2fips=df.set_index('name', inplace=False)['fips'].to_dict()
fips2county_name=df.set_index('fips', inplace=False)['name'].to_dict()

with open('./dist/county_name2fips.pickle', 'wb') as f:
    pickle.dump(county_name2fips, f)

with open('./dist/fips2county_name.pickle', 'wb') as f:
    pickle.dump(fips2county_name, f)

