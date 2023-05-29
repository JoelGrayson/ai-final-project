import pandas as pd

df=None #for global scope of ipython -i interactivity

def main():
    pd.set_option('display.max_columns', 50)
    pd.set_option('display.max_rows', 50)

    process_acs('2010')
    process_acs('2020')
    preprocess_2020_votes()


def process_acs(year):
    global df
    df=pd.read_csv(f'./src/{year}/ACS/data.csv', dtype=object)
    df=df.drop([0]) #drop first row
    
    # df=df.drop(columns=['NAME']) #drop first row
    # df=df.astype('int32') #convert all columns to int32
    cols_to_drop=filter(lambda x: x[-1]!='E', df.columns) #keep only estimates, not margin of errors or notes
    df=df.drop(columns=cols_to_drop)

    df.to_csv(f'./dist/{year}-ACS-data.csv', index=False)


def preprocess_2020_votes():
    global df
    df=pd.read_csv('./src/2020/votes/president_county_candidate.csv', dtype=object)

    df.to_csv('./dist/2020-votes.csv', index=False)


main()
