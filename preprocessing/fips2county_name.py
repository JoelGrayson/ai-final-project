import pickle

f=open('./preprocessing/src/fips/dist/fips2county_name.pickle', 'rb')
dict=pickle.load(f)
f.close()

def fips2county_name(fips): # (fips: number): string
    if not (fips in dict):
        return None #null which will be removed from df later
    return dict[fips]

"""
>>> fips2county_name(36061)
'New York County, New York'
"""
