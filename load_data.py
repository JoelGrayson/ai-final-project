import pandas as pd

### <CONFIG>
validation_size=.10 #used to find C
train_size=.60
### </>

def load_data(name): #no splits
    df=pd.read_csv(f'./preprocessing/dist/{name}.csv', dtype={ 'fips': 'str', 'party': 'float' })\
        .sample(frac=1) #shuffle
    X=df.drop(columns=['party', 'fips'])
    y=df.party
    fips=df.fips.astype('str')
    return X, y, fips


def load_split_data(name): #splits into categories
    X, y, fips=load_data(name)

    # Manual split
    num_rows=X.shape[0]
    validation_index=round(num_rows*train_size)
    train_index=validation_index+round(num_rows*validation_size)

    return {
        'X_val': X[:validation_index],
        'y_val': y[:validation_index],
        'fips_val': fips[:validation_index],

        'X_train': X[validation_index:train_index],
        'y_train': y[validation_index:train_index],
        'fips_train': fips[validation_index:train_index],

        'X_test': X[train_index:],
        'y_test': y[train_index:],
        'fips_test': fips[train_index:]
    }


def continuous2binary(data): #round y_* data
    for label in ['y_val', 'y_train', 'y_test']:
        data[label]=data[label].round()
    return data

