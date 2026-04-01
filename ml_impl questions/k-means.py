# Implement K-Means clustering
import numpy as np
class KMeans:
    def __init__(self, n_clusters=3, max_iters=100):
        self.n_clusters = n_clusters
        self.max_iters = max_iters
        self.centroids = None

    def fit(self, X):
        m, n = X.shape
        # Randomly initialize centroids by selecting random samples from the dataset
        np.random.seed(42)  # For reproducibility
        random_indices = np.random.choice(m, self.n_clusters, replace=False)
        self.centroids = X[random_indices]

        for _ in range(self.max_iters):
            # Assign clusters based on closest centroid
            distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
            closest_centroids = np.argmin(distances, axis=1)

            # Update centroids by calculating the mean of assigned samples
            new_centroids = np.array([X[closest_centroids == k].mean(axis=0) for k in range(self.n_clusters)])

            # Check for convergence (if centroids do not change)
            if np.all(self.centroids == new_centroids):
                break
            
            self.centroids = new_centroids

    def predict(self, X):
        distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
        return np.argmin(distances, axis=1)
# Example usage
if __name__ == "__main__":
    # Sample dataset
    X = np.array([[1, 2], [1, 4], [1, 0],
                  [4, 2], [4, 4], [4, 0]])
    
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(X)
    print("Centroids:\n", kmeans.centroids)
    print("Cluster Assignments:", kmeans.predict(X))


# Alternative implementation of K-Means clustering using a more concise approach
import numpy as np
from collections import Counter

class KNNFromScratch:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        # KNN is a "lazy learner"—it just stores the data
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        return [self._predict_single(x) for x in X]

    def _predict_single(self, x):
        # Compute Euclidean distances
        distances = [np.sqrt(np.sum((x - x_train)**2)) for x_train in self.X_train]
        
        # Get indices of k nearest neighbors
        k_indices = np.argsort(distances)[:self.k]
        
        # Extract labels and find the most common one
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]
# Example usage
if __name__ == "__main__":
    # Sample dataset
    X_train = np.array([[1, 2], [1, 4], [1, 0],
                        [4, 2], [4, 4], [4, 0]])
    y_train = np.array([0, 0, 0, 1, 1, 1])  # Class labels

    knn = KNNFromScratch(k=3)
    knn.fit(X_train, y_train)

    X_test = np.array([[1, 3], [4, 3]])
    predictions = knn.predict(X_test)
    print("Predictions:", predictions)  # Output: [0, 1]
    