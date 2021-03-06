import numpy as np
from collections import Counter
import numpy
import numpy as np

#def euclidean_distance(x1, x2):
#        return np.sqrt(np.sum((x1 - x2)**2))
        
def euclidean_dist(x1,x2):
    return numpy.linalg.norm(x1-x2)


class KNN:

    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)
        

    def _predict(self, x):
        # Compute distances between x and all examples in the training set
        dis = [euclidean_dist(x, x_train) for x_train in self.X_train]
        print(dis)
        # Sort by distance and return indices of the first k neighbors
        k_idx = np.argsort(dis)[:self.k]
        # Extract the labels of the k nearest neighbor training samples
        k_neighbor_labels = [self.y_train[i] for i in k_idx]  
        # return the most common class label
        most_common = Counter(k_neighbor_labels).most_common(1)
        return most_common[0][0]