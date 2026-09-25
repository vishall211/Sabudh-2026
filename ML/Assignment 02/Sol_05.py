import numpy as np

class Regression:

    def __init__(self, learning_rate, k, tau):
        self.learning_rate = learning_rate
        self.k = k
        self.tau = tau
        self.beta = None

    def fit(self, X, Y):
        self.beta = np.random.randn(X.shape[1])
        previous_cost = float("inf")

        for i in range(self.k):
            predictions = self.predict(X)
            cost = self.cost_function(X, Y, predictions)
            gradient = self.gradient(X, Y, predictions)

            self.beta = self.beta - self.learning_rate * gradient
            if abs(previous_cost - cost) < self.tau:
                break
            previous_cost = cost

        return self.beta, cost


class LinearRegression(Regression):

    def predict(self, X):
        return X @ self.beta

    def cost_function(self, X, Y, predictions):
        return np.mean((Y - predictions) ** 2) / 2

    def gradient(self, X, Y, predictions):
        return (X.T @ (predictions - Y)) / len(Y)


class LogisticRegression(Regression):

    def predict(self, X):
        z = X @ self.beta
        return 1 / (1 + np.exp(-z))

    def cost_function(self, X, Y, predictions):
        return -np.mean(
            Y * np.log(predictions + 1e-10) +
            (1 - Y) * np.log(1 - predictions + 1e-10)
        )

    def gradient(self, X, Y, predictions):
        return (X.T @ (predictions - Y)) / len(Y)


n = int(input("\nEnter number of data points : "))
m = int(input("Enter number of variables : "))

X = np.random.randn(n, m)
Y = np.random.randint(0, 2, size=n)

k = int(input("Enter number of iterations : "))
tau = float(input("Enter cost threshold : "))
learning_rate = float(input("Enter learning rate : "))

model = LogisticRegression(learning_rate, k, tau)
beta, final_cost = model.fit(X, Y)

print("\nLearned Beta : ",beta)
print("Final Cost : ",final_cost)
print("\n")
