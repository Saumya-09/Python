import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt

from Custom_Logistic import LogisticRegression
#from regression import LogisticRegression

def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy

bc = pd.read_csv("Titanic_Dataset.csv")
#X, y = bc.data, bc.target
y = bc.Survived
X = bc.drop('Survived', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state= 100)
print(X_train.head())
print(X_test.head())
print(y_train.head())
print(y_test.head())
regressor = LogisticRegression(learning_rate=0.001, n_iters=1000)
regressor.fit(X_train, y_train)
predictions = regressor.predict(X_test)
#print(predictions)
print()
print("Accuracy:", accuracy(y_test, predictions))
