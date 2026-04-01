# Implement Gradient Descent for linear regression
import numpy as np
class LinearRegressionGD:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.theta = None

    def fit(self, X, y):
        m, n = X.shape
        self.theta = np.zeros(n)
        
        for _ in range(self.n_iterations):
            gradients = (1/m) * X.T.dot(X.dot(self.theta) - y)
            self.theta -= self.learning_rate * gradients

    def predict(self, X):
        return X.dot(self.theta)
# Example usage
if __name__ == "__main__":
    # Sample dataset
    X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])  # Features
    y = np.dot(X, np.array([1, 2])) + 3  # Target variable with some noise

    model = LinearRegressionGD(learning_rate=0.01, n_iterations=1000)
    model.fit(X, y)
    predictions = model.predict(X)
    print("Predictions:", predictions)

# Alternative implementation using gradient descent without class structure

import numpy as np

def gradient_descent(x, y, learning_rate=0.01, epochs=1000):
    m, b = 0.0, 0.0  # Initialize slope and intercept
    n = float(len(x))
    
    for i in range(epochs):
        # 1. Predictions
        y_pred = m * x + b
        
        # 2. Compute Gradients (Partial Derivatives)
        dm = (-2/n) * sum(x * (y - y_pred))
        db = (-2/n) * sum(y - y_pred)
        
        # 3. Update Parameters
        m = m - learning_rate * dm
        b = b - learning_rate * db
        
    return m, b
# Example usage
if __name__ == "__main__":
    # Sample dataset
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 3, 5, 7, 11])  # Target variable with some noise

    m, b = gradient_descent(x, y)
    print(f"Slope (m): {m}, Intercept (b): {b}")