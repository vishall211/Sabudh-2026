import numpy as np

def generate_data(theta, n, m):

    beta = np.random.randn(m)
    X = np.ones((n, m))
    if m > 1:
        X[:, 1:] = np.random.randn(n, m - 1)

    z = X @ beta
    probability = 1 / (1 + np.exp(-z))

    Y = np.random.binomial(1, probability)

    flip = np.random.binomial(1, theta, size=n)
    Y = np.where(flip == 1, 1 - Y, Y)

    return X, Y, beta


def logistic_regression(X, Y, k, tau, learning_rate, reg_type, reg_constant):

    beta = np.random.randn(X.shape[1])
    previous_cost = float("inf")

    for i in range(k):
        z = X @ beta
        probability = 1 / (1 + np.exp(-z))

        # Calculate regularized cost
        cost = -np.mean(
            Y * np.log(probability + 1e-10) +
            (1 - Y) * np.log(1 - probability + 1e-10)
        )

        if reg_type == "L1":
            cost += reg_constant * np.sum(np.abs(beta))

        elif reg_type == "L2":
            cost += reg_constant * np.sum(beta ** 2)

        # Calculate gradient
        gradient = (X.T @ (probability - Y)) / len(Y)

        if reg_type == "L1":
            gradient += reg_constant * np.sign(beta)

        elif reg_type == "L2":
            gradient += 2 * reg_constant * beta

        # Update beta
        beta = beta - learning_rate * gradient

        if abs(previous_cost - cost) < tau:
            break

        previous_cost = cost
    return beta, cost


theta = float(input("\nEnter theta : "))
n = int(input("Enter number of data points : "))
m = int(input("Enter number of variables : "))

k = int(input("Enter number of iterations : "))
tau = float(input("Enter cost threshold : "))
learning_rate = float(input("Enter learning rate : "))

reg_type = input("Enter regularization type (L1/L2) : ").upper()
reg_constant = float(input("Enter regularization constant : "))

X, Y, original_beta = generate_data(theta, n, m)
learned_beta, final_cost = logistic_regression(X, Y, k, tau, learning_rate, reg_type, reg_constant)

print("\nOriginal Beta : ", original_beta)
print("\nLearned Beta : ", learned_beta)
print("\nFinal Cost : ", final_cost)
print("\n")