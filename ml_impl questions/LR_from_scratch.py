# Implement Linear Regression from scratch
import numpy as np
class LinearRegression:
    def __init__(self):
        self.theta = None

    def fit(self, X, y):
        m, n = X.shape
        # Add intercept term to X
        X_b = np.c_[np.ones((m, 1)), X]
        # Normal Equation: theta = (X^T * X)^(-1) * X^T * y
        self.theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

    def predict(self, X):
        m = X.shape[0]
        X_b = np.c_[np.ones((m, 1)), X]  # Add intercept term
        return X_b.dot(self.theta)
# Example usage
if __name__ == "__main__":
    # Sample dataset
    X = np.array([[1], [2], [3], [4], [5]])  # Features
    y = np.array([2, 3, 5, 7, 11])  # Target variable with some noise

    model = LinearRegression()
    model.fit(X, y)
    predictions = model.predict(X)
    print("Predictions:", predictions)


# Alternative implementation using normal equation without class structure
# 1. simple linear regression using normal equation
import numpy as np

class SimpleLinearRegression:
    def __init__(self):
        self.slope = None
        self.intercept = None

    def fit(self, x, y):
        # Calculate means
        x_mean, y_mean = np.mean(x), np.mean(y)
        
        # Calculate slope (m) and intercept (b) using Least Squares
        numerator = np.sum((x - x_mean) * (y - y_mean))
        denominator = np.sum((x - x_mean) ** 2)
        
        self.slope = numerator / denominator
        self.intercept = y_mean - (self.slope * x_mean)

    def predict(self, x):
        return self.intercept + self.slope * x
# Example usage
if __name__ == "__main__":
    # Sample dataset
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 3, 5, 7, 11])  # Target variable with some noise

    model = SimpleLinearRegression()
    model.fit(x, y)
    predictions = model.predict(x)
    print("Predictions:", predictions)

# 2. Multiple linear regression using normal equation
class LinearRegressionGD:
    def __init__(self, lr=0.01, n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            # 1. Prediction (y_hat = Xw + b)
            y_predicted = np.dot(X, self.weights) + self.bias
            
            # 2. Compute Gradients
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)

            # 3. Update Parameters
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias
# Example usage
if __name__ == "__main__":
    # Sample dataset
    X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])  # Features
    y = np.dot(X, np.array([1, 2])) + 3  # Target variable with some noise

    model = LinearRegressionGD(lr=0.01, n_iters=1000)
    model.fit(X, y)
    predictions = model.predict(X)
    print("Predictions:", predictions)