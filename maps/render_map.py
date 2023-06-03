import requests
import plotly.express as px
import pandas as pd
import os
from preprocessing.helpers.fips2county_name import fips2county_name

# Get counties from plotly
response=requests.get('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json')
if response.status_code!=200:
    print('API response was not OK')
    exit()

counties=response.json()
response.close()

# Exported
def merge_fips(fips, party):
    return pd.concat([fips, party], axis=1)\
        .astype({ 'fips': 'str', 'party': 'float' })\
        .sort_values(by='fips')

def render_map(
    filename,
    fips_codes, #dataframe of fips codes and their corresponding party [0-1]
):
    # Plot Data
    fig=px.choropleth(
        fips_codes, geojson=counties, locations='fips',
        color='party', color_continuous_scale=['#ff0000', '#0000ff'], range_color=(0, 1),
        scope='usa', labels={'party': 'Party'}
    )

    fig.update_layout(margin={'r': 0, 't': 0, 'l': 0, 'b': 0})
    filepath=f'./maps/predicted/{filename}'
    fig.write_image(filepath+'.png') #export as PNG into predicted folder
    os.system(f'open {filepath}.png')

    # Write image text
    text='county_name\tfips\tparty\n'
    for index, row in fips_codes.sort_values(by='fips').iterrows():
        text+=f'{fips2county_name(row.fips)}\t{row.fips}\t{row.party}\n'

    with open(filepath+'.tsv', 'w') as f:
        f.write(text)

