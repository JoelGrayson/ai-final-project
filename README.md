I attempted to create a model which can predict how a county votes in the presidential elections (Democratic or Republican) based on information collected from the American Community Survey (ACS). The program will create a map of the counties as red and blue. I chose the ACS over the decennial census because it collects data every year and has more features. The features are Housing Occupancy, Units in Structure, Year Structure Built, Rooms, Bedrooms, Housing Tenure, Year Householder Moved into Unit, Vehicles Available, House Heating Fuel, Selected Characteristics, Occupants per Room, Value, Mortgage Status, Selected Monthly Owner Costs (SMOC), Selected Monthly Owner Costs as a Percentage of Household Income (SMOCAPI), Gross Rent, and Gross Rent as a Percentage of Household Income (GRAPI).

First, I downloaded the ACS' 5-year average data for 2020 and 2010 from [data.census.gov's advanced search](https://data.census.gov/advanced), which I had learned how to use at a community board member census training session. Then, I had to preprocess it by removing the margin of error and notes columns. I dropped all the various symbols that corresponded to null, such as '(X)' and '\*\*'. I downloaded the presidential voting data from sources that I found in the footnotes of Wikipedia pages since the federal election commission's centralized data is not in a developer-friendly format (PDFs and mixed Excel spreadsheets). I downloaded from [kaggle.com/datasets/unanimad/us-election-2020](http://kaggle.com/datasets/unanimad/us-election-2020) for the 2020 election and [github.com/john-guerra/US\_Elections\_Results](https://github.com/john-guerra/US_Elections_Results) for 2012. Both were of different formats and needed to be preprocessed differently in the files preprocessing/data\_2020.py and preprocessing/data\_2010\_2012.py. The 2020 data had county and state names instead of FIPS codes, so I inserted a FIPS column using another dataframe that had FIPS codes and state and county names from. Then, I was able to merge the data frames on FIPS codes using an inner join. I iterated through 2020 rows to create the party column, which was what percentage of all Democratic and Republican voters voted Democratic.

One bug I faced was that I stored my FIPS codes as numbers instead of strings, which caused problems when rendering the map because it did not recognize "1000" as "01000." I padded a zero at the front to solve this problem.

After preprocessing, I tried many different models with these results:

|   |   |  **2010-2012** | **2020** |
| --- | --- | ---------- | -------- |
| Continuous | Mean Classifier (Baseline) | MSE 0.0248 | MSE 0.0267 |
| Continuous | Linear Regression | MSE 0.0476 | MSE 0.0838 |
| Continuous | Support Vector Regression | MSE 0.409 | MSE 0.268 |
| Binary | Majority Classifier (Baseline) | MSE 0.386<br>Log Loss 13.91<br>Accuracy 0.614 | MSE 0.167<br>Log Loss 6.036<br>Accuracy 0.833 |
| Binary | Logistic Regression | MSE 0.228<br>Log Loss 8.215<br>Accuracy 0.772<br>Precision 0.758<br>Recall 0.602 | MSE 0.114<br>Log Loss 4.121<br>Accuracy 0.886<br>Precision 0.634<br>Recall 0.750 |
| Binary | Decision Trees | MSE 0.273<br>Log Loss 9.827<br>Accuracy 0.727<br>Precision 0.641<br>Recall 0.669 | MSE 0.148<br>Log Loss 5.340<br>Accuracy 0.852<br>Precision 0.557<br>Recall 0.567 |
| Binary | Random Forest | MSE 0.202<br>Log Loss 7.311<br>Accuracy 0.797<br>Precision 0.790<br>Recall 0.647 | MSE 0.098<br>Log Loss 3.541<br>Accuracy 0.902<br>Precision 0.864<br>Recall 0.490 |
| Binary | KNN | MSE 0.230<br>Log Loss 8.294<br>Accuracy 0.770<br>Precision 0.734<br>Recall 0.633 | MSE 0.132<br>Log Loss 4.759<br>Accuracy 0.868<br>Precision 0.893<br>Recall 0.240 |
| Binary | Naive-Bayes | MSE 0.366<br>Log Loss 13.207<br>Accuracy 0.634<br>Precision 0.578<br>Recall 0.189 | MSE 0.135<br>Log Loss 4.875<br>Accuracy 0.865<br>Precision 0.885<br>Recall 0.221 |
| Binary | Bernoulli Naive Bayes | MSE 0.274<br>Log Loss 9.866<br>Accuracy 0.726<br>Precision 0.618<br>Recall 0.763 | MSE 0.177<br>Log Loss 6.385<br>Accuracy 0.823<br>Precision 0.478<br>Recall 0.635 |
| Binary | Support Vector Classifier | MSE 0.260<br>Log Loss 9.355<br>Accuracy 0.740<br>Precision 0.653<br>Recall 0.698 | MSE 0.143<br>Log Loss 5.166<br>Accuracy 0.857<br>Precision 0.569<br>Recall 0.596 |


I then used plotly's choropleth library to render the maps colorfully by county level.

For continuous models, no model performed better than the baseline and Random forest performed best on binary. This shows that housing data is not a great predictor of how a county will vote in the election, a surprising conclusion.

Looking at the rendered map that the 2020 random forest binary model predicts, one can see that the model clearly does not understand which counties are supposed to be red or blue. It seemingly chooses blue or red randomly, not at all in the supposed relationship. The average party for 2020 is 0.338, suggesting that it should predict Republican most of the time. This is because many Democratic counties are urban and have a large population size (such as New York County at 1.6 million). In order to prevent all the counties from being weighed equally, I added the total number of votes per county as the weights, the optional third parameter for the model.fit method.

In `linear_model_features.py`, you can see how the housing factors affect county data. [Here is a list of all the results of the run program](https://docs.google.com/document/d/1xMnac38aQ3cxyWDbwOQvfslj-PB1R86xrC0kwVgyvto/edit). Unfortunately, many of the features are inconsistent between the two times I ran the program. However, there were some understandable features such as `BEDROOMS \> Total housing units \> 5 or more bedrooms (DP04\_0044PE)` being negative in both cases since rich people tend to be more Republican. Interestingly, all the `ROOMS \> Total housing units` features were negative and `UNITS IN STRUCTURE \> Total housing units` were positive but they were negative or positive to different degrees, causing the differences.

To improve the results, I likely should use the census data, which has more economic, population, and racial features that would correlate better with party. Although my model may not work as well as I had hoped, I learned a lot throughout this final project, such as how to manage a large python code base over time and separate the process into three stages (preprocessing, models, and rendering the map).

Throughout the process, I used different modules and folders to keep code organized. The top-level folder is a package, indicated by `__init__.py`, allowing all imports in modules and submodules to be from that relative path. This allows me to import preprocessing/helpers/fips2county\_name.py from the file map/render\_map using from preprocessing.helpers.fips2county\_name import fips2county\_name.

I used many regular expressions, my old friend. For example, replacing `(^\d{4}(?!\d))` with `0$1` to prepend four FIPS digit codes with a `0` in the csv file and `(\d{5})` with `"$1"` to surround the FIPS codes with quotes.


### Quick Facts
* 3143 counties in the United States
* 3106 counties in 2020 preprocessed data
* 3114 counties in 2010-2012 preprocessed data (found with `awk -F ',' '{print $1}' \<'./preprocessing/dist/2010-acs-and-2012-votes.csv' | uniq | sort | wc --lines`)
* Elections inspected: 2008 and 2020
* Corresponding census data: 2010 and 2020 (ACS)


### Sources
* Data
  * [FIPS Codes Corresponding to County and State Names](https://github.com/kjhealy/fips-codes/blob/master/state_and_county_fips_master.csv)
  * [2020 Voting Data](https://www.kaggle.com/datasets/unanimad/us-election-2020)
  * [2012 Voting Data](https://github.com/john-guerra/US_Elections_Results)
  * Wikipedia for Filling in Missing County Data
  * [ACS from Census Advanced Search](https://data.census.gov/advanced), specifically this query: https://data.census.gov/table?t=Business+and+Economy:Business+and+Owner+Characteristics&g=010XX00US$0500000&d=ACS+5-Year+Estimates+Data+Profiles&tid=ACSDP5Y2021.DP04
  * True maps from http://www-personal.umich.edu/~mejn/election/2008/
* Code
  * [Pandas DataFrame Documentation](https://pandas.pydata.org/docs/reference/frame.html)
  * [Plotly Choropleth Maps Documentation](https://plotly.com/python/choropleth-maps/)


### Notes
* How the election works - each county has multiple precincts which correspond to a voting poll station. The counties then report to the state.
* Choropleth map - shows the intensity of each region in a map through color intensity
    * [Plotly Chloropleth Documentation](https://plotly.com/python/choropleth-maps/)
* Federal Information Processing Standards (FIPS) codes are standardized five-digit numeric codes identifying counties
* Election Districts (EDs in Alaska)
    * Boroughs are Alaska's form of counties (parishes for Louisiana)


### Running Requirements
pip packages: kaleido pandas requests plotly\
Pro tip: pipe `python3 model_comparison.py` into glow for rendering markdown. Install glow [here](https://github.com/charmbracelet/glow#installation).

