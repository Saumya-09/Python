import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv("Play_Predictor.csv")
print(data.head())

 
'''#X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)'''

# Import label encoder 
from sklearn import preprocessing 
# label_encoder object knows how to understand word labels. 
label_encoder = preprocessing.LabelEncoder() 
# Encode labels in column 'species'. 
data['Wether']= label_encoder.fit_transform(data['Wether']) 
print(data['Wether'].unique())
label_encode = preprocessing.LabelEncoder() 
# Encode labels in column 'species'. 
data['Temperature']= label_encode.fit_transform(data['Temperature']) 
print(data['Temperature'].unique())

y = data.Play
x = data.drop('Play', axis=1)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2, random_state=1234)
print()
print(y_test)
print()
# Create KNN classifier
knn = KNeighborsClassifier(n_neighbors = 3)
# Fit the classifier to the data
knn.fit(x_train,y_train)

#show first 5 model predictions on the test data
predic = knn.predict(x_test)
print()
print("  Predicted values: ")
print("  ", predic)
print()

#check accuracy of our model on the test data
s = knn.score(x_test, y_test)
s*=100
print()
print("  Accuracy: ")
print("  ",s)
print()