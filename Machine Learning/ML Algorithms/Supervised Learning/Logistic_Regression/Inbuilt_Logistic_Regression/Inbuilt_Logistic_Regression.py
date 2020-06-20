import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("Titanic_Dataset.csv")
print(df.head())

x = df.drop("Survived",axis = 1)
y = df.Survived
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.1, random_state=4)
pd.DataFrame(x_train).fillna(0)
print(x_train.head())
print(x_test.head())
print(y_train.head())
print(y_test.head())

logistic_regression = LogisticRegression(max_iter=500)
logistic_regression.fit(x_train,y_train)

y_pred = logistic_regression.predict(x_test)
print()
print("  Labels: ")
print("  ", y_pred)
print()
acc = metrics.accuracy_score(y_test, y_pred)
accuracy_percentage = 100 * acc
print()
print("  Accuracy: ")
print("  ",accuracy_percentage)
print()



