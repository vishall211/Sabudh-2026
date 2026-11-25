# Task 4: Model Selection
# Predicting the Market Value of Football Players

# Import required libraries
import os
import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split, KFold, cross_val_score
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


# Step 6: Define cross-validation
kfold = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)


# Step 7: Create regression models
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


# Step 8: Perform 5-Fold Cross-Validation
results = []

best_rmse = float("inf")
best_model = None
best_model_name = ""

for model_name, model in models.items():

    print("\nEvaluating Model:", model_name)

    # Create pipeline
    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    # Calculate cross-validation RMSE
    scores = cross_val_score(
        pipeline,
        X_train,
        y_train,
        cv=kfold,
        scoring="neg_root_mean_squared_error",
        n_jobs=-1
    )

    # Convert negative RMSE into positive RMSE
    rmse_scores = -scores

    average_rmse = rmse_scores.mean()

    # Store results
    results.append({
        "Model": model_name,
        "Average CV RMSE": average_rmse,
        "Standard Deviation": rmse_scores.std()
    })

    print("Fold RMSE Scores:", np.round(rmse_scores, 2))
    print("Average RMSE:", round(average_rmse, 2))

    # Select the model with lowest average RMSE
    if average_rmse < best_rmse:

        best_rmse = average_rmse
        best_model = pipeline
        best_model_name = model_name


# Step 9: Compare all models
results_df = pd.DataFrame(results)

results_df = results_df.sort_values(
    by="Average CV RMSE",
    ascending=True
)

print("\nFinal Model Selection Results:")
print(results_df.to_string(index=False))


# Step 10: Train the selected model
best_model.fit(X_train, y_train)

# Predict using test data
predictions = best_model.predict(X_test)


# Step 11: Evaluate the selected model
mae = mean_absolute_error(y_test, predictions)

mse = mean_squared_error(y_test, predictions)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, predictions)

print("\nSelected Model:", best_model_name)

print("Test MAE:", round(mae, 2))
print("Test MSE:", round(mse, 2))
print("Test RMSE:", round(rmse, 2))
print("Test R2 Score:", round(r2, 4))


# Step 12: Save results and selected model
folder_path = os.path.dirname(os.path.abspath(__file__))

results_df.to_csv(
    os.path.join(folder_path, "Task_4_Model_Selection.csv"),
    index=False
)

joblib.dump(
    best_model,
    os.path.join(folder_path, "Task_4_Best_Model.pkl")
)

print("\nInput:", X.shape)
print("Output:", "Model selection completed successfully", "\n")
