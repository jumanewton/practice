# Implement K-Nearest Neighbors (KNN) classifier
import numpy as np
from collections import Counter

class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def euclidean_distance(self, point1, point2):
        return np.sqrt(np.sum((point1 - point2) ** 2))

    def predict(self, X):
        predictions = []
        for test_point in X:
            # Calculate distances to all training points
            distances = []
            for i, train_point in enumerate(self.X_train):
                dist = self.euclidean_distance(test_point, train_point)
                distances.append((dist, self.y_train[i]))

            # Sort by distance and select the k nearest neighbors
            distances.sort(key=lambda x: x[0])
            k_nearest = distances[:self.k]

            # Get the labels of the k nearest neighbors
            k_nearest_labels = [label for _, label in k_nearest]

            # Vote for the most common label
            most_common_label = Counter(k_nearest_labels).most_common(1)[0][0]
            predictions.append(most_common_label)

        return predictions
# Example usage
if __name__ == "__main__":
    # Sample dataset (4 samples, 2 features)
    X_train = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])
    y_train = np.array([0, 0, 0, 1])  # Class labels
    X_test = np.array([[1, 1], [0, 0], [0, 1]])
    knn = KNN(k=3)
    knn.fit(X_train, y_train)
    predictions = knn.predict(X_test)
    print("Predictions:", predictions)  # Output: [0, 1, 0]


# Alternative implementation using scikit-learn
from sklearn.neighbors import KNeighborsClassifier
# Sample dataset (4 samples, 2 features)
X_train = np.array([[1, 1], [1, 0], [0, 1], [0, 0]])
y_train = np.array([0, 0, 0, 1])  # Class labels
X_test = np.array([[1, 1], [0, 0], [0, 1]])
knn = KNeighborsClassifier(n_neighbors=3)   
knn.fit(X_train, y_train)
predictions = knn.predict(X_test)
print("Predictions:", predictions)  # Output: [0, 1, 0]

# Example usage with Iris dataset
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 1. Load data
iris = load_iris()
X, y = iris.data, iris.target

# 2. Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Create and train the model (k=3)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# 4. Make predictions
y_pred = knn.predict(X_test)

# 5. Evaluate accuracy
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
