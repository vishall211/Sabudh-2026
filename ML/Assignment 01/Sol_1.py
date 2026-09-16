import numpy as np

def make_data(sigma, n, m):
    x = np.random.randn(n, m) # Here i am generating random input values
    x = np.c_[np.ones(n), x]

    beta = np.random.randn(m + 1, 1) # Generating random beta values
    noise = np.random.normal(0, sigma, (n, 1)) # Generating Gaussian noise

    # Calculate y using X, beta and noise
    y = x @ beta + noise
    return x, y, beta


# Example
sigma = 2
n = 100
m = 3

x, y, beta = make_data(sigma, n, m)

print("X : ")
print(x)

print("\nY : ")
print(y)

print("\nBeta : ")
print(beta)