from sklearn.neighbors import KNeighborsClassifier
import numpy as np

knn = KNeighborsClassifier(

    n_neighbors = 7,     # k value
    weights = 'uniform',
    metric = 'minkowski' # distance
)

X_train = np.array([[2, 3], [5, 4], [3, 2], [9, 9], [8, 6], [7, 8], [6, 9]])
y_train = np.array([0, 0, 0, 1, 1, 1, 1])
knn.fit(X_train, y_train)

X_test = np.array([[1, 2], [9, 9]])
y_pred = knn.predict(X_test)

print(y_pred)