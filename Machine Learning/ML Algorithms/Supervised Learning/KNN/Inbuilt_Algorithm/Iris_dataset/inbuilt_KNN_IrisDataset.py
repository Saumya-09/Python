import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data = datasets.load_iris()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

# Create KNN classifier
knn = KNeighborsClassifier(n_neighbors = 5)
# Fit the classifier to the data
knn.fit(X_train,y_train)

#show first 5 model predictions on the test data
predict = knn.predict(X_test)
print()
print("  Predicted values: ")
print("  ",predict)
print()
#check accuracy of our model on the test data
s = knn.score(X_test, y_test)
print()
print("  Accuracy: ")
print("  ",s)
print()