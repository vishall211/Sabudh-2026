
# Task 3: Hyperparameter Tuning
# Predicting the Market Value of Football Players

# Import required libraries
import os
import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import Lasso, Ridge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


# Step 1: Load the dataset
folder_path = os.path.dirname(os.path.abspath(__file__))
data = pd.read_csv(os.path.join(folder_path, "Data set__1682565729-62fcaa4ea2bc0b6439d2306a.csv"))

# Convert FPL selection percentage into numeric values
data["fpl_sel"] = data["fpl_sel"].str.replace("%", "", regex=False)
data["fpl_sel"] = pd.to_numeric(data["fpl_sel"])


# Step 2: Select input features
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

X = data[features]

# Target variable
y = data["market_value"]


# Step 3: Separate numerical and categorical columns
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


# Step 4: Prepare the data
numerical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", numerical_pipeline, numerical_columns),
    ("cat", categorical_pipeline, categorical_columns)
])


# Step 5: Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Step 6: Define regression models and parameters
models = {
    "Lasso Regression": {
        "model": Lasso(max_iter=10000),
        "parameters": {
            "model__alpha": [0.01, 0.1, 1, 10, 100]
        }
    },

    "Ridge Regression": {
        "model": Ridge(),
        "parameters": {
            "model__alpha": [0.01, 0.1, 1, 10, 100]
        }
    },

    "KNN Regression": {
        "model": KNeighborsRegressor(),
        "parameters": {
            "model__n_neighbors": [3, 5, 7, 9, 11],
            "model__weights": ["uniform", "distance"]
        }
    },

    "Support Vector Regression": {
        "model": SVR(),
        "parameters": {
            "model__C": [1, 10, 50, 100],
            "model__epsilon": [0.1, 0.2, 0.5],
            "model__kernel": ["linear", "rbf"]
        }
    },

    "Decision Tree Regression": {
        "model": DecisionTreeRegressor(random_state=42),
        "parameters": {
            "model__max_depth": [None, 5, 10, 15],
            "model__min_samples_split": [2, 5, 10],
            "model__min_samples_leaf": [1, 2, 4]
        }
    },

    "Random Forest Regression": {
        "model": RandomForestRegressor(random_state=42),
        "parameters": {
            "model__n_estimators": [100, 200, 300],
            "model__max_depth": [None, 5, 10],
            "model__min_samples_split": [2, 5],
            "model__min_samples_leaf": [1, 2]
        }
    },

    "Gradient Boosting Regression": {
        "model": GradientBoostingRegressor(random_state=42),
        "parameters": {
            "model__n_estimators": [100, 200],
            "model__learning_rate": [0.01, 0.05, 0.1],
            "model__max_depth": [2, 3, 4]
        }
    }
}


# Step 7: Perform hyperparameter tuning
results = []

best_score = float("inf")
best_model = None
best_model_name = ""

for model_name, model_details in models.items():

    print("\nTuning Model:", model_name)

    # Create pipeline
    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", model_details["model"])
    ])

    # Apply GridSearchCV
    grid_search = GridSearchCV(
        estimator=pipeline,
        param_grid=model_details["parameters"],
        cv=5,
        scoring="neg_root_mean_squared_error",
        n_jobs=-1
    )

    # Train the model
    grid_search.fit(X_train, y_train)

    # Get the best model
    tuned_model = grid_search.best_estimator_

    # Predict using test data
    predictions = tuned_model.predict(X_test)

    # Calculate evaluation metrics
    mae = mean_absolute_error(y_test, predictions)

    mse = mean_squared_error(y_test, predictions)

    rmse = np.sqrt(mse)

    r2 = r2_score(y_test, predictions)

    # Store results
    results.append({
        "Model": model_name,
        "Best Parameters": str(grid_search.best_params_),
        "CV RMSE": -grid_search.best_score_,
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "R2 Score": r2
    })

    print("Best Parameters:", grid_search.best_params_)
    print("Best CV RMSE:", round(-grid_search.best_score_, 2))
    print("Test MAE:", round(mae, 2))
    print("Test RMSE:", round(rmse, 2))
    print("Test R2 Score:", round(r2, 4))

    # Select the model with the lowest CV RMSE
    if -grid_search.best_score_ < best_score:

        best_score = -grid_search.best_score_
        best_model = tuned_model
        best_model_name = model_name


# Step 8: Compare tuned models
results_df = pd.DataFrame(results)

results_df = results_df.sort_values(
    by="RMSE",
    ascending=True
)

print("\nFinal Tuned Model Comparison:")
print(results_df.to_string(index=False))


# Step 9: Display the best model
print("\nBest Tuned Model:", best_model_name)
print("Best Cross Validation RMSE:", round(best_score, 2))

# Evaluate the selected model on test data
best_predictions = best_model.predict(X_test)

best_rmse = np.sqrt(
    mean_squared_error(y_test, best_predictions)
)

best_r2 = r2_score(y_test, best_predictions)

print("Final Test RMSE:", round(best_rmse, 2))
print("Final Test R2 Score:", round(best_r2, 4))


# Step 10: Save results and trained model
folder_path = os.path.dirname(os.path.abspath(__file__))

results_df.to_csv(
    os.path.join(folder_path, "Task_3_Tuned_Results.csv"),
    index=False
)

joblib.dump(
    best_model,
    os.path.join(folder_path, "Task_3_Best_Model.pkl")
)

print("\nInput:", X.shape)
print("Output:", "Hyperparameter tuning completed successfully", "\n")
