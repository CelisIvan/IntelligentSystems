import numpy as np
from collections import Counter


def eu_dis(x1, x2):
        return np.sqrt(np.sum((x1 - x2)**2))


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
        # Calc distances
        distances = [eu_dis(x, x_train) for x_train in self.X_train]

        # Sort and return first k indexes
        indexes = np.argsort(distances)[:self.k]
        # Extract the labels of the k nearest neighbor training samples
        k_neighbor_labels = [self.y_train[i] for i in indexes]
        # return the most common class label
        neigh_labels =[None]*self.k
        for i in range (self.k):
            neigh_labels[i] = k_neighbor_labels[i][0]
        most_common = Counter(neigh_labels).most_common(1)
        return most_common[0][0]