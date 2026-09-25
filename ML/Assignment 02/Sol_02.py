import numpy as np

def logistic_regression(X, Y, k, tau, learning_rate):

    beta = np.random.randn(X.shape[1])
    previous_cost = float("inf")

    for i in range(k):

        # Calculate predicted probabilities
        z = X @ beta
        probability = 1 / (1 + np.exp(-z))

        # Calculate cost
        cost = -np.mean(
            Y * np.log(probability + 1e-10) +
            (1 - Y) * np.log(1 - probability + 1e-10)
        )

        # Calculate gradient
        gradient = (X.T @ (probability - Y)) / len(Y)
        beta = beta - learning_rate * gradient
        if abs(previous_cost - cost) < tau:
            break
        previous_cost = cost
    return beta, cost


n = int(input("\nEnter number of data points : "))
m = int(input("Enter number of variables : "))

X = np.random.randn(n, m)
Y = np.random.randint(0, 2, size=n)

k = int(input("Enter number of iterations (k) : "))
tau = float(input("Enter cost threshold (tau) : "))
learning_rate = float(input("Enter learning rate : "))

beta, final_cost = logistic_regression(X, Y, k, tau, learning_rate)

print("\nLearned Beta : ", beta)
print("\nFinal Cost : ", final_cost)
print("\n")
