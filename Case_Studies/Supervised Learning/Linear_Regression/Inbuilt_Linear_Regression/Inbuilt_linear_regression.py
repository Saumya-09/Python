import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('HeadBrain.csv')


y = df['Brain Weight(grams)'].values
y.shape
X = df['Head Size(cm^3)'].values
X = X.reshape(X.shape[0], 1)
X.shape


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
print()
print("  Labels: ")
print("  ",y_pred)
print()

s = lr.score(X_test, y_test)
print()
print("  Accuracy: ")
print("  ",s)
print()
min_pred = X_train.min() * lr.coef_ + lr.intercept_
max_pred = X_train.max() * lr.coef_ + lr.intercept_

plt.scatter(X_train, y_train, c='red')
plt.plot([X_train.min(), X_train.max()],[min_pred, max_pred],color='blue',linewidth=2)
plt.xlabel('Head size (cm^3)')
plt.ylabel('Brain weight (grams)');
plt.legend()
plt.show()