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


def logistic_regression(X, Y, k, tau, learning_rate):

    beta = np.random.randn(X.shape[1])
    previous_cost = float("inf")

    for i in range(k):

        z = X @ beta
        probability = 1 / (1 + np.exp(-z))

        cost = -np.mean(
            Y * np.log(probability + 1e-10) +
            (1 - Y) * np.log(1 - probability + 1e-10)
        )

        gradient = (X.T @ (probability - Y)) / len(Y)
        beta = beta - learning_rate * gradient
        if abs(previous_cost - cost) < tau:
            break
        previous_cost = cost
    return beta, cost


m = int(input("\nEnter number of variables : "))
k = int(input("Enter number of iterations : "))
tau = float(input("Enter cost threshold : "))
learning_rate = float(input("Enter learning rate : "))

n_values = [50, 100, 500, 1000]
theta_values = [0.0, 0.1, 0.2, 0.3]

print("\nResults : ")
print("-" * 70)

for n in n_values:
    for theta in theta_values:

        X, Y, original_beta = generate_data(theta, n, m)
        learned_beta, cost = logistic_regression(X, Y, k, tau, learning_rate)
        beta_error = np.mean(np.abs(original_beta - learned_beta))

        print(f"n = {n}, theta = {theta:.1f}, " f"Beta Error = {beta_error:.4f}")
    print("\n")