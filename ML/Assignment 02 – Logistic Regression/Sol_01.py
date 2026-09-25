import numpy as np

def generate_data(theta, n, m):

    # Here i am generting random coefficients
    beta = np.random.randn(m)

    # First column is for the intercept
    X = np.ones((n, m))

    if m > 1:
        X[:, 1:] = np.random.randn(n, m - 1)

    # Here i am calculating probabilities
    z = X @ beta
    probability = 1 / (1 + np.exp(-z))

    # Generate binary labels
    Y = np.random.binomial(1, probability).reshape(-1, 1)

    # Flip labels according to theta
    flip = np.random.binomial(1, theta, size=(n, 1))
    Y = np.where(flip == 1, 1 - Y, Y)

    return X, Y, beta


theta = float(input("\nEnter theta : "))
n = int(input("Enter the size of dataset (n) : "))
m = int(input("Enter the number of variables (m) : "))

X, Y, beta = generate_data(theta, n, m)

print("\nX : ",X)
print("\nY : ", Y)
print("\nBeta : ", beta, "\n")

