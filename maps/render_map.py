import requests
import plotly.express as px

# Get Counties
response=requests.get('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json')
if response.status_code!=200:
    print('API response was not OK')
    exit()

counties=response.json()
response.close()

# Exported
def render_map(
    filename,
    fips_codes #dataframe of fips codes and their corresponding party [0-1]
):
    # Plot Data
    fig=px.choropleth(fips_codes, geojson=counties, locations='fips', color='party', color_continuous_scale=['#ff0000', '#0000ff'], range_color=(0, 1), scope='usa', labels={'party': 'Party'})

    fig.update_layout(margin={'r': 0, 't': 0, 'l': 0, 'b': 0})
    # fig.show()
    fig.write_image(f'./predicted/{filename}.png') #export as PNG into predicted folder

