import pandas as pd

### <CONFIG>
validation_size=.10 #used to find C
train_size=.60
### </>

def load_data(): #returns [X_val, y_val, X_train, y_train, X_test, y_test]
    df=pd.read_csv('./preprocessing/dist/2020-acs-and-votes.csv')\
        .drop(columns=['fips'])\
        .sample(frac=1) #shuffle


    # Manual split
    num_rows=df.shape[0]
    validation_index=round(num_rows*train_size)
    train_index=validation_index+round(num_rows*validation_size)

    val_data=df[:validation_index]
    train_data=df[validation_index:train_index]
    test_data=df[train_index:]

    def get_xy(rows):
        X=rows.drop(columns=['party'])
        y=rows.party
        return X, y


    # Export ↓
    X_val,     y_val=get_xy(val_data)
    X_train, y_train=get_xy(train_data)
    X_test,   y_test=get_xy(test_data)

    return [X_val, y_val, X_train, y_train, X_test, y_test]

