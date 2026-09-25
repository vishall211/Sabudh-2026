import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression, LogisticRegression

data = pd.read_csv("/Users/vishalsingh/Desktop/SABUDH - 26/ML/Assignment 04 – YouTube Analytics Coursework/USvideos.csv")

# Create required columns
data["title_length"] = data["title"].str.len()

# Creating viral column
threshold = data["views"].quantile(0.75)
data["viral"] = (data["views"] > threshold).astype(int)

X = data[["likes", "dislikes", "comment_count", "title_length","channel_title", "category_id"]]
y_regression = data["views"]
y_classification = data["viral"]

# Encode categorical features
X = pd.get_dummies(X, columns=["channel_title", "category_id"])

# Numeric features
numeric_features = ["likes", "dislikes", "comment_count", "title_length"]

# StandardScaler
standard_scaler = StandardScaler()
X_standard = X.copy()
X_standard[numeric_features] = standard_scaler.fit_transform(X_standard[numeric_features])

# MinMaxScaler
minmax_scaler = MinMaxScaler()
X_minmax = X.copy()
X_minmax[numeric_features] = minmax_scaler.fit_transform(X_minmax[numeric_features])

# Linear Regression - 5 Fold Cross Validation
linear_model = LinearRegression()
linear_scores = cross_val_score(linear_model,X_standard,y_regression,cv=5,scoring="r2")

print("\nLinear Regression Cross-Validation : ")
print("Scores : ", linear_scores)
print("Mean : ", linear_scores.mean())
print("Variance : ", linear_scores.var())

# Logistic Regression - 5 Fold Cross Validation
logistic_model = LogisticRegression(max_iter=1000)
logistic_scores = cross_val_score(logistic_model,X_standard,y_classification,cv=5,scoring="accuracy")

print("\nLogistic Regression Cross-Validation : ")
print("Scores : ", logistic_scores)
print("Mean : ", logistic_scores.mean())
print("Variance : ", logistic_scores.var())

# Scaling comparison
linear_minmax_scores = cross_val_score(linear_model,X_minmax,y_regression,cv=5,scoring="r2")
logistic_minmax_scores = cross_val_score(logistic_model,X_minmax,y_classification,cv=5,scoring="accuracy")

print("\nScaling Comparison : ")
print("StandardScaler - Linear Regression : ", linear_scores.mean())
print("MinMaxScaler - Linear Regression : ", linear_minmax_scores.mean())
print("StandardScaler - Logistic Regression : ", logistic_scores.mean())
print("MinMaxScaler - Logistic Regression : ", logistic_minmax_scores.mean())

# Logistic Regression Feature Importance
logistic_model.fit(X_standard, y_classification)
importance = pd.Series(logistic_model.coef_[0],index=X_standard.columns)
importance = importance.abs().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
importance.plot(kind="bar")
plt.title("Top Features Influencing Virality")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Interpretation : Likes, comment count, and dislikes have the highest influence on virality. 
# Title length has relatively less influence.