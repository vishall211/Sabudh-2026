# Task 5: Genetic Algorithm for KNN Feature Weighting
# Predicting the Market Value of Football Players

# Import required libraries
import os
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


# Step 1: Load the dataset
folder_path = os.path.dirname(os.path.abspath(__file__))
data = pd.read_csv(os.path.join(folder_path, "Data set__1682565729-62fcaa4ea2bc0b6439d2306a.csv"))

# Convert FPL selection percentage into numeric values
data["fpl_sel"] = data["fpl_sel"].str.replace("%", "", regex=False)
data["fpl_sel"] = pd.to_numeric(data["fpl_sel"])


# Step 2: Select features and target
features = [
    "age",
    "position",
    "club",
    "page_views",
    "fpl_value",
    "fpl_sel",
    "fpl_points",
    "region",
    "new_foreign",
    "big_club",
    "new_signing"
]

numerical_columns = [
    "age",
    "page_views",
    "fpl_value",
    "fpl_sel",
    "fpl_points",
    "region",
    "new_foreign",
    "big_club",
    "new_signing"
]

categorical_columns = [
    "position",
    "club"
]

X = data[features]
y = data["market_value"].to_numpy()


# Step 3: Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Further divide training data for GA
X_ga, X_validation, y_ga, y_validation = train_test_split(
    X_train,
    y_train,
    test_size=0.2,
    random_state=42
)


# Step 4: Calculate distance between players
def build_distance_matrix(reference_data, compare_data):

    distance_list = []

    for column in features:

        if column in numerical_columns:

            # Fill missing values using training median
            median_value = reference_data[column].median()

            reference_values = reference_data[column].fillna(
                median_value
            ).astype(float).to_numpy()

            compare_values = compare_data[column].fillna(
                median_value
            ).astype(float).to_numpy()

            # Normalize numerical values
            minimum = reference_values.min()
            maximum = reference_values.max()

            difference = maximum - minimum

            if difference == 0:
                difference = 1

            reference_values = (
                reference_values - minimum
            ) / difference

            compare_values = (
                compare_values - minimum
            ) / difference

            # Calculate numerical distance
            distance = np.abs(
                compare_values[:, None] -
                reference_values[None, :]
            )

        else:

            # Fill missing categorical values
            most_common = reference_data[column].mode().iloc[0]

            reference_values = reference_data[column].fillna(
                most_common
            ).astype(str).to_numpy()

            compare_values = compare_data[column].fillna(
                most_common
            ).astype(str).to_numpy()

            # Calculate categorical distance
            distance = (
                compare_values[:, None] !=
                reference_values[None, :]
            ).astype(float)

        distance_list.append(distance)

    return np.stack(distance_list, axis=2)


# Step 5: Create weighted KNN prediction function
def knn_prediction(distance_matrix, target_values, weights, k=5):

    # Apply attribute weights to distances
    weighted_distance = np.sum(
        distance_matrix * weights.reshape(1, 1, -1),
        axis=2
    ) / (weights.sum() + 1e-10)

    predictions = []

    for i in range(len(weighted_distance)):

        # Find the nearest K players
        nearest_indices = np.argpartition(
            weighted_distance[i],
            k - 1
        )[:k]

        # Calculate average market value
        predicted_value = np.mean(
            target_values[nearest_indices]
        )

        predictions.append(predicted_value)

    return np.array(predictions)


# Step 6: Prepare validation distances
validation_distances = build_distance_matrix(
    X_ga,
    X_validation
)


# Step 7: Define fitness function
def calculate_fitness(weights):

    predictions = knn_prediction(
        validation_distances,
        y_ga,
        weights,
        k=5
    )

    rmse = np.sqrt(
        mean_squared_error(y_validation, predictions)
    )

    return rmse


# Step 8: Initialize Genetic Algorithm
np.random.seed(42)

population_size = 30
generations = 40
number_of_features = len(features)

# Generate random attribute weights
population = np.random.rand(
    population_size,
    number_of_features
)

best_weights = None
best_fitness = float("inf")


# Step 9: Run Genetic Algorithm
for generation in range(generations):

    # Calculate fitness of each individual
    fitness_values = np.array([
        calculate_fitness(individual)
        for individual in population
    ])

    # Find the best individual
    best_index = np.argmin(fitness_values)

    if fitness_values[best_index] < best_fitness:

        best_fitness = fitness_values[best_index]

        best_weights = population[best_index].copy()

    # Sort population by fitness
    sorted_indices = np.argsort(fitness_values)

    # Keep the best two individuals
    new_population = [
        population[sorted_indices[0]].copy(),
        population[sorted_indices[1]].copy()
    ]

    # Tournament selection
    def selection():

        candidates = np.random.choice(
            population_size,
            3,
            replace=False
        )

        winner = candidates[
            np.argmin(fitness_values[candidates])
        ]

        return population[winner]

    # Crossover and mutation
    while len(new_population) < population_size - 4:

        parent1 = selection()
        parent2 = selection()

        # Uniform crossover
        mask = np.random.rand(number_of_features) < 0.5

        child = np.where(mask, parent1, parent2).copy()

        # Mutation
        if np.random.rand() < 0.3:

            random_index = np.random.randint(
                number_of_features
            )

            child[random_index] += np.random.normal(0, 0.15)

            # Keep weights between 0 and 1
            child = np.clip(child, 0, 1)

        # Avoid all-zero weights
        if child.sum() < 1e-8:

            child[np.random.randint(number_of_features)] = 0.5

        new_population.append(child)

    # Step 10: Diversity maintenance
    # Introduce four random individuals in every generation

    for i in range(4):

        new_individual = np.random.rand(
            number_of_features
        )

        new_population.append(new_individual)

    population = np.array(new_population)

    # Display progress
    if (generation + 1) % 10 == 0:

        print(
            "Generation:",
            generation + 1,
            "Best RMSE:",
            round(best_fitness, 4)
        )


# Step 11: Find the final best individual
final_fitness = np.array([
    calculate_fitness(individual)
    for individual in population
])

final_index = np.argmin(final_fitness)

if final_fitness[final_index] < best_fitness:

    best_fitness = final_fitness[final_index]

    best_weights = population[final_index].copy()


# Step 12: Display learned attribute weights
weights_df = pd.DataFrame({
    "Attribute": features,
    "Weight": best_weights
})

print("\nLearned Attribute Weights:")
print(weights_df.to_string(index=False))

print("\nBest Validation RMSE:", round(best_fitness, 4))


# Step 13: Prepare test distances
test_distances = build_distance_matrix(
    X_train,
    X_test
)


# Step 14: Predict using normal KNN
normal_weights = np.ones(number_of_features)

normal_predictions = knn_prediction(
    test_distances,
    y_train,
    normal_weights,
    k=5
)


# Step 15: Predict using GA Weighted KNN
ga_predictions = knn_prediction(
    test_distances,
    y_train,
    best_weights,
    k=5
)


# Step 16: Evaluate both models
normal_mae = mean_absolute_error(
    y_test,
    normal_predictions
)

normal_rmse = np.sqrt(
    mean_squared_error(y_test, normal_predictions)
)

normal_r2 = r2_score(
    y_test,
    normal_predictions
)


ga_mae = mean_absolute_error(
    y_test,
    ga_predictions
)

ga_rmse = np.sqrt(
    mean_squared_error(y_test, ga_predictions)
)

ga_r2 = r2_score(
    y_test,
    ga_predictions
)


# Step 17: Compare both models
comparison = pd.DataFrame({
    "Model": [
        "Normal KNN",
        "GA Weighted KNN"
    ],

    "MAE": [
        normal_mae,
        ga_mae
    ],

    "RMSE": [
        normal_rmse,
        ga_rmse
    ],

    "R2 Score": [
        normal_r2,
        ga_r2
    ]
})

print("\nModel Comparison:")
print(comparison.to_string(index=False))


# Step 18: Save results
folder_path = os.path.dirname(
    os.path.abspath(__file__)
)

weights_df.to_csv(
    os.path.join(folder_path, "Task_5_Attribute_Weights.csv"),
    index=False
)

comparison.to_csv(
    os.path.join(folder_path, "Task_5_Model_Comparison.csv"),
    index=False
)


# Final output
print("\nInput:", X.shape)
print("Output:", "Genetic Algorithm completed successfully", "\n")
