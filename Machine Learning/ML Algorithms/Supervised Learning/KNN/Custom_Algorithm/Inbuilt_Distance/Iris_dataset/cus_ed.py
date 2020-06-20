import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
cmap = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

from knn1 import KNN

def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy
 

iris = datasets.load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

k = 5 #n can be customised
clf = KNN(k=k)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
print()
print("custom algorithm accuracy uing inbuilt Euclidean Distance", accuracy(y_test, predictions))
