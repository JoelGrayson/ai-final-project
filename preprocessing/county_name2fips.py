import pickle

f=open('./src/fips/dist/county_name2fips.pickle', 'rb')
dict=pickle.load(f)
f.close()

def county_name2fips(name): #exported
    if not (name in dict):
        return None #null which will be removed from df later
    return dict[name]

"""
>>> county_name2fips('New York County, New York')
36061
"""
