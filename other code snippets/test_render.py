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
def merge_fips(fips, data):
    return pd.concat([fips, data], axis=1)

def render_map(
    filename,
    fips_codes, #dataframe of fips codes and their corresponding party [0-1]
):
    # Plot Data
    fig=px.choropleth(
        fips_codes, geojson=counties, locations='fips',
        scope='usa', labels={'party': 'Party'},
        color='party', color_continuous_scale='Viridis', range_color=(0, 1),
        # color='party', color_continuous_scale=['#ff0000', '#0000ff'], range_color=(0, 1),
    )

    fig.update_layout(margin={'r': 0, 't': 0, 'l': 0, 'b': 0})
    fig.write_image(filename+'.png') #export as PNG into predicted folder
    os.system(f'open {filename}.png')


render_map('test', pd.DataFrame([ 
    # [56001, 1], [56003, 1], [56005, 1], [56007, 1], [56009, 1], [56011, 1], [56013, 1], [56015, 1], [56017, 1], [56019, 1], [56021, 1], [56023, 1], [56025, 1], [56027, 1], [56029, 1], [56031, 1], [56033, 1], [56035, 1], [56037, 1], [56039, 1], [56041, 1], [56043, 1] #Wyoming
    [6001, 1], [6003, 1], [6005, 1], [6007, 1], [6009, 1], [6011, 1], [6013, 1], [6015, 1], [6017, 1], [6019, 1], [6021, 1], [6023, 1], [6025, 1], [6027, 1], [6029, 1], [6031, 1], [6033, 1], [6035, 1], [6037, 1], [6039, 1], [6041, 1], [6043, 1], [6045, 1], [6047, 1], [6049, 1], [6051, 1], [6053, 1], [6055, 1], [6057, 1], [6059, 1], [6061, 1], [6063, 1], [6065, 1], [6067, 1], [6069, 1], [6071, 1], [6073, 1], [6075, 1], [6077, 1], [6079, 1], [6081, 1], [6083, 1], [6085, 1], [6087, 1], [6089, 1], [6091, 1], [6093, 1], [6095, 1], [6097, 1], [6099, 1], [6101, 1], [6103, 1], [6105, 1], [6107, 1], [6109, 1], [6111, 1], [6113, 1], [6115, 1] #California
], columns=['fips', 'party']))

