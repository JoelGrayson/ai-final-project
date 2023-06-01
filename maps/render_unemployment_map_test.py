from render_map import render_map
import pandas as pd

df=pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv', dtype={'fips': str, 'unemp': float})
df.rename(columns={ 'unemp': 'party' }, inplace=True)
df.party/=15 #make from 0-1
render_map('unemployment', df)
