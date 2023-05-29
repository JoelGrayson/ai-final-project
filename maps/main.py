import requests
import pandas as pd
import plotly.express as px

# Get Counties
response=requests.get('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json')
if response.status_code!=200:
    print('API response was not OK')
    exit()

counties=response.json()
response.close()


# Get data
df=pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv', dtype={'fips': str, 'unemp': float})


# Plot Data
fig=px.choropleth(df, geojson=counties, locations='fips', color='unemp', color_continuous_scale=['#ff0000', '#0000ff'], range_color=(0, 12), scope='usa', labels={'unemp': 'unemployment Rate'})

fig.update_layout(margin={'r': 0, 't': 0, 'l': 0, 'b': 0})
# fig.show()
fig.write_image('./predicted/map.png') #export as PNG into predicted folder

