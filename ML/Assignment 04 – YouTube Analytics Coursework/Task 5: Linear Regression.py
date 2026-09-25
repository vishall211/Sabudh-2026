import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

data = pd.read_csv("/Users/vishalsingh/Desktop/SABUDH - 26/ML/Assignment 04 – YouTube Analytics Coursework/USvideos.csv")

data["title_length"] = data["title"].str.len() # Create title length

X = data[["likes", "dislikes", "comment_count", "title_length","channel_title", "category_id"]] # Select features
y = data["views"] # Target

# Encode categorical features
X = pd.get_dummies(X, columns=["channel_title", "category_id"])

# Scaling numeric features
numeric_features = ["likes", "dislikes", "comment_count", "title_length"]

scaler = StandardScaler()
X[numeric_features] = scaler.fit_transform(X[numeric_features])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# Predict views
y_pred = model.predict(X_test)

# Calculating and metrics
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMSE : ", mse)
print("RMSE : ", rmse)
print("MAE : ", mae)
print("R Sqaure : ", r2, "\n")

# Feature coefficients
coefficients = pd.Series(model.coef_, index=X.columns)
coefficients = coefficients.sort_values(ascending=False)

# Plot feature coefficients
plt.figure(figsize=(10, 6))
coefficients.head(10).plot(kind="bar")
plt.title("–– Top 10 Feature Coefficients ––")
plt.xlabel("Features")
plt.ylabel("Coefficient")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Observation: The Linear Regression model achieved an R² score of 0.904, 
# indicating that the model explains approximately 90.4% of the variation in video views. 
# The model’s MAE is approximately 771,226 views.