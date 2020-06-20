import pandas as pd 
import numpy as np 
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns 

X1 = np.random.randint(60,size=200)
Y1 = np.random.randint(60, size=200)

x = np.array(list(zip(X1, Y1))).reshape(len(X1), 2)


k_mean = KMeans(n_clusters = 3)

labels = k_mean.fit_predict(x)

centroids = k_mean.cluster_centers_

print("Centroids : ",centroids)
print()

print(" Labels(Predicted) : ",labels)

plt.plot()
plt.title('k means centroids')
plt.xlabel('X', color='r')
plt.ylabel('Y',color='g')

plt.scatter(x[:, 0], x[:, 1], c=labels, s=50, cmap='viridis')

plt.scatter(centroids[:,0], centroids[:,1], marker=".", color='b')
plt.show()