import numpy as np

def linear_regression(x, y, iterations, threshold, learning_rate):
    rows, columns = x.shape

    beta = np.random.randn(columns, 1)      # Generating random beta values
    previous_cost = float("inf")

    for i in range(iterations):             # Predicting the output
        predicted_y = x @ beta
        error = predicted_y - y                     # Calculating the error
        cost = np.sum(error ** 2) / (2 * rows)      # Calculating the cost

        # Stop if the change in cost is very small
        if abs(previous_cost - cost) < threshold:
            break
        gradient = (x.T @ error) / rows         # Here i am calculating the gradient
        beta = beta - learning_rate * gradient  # Update beta values
        previous_cost = cost
        
    return beta, cost


# Generate sample data

np.random.seed(10)
n = 100
m = 3
sigma = 2

x = np.random.randn(n, m)
x = np.c_[np.ones(n), x]

original_beta = np.random.randn(m + 1, 1)
noise = np.random.normal(0, sigma, (n, 1))
y = x @ original_beta + noise

# Here i am training the model.

iterations = 1000
threshold = 0.000001
learning_rate = 0.01

learned_beta, final_cost = linear_regression(x, y, iterations, threshold, learning_rate)

print("Original Beta : ", original_beta)
print("\nLearned Beta : ", learned_beta)
print("\nFinal Cost : ", final_cost)
