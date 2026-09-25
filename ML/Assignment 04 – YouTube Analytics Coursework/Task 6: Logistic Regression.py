import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
    f1_score, roc_auc_score, confusion_matrix, roc_curve
)

data = pd.read_csv("/Users/vishalsingh/Desktop/SABUDH - 26/ML/Assignment 04 – YouTube Analytics Coursework/USvideos.csv")

# Create viral column
threshold = data["views"].quantile(0.75)
data["viral"] = (data["views"] > threshold).astype(int)

data["title_length"] = data["title"].str.len()

X = data[["likes", "dislikes", "comment_count", "title_length","channel_title", "category_id"]] # Select features
y = data["viral"] # Target

# Encode categorical features
X = pd.get_dummies(X, columns=["channel_title", "category_id"])

# Scale numeric features
numeric_features = ["likes", "dislikes", "comment_count", "title_length"]
scaler = StandardScaler()
X[numeric_features] = scaler.fit_transform(X[numeric_features])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Logistic Regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_prob)

print("\nAccuracy : ", accuracy)
print("Precision : ", precision)
print("Recall : ", recall)
print("F1-Score : ", f1)
print("ROC-AUC : ", roc_auc, "\n")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt="d")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

# ROC Curve
fpr, tpr, thresholds = roc_curve(y_test, y_prob)

plt.plot(fpr, tpr)
plt.plot([0, 1], [0, 1], "--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.show()

# Interpretation : I found Likes, dislikes, and comment count have the strongest influence on video virality, 
# while title length has a weaker influence.