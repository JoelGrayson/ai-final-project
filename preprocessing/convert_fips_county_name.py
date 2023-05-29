import pandas as pd

df=pd.read_csv('./src/fips/dist/county-names-to-fips.csv', dtype={
    'fips': int,
    'name': str
})

def county_name_to_fips(name): #exported
    matched=df[df.name==name] #should be length 0 or 1
    if matched.shape[0]==0: #no row matches
        return None #null which will be removed later
    return matched.iloc[0].fips


def fips_to_county_name(fips):
    return df[df.fips==fips].iloc[0].name

