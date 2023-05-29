# About
[Proposal](https://docs.google.com/document/d/1E4FkeQ8UsCsFyLSj4cYP6SSVMuc98ruH8EV7Radr36I/edit)


# Data
## American Community Survey (ACS)
Data estimates are a five year average.
https://data.census.gov/table?t=Business+and+Economy:Business+and+Owner+Characteristics&g=010XX00US$0500000&d=ACS+5-Year+Estimates+Data+Profiles&tid=ACSDP5Y2021.DP04
* All Counties within United States and Puerto Rico
* ACS 5-Year Estimates Data Profiles
* Business and Economy
* Business and Owner Characteristics

## Voting
* I Used
    * 2016 - https://www.kaggle.com/datasets/benhamner/2016-us-election
    * 2020 - https://www.kaggle.com/datasets/unanimad/us-election-2020
    * 2008 - 
* Others
    * Wikipedia map data for 2008 election http://www-personal.umich.edu/~mejn/election/2008/

## Others (not used)
* https://census.gov/data/developers/data-sets.html has a list of datasets for developers


# Notes
* How the election works - each county has multiple precincts which correspond to a voting poll station. The counties then report to the state.
* Choropleth map - shows the intensity of each region in a map through color intensity
    * https://plotly.com/python/choropleth-maps/
* Federal Information Processing Standards (FIPS) codes are standardized five-digit numeric codes identifying counties


# Requirements
## Running
pip packages: kaleido pandas requests plotly

## Development
ipython3
