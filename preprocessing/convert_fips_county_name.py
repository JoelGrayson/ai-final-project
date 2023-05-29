import pandas as pd

df=pd.read_csv('./src/fips/dist/county-names-to-fips.csv', dtype={
    'fips': int,
    'name': str
})

def county_name_to_fips(name): #exported
    return df[df.name==name].fips[0]


def fips_to_county_name(fips):
    return df[df.fips==fips].name[0]

