import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_csv("/Users/vishalsingh/Desktop/SABUDH - 26/ML/Assignment 04 – YouTube Analytics Coursework/USvideos.csv")

data["title_length"] = data["title"].str.len() # Create title length

# Select features
X = data[["likes", "dislikes", "comment_count", "title_length","channel_title", "category_id"]]
y = data["views"] # Target

# Convert categorical columns into numbers
X = pd.get_dummies(X, columns=["channel_title", "category_id"])

# Scaling numeric features
numeric_features = ["likes", "dislikes", "comment_count", "title_length"]
scaler = StandardScaler()
X[numeric_features] = scaler.fit_transform(X[numeric_features])

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\nTraining data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)
print("\nPreprocessed data:")
print(X_train.head(),"\n")