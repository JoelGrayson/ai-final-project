from sklearn.linear_model import LogisticRegression
from models.binary.evaluate import evaluate

def classify(data, C=1.0):
    model=LogisticRegression(C=C, max_iter=3000) #classifier model
    
    model.fit(data['X_train'], data['y_train'])
    # Probabilistic
    y_pred=model.predict(data['X_test'])
    return y_pred


def evaluate_hyperparameters(data, C): #train on training, evaluate on validation
    model=LogisticRegression(C=C, max_iter=3000) #classifier model
    model.fit(data['X_train'], data['y_train'])
    # Probabilistic
    y_pred=model.predict(data['X_val'])
    evaluate(data['y_val'], y_pred)

