# Task 2: Building Regression Models
# Predicting the Market Value of Football Players

# Import required libraries
import os
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression, Lasso, Ridge
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


# Step 4: Handle missing values and prepare data
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


# Step 5: Split the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Step 6: Create regression models
models = {
    "Linear Regression": LinearRegression(),

    "Lasso Regression": Lasso(alpha=1.0),

    "Ridge Regression": Ridge(alpha=1.0),

    "KNN Regression": KNeighborsRegressor(n_neighbors=5),

    "Support Vector Regression": SVR(),

    "Decision Tree Regression": DecisionTreeRegressor(
        random_state=42
    ),

    "Random Forest Regression": RandomForestRegressor(
        n_estimators=100,
        random_state=42
    ),

    "Gradient Boosting Regression": GradientBoostingRegressor(
        random_state=42
    )
}


# Step 7: Train and evaluate all models
results = []

for model_name, model in models.items():

    # Create a pipeline
    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    # Train the model
    pipeline.fit(X_train, y_train)

    # Make predictions
    predictions = pipeline.predict(X_test)

    # Calculate evaluation metrics
    mae = mean_absolute_error(y_test, predictions)

    mse = mean_squared_error(y_test, predictions)

    rmse = np.sqrt(mse)

    r2 = r2_score(y_test, predictions)

    # Store results
    results.append({
        "Model": model_name,
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "R2 Score": r2
    })

    print("\nModel:", model_name)
    print("MAE:", round(mae, 2))
    print("MSE:", round(mse, 2))
    print("RMSE:", round(rmse, 2))
    print("R2 Score:", round(r2, 4))


# Step 8: Compare all models
results_df = pd.DataFrame(results)

results_df = results_df.sort_values(
    by="RMSE",
    ascending=True
)

print("\nFinal Model Comparison:")
print(results_df.to_string(index=False))

# Step 9: Identify the best model
best_model = results_df.iloc[0]

print("\nBest Model:", best_model["Model"])
print("Best RMSE:", round(best_model["RMSE"], 2))
print("Best R2 Score:", round(best_model["R2 Score"], 4))


# Step 10: Save comparison results
import os

folder_path = os.path.dirname(os.path.abspath(__file__))
results_df.to_csv(
    os.path.join(folder_path, "Task_2_Model_Results.csv"),
    index=False
)
print("\nOutput:", "Results saved successfully", "\n")


print("\nInput:", X.shape)
print("Output:", "All 8 regression models trained successfully", "\n")
