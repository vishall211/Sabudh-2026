# Question Identification
# This program identifies whether a lecture sentence is a question or a normal sentence.

import re
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from gensim.models import Word2Vec

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    roc_curve,
    classification_report,
    ConfusionMatrixDisplay
)

# ------------------------------------------------------------------------------------
# 1. Read the dataset
# ------------------------------------------------------------------------------------

file_path = Path(__file__).resolve().parent / "Data Set _Question Identification - Data Set.csv.csv"

df = pd.read_csv(file_path)

print("Original dataset shape:", df.shape)
print(df.head())
print("\nLabel counts:")
print(df["label"].value_counts())


# ------------------------------------------------------------------------------------
# 2. Clean the data
# ------------------------------------------------------------------------------------

# Remove the extra index column
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

# Remove missing and duplicate rows
df = df.dropna(subset=["sentence", "label"])
df = df.drop_duplicates(subset=["sentence", "label"])

df["sentence"] = df["sentence"].astype(str).str.strip()
df["label"] = df["label"].astype(str).str.strip().str.lower()

# Keep only the two required labels
df = df[df["label"].isin(["question", "sentence"])]
df = df[df["sentence"] != ""].copy()

print("\nDataset after cleaning:", df.shape)
print(df["label"].value_counts())


# ------------------------------------------------------------------------------------
# 3. Check the data
# ------------------------------------------------------------------------------------

df["length"] = df["sentence"].apply(lambda text: len(text.split()))

df["label"].value_counts().plot(kind="bar")
plt.title("Number of Questions and Normal Sentences")
plt.xlabel("Label")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

print(df.groupby("label")["length"].describe())


# ------------------------------------------------------------------------------------
# 4. Clean the text
# ------------------------------------------------------------------------------------

# I am keeping question marks because they can help identify questions.
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", " ", text)
    text = re.sub(r"[^a-z0-9\s?!.,']", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


df["clean_sentence"] = df["sentence"].apply(clean_text)

print("\nCleaned sentences:")
print(df[["sentence", "clean_sentence", "label"]].head())


# ------------------------------------------------------------------------------------
# 5. Split the data
# ------------------------------------------------------------------------------------

# Question = 1 and normal sentence = 0
X = df["clean_sentence"]
y = df["label"].map({"sentence": 0, "question": 1})

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining rows:", len(X_train))
print("Testing rows:", len(X_test))


# ------------------------------------------------------------------------------------
# 6. Apply text vectorization
# ------------------------------------------------------------------------------------

vectorizers = {
    "Bag of Words": CountVectorizer(
        max_features=20000,
        ngram_range=(1, 2),
        min_df=2
    ),
    "TF-IDF": TfidfVectorizer(
        max_features=20000,
        ngram_range=(1, 2),
        min_df=2
    ),
    "Character TF-IDF": TfidfVectorizer(
        analyzer="char",
        ngram_range=(3, 5),
        max_features=20000,
        min_df=2
    )
}

features = {}

for name, vectorizer in vectorizers.items():
    print("\nCreating features using:", name)
    train_vec = vectorizer.fit_transform(X_train)
    test_vec = vectorizer.transform(X_test)
    features[name] = (train_vec, test_vec)
    print("Training feature shape:", train_vec.shape)


# ------------------------------------------------------------------------------------
# 7. Train and evaluate classification models
# ------------------------------------------------------------------------------------

results = []
roc_values = {}
models = {}

for vector_name, (x_train_vec, x_test_vec) in features.items():

    model_list = [
        ("Logistic Regression", LogisticRegression(max_iter=300, solver="liblinear")),
        ("Linear SVM", LinearSVC())
    ]

    # Naive Bayes works with non-negative count and TF-IDF features
    if vector_name != "Character TF-IDF":
        model_list.append(("Naive Bayes", MultinomialNB()))

    for model_name, model in model_list:
        print("\nTraining:", vector_name, "-", model_name)
        model.fit(x_train_vec, y_train)

        prediction = model.predict(x_test_vec)

        if hasattr(model, "predict_proba"):
            score = model.predict_proba(x_test_vec)[:, 1]
        else:
            score = model.decision_function(x_test_vec)

        auc = roc_auc_score(y_test, score)

        results.append({
            "Vectorizer": vector_name,
            "Model": model_name,
            "Accuracy": accuracy_score(y_test, prediction),
            "Precision": precision_score(y_test, prediction, zero_division=0),
            "Recall": recall_score(y_test, prediction, zero_division=0),
            "F1 Score": f1_score(y_test, prediction, zero_division=0),
            "ROC-AUC": auc
        })

        model_name_full = vector_name + " + " + model_name
        roc_values[model_name_full] = (roc_curve(y_test, score), auc)
        models[model_name_full] = model

results_df = pd.DataFrame(results).sort_values("ROC-AUC", ascending=False)
print("\nResults of syntactic methods:")
print(results_df.round(4).to_string(index=False))


# ------------------------------------------------------------------------------------
# 8. Plot ROC curves for syntactic methods
# ------------------------------------------------------------------------------------

plt.figure(figsize=(10, 7))

for name, (curve_values, auc) in roc_values.items():
    fpr, tpr, thresholds = curve_values
    plt.plot(fpr, tpr, label=f"{name} (AUC = {auc:.3f})")

plt.plot([0, 1], [0, 1], "--", label="Random model")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curves - Syntactic Methods")
plt.legend(fontsize=8)
plt.grid()
plt.tight_layout()
plt.show()


# ------------------------------------------------------------------------------------
# 9. Semantic vectorization using Word2Vec
# ------------------------------------------------------------------------------------

# Word2Vec learns word vectors using the surrounding words.
def get_words(text):
    return re.findall(r"[a-z0-9]+", text.lower())


train_words = [get_words(text) for text in X_train]
test_words = [get_words(text) for text in X_test]

word_model = Word2Vec(
    sentences=train_words,
    vector_size=100,
    window=5,
    min_count=2,
    workers=4,
    sg=1,
    epochs=5,
    seed=42
)


def make_sentence_vector(words):
    word_vectors = [word_model.wv[word] for word in words if word in word_model.wv]

    if len(word_vectors) == 0:
        return np.zeros(100)

    return np.mean(word_vectors, axis=0)


X_train_w2v = np.array([make_sentence_vector(words) for words in train_words])
X_test_w2v = np.array([make_sentence_vector(words) for words in test_words])

print("\nWord2Vec training shape:", X_train_w2v.shape)
print("Word2Vec testing shape:", X_test_w2v.shape)


# ------------------------------------------------------------------------------------
# 10. Train Logistic Regression using Word2Vec
# ------------------------------------------------------------------------------------

w2v_model = LogisticRegression(max_iter=500)
w2v_model.fit(X_train_w2v, y_train)

w2v_prediction = w2v_model.predict(X_test_w2v)
w2v_score = w2v_model.predict_proba(X_test_w2v)[:, 1]
w2v_auc = roc_auc_score(y_test, w2v_score)

w2v_result = {
    "Vectorizer": "Word2Vec",
    "Model": "Logistic Regression",
    "Accuracy": accuracy_score(y_test, w2v_prediction),
    "Precision": precision_score(y_test, w2v_prediction, zero_division=0),
    "Recall": recall_score(y_test, w2v_prediction, zero_division=0),
    "F1 Score": f1_score(y_test, w2v_prediction, zero_division=0),
    "ROC-AUC": w2v_auc
}

results_df = pd.concat([results_df, pd.DataFrame([w2v_result])], ignore_index=True)
results_df = results_df.sort_values("ROC-AUC", ascending=False)

print("\nFinal model comparison:")
print(results_df.round(4).to_string(index=False))


# ------------------------------------------------------------------------------------
# 11. Plot the Word2Vec ROC curve
# ------------------------------------------------------------------------------------

fpr, tpr, thresholds = roc_curve(y_test, w2v_score)

plt.figure(figsize=(7, 5))
plt.plot(fpr, tpr, label=f"Word2Vec + Logistic Regression (AUC = {w2v_auc:.3f})")
plt.plot([0, 1], [0, 1], "--", label="Random model")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Word2Vec")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()


# ------------------------------------------------------------------------------------
# 12. Select the best model
# ------------------------------------------------------------------------------------

best_result = results_df.iloc[0]
best_name = best_result["Vectorizer"] + " + " + best_result["Model"]

print("\nBest model:", best_name)
print("ROC-AUC:", round(best_result["ROC-AUC"], 4))
print("Accuracy:", round(best_result["Accuracy"], 4))
print("F1 Score:", round(best_result["F1 Score"], 4))

if best_result["Vectorizer"] == "Word2Vec":
    final_model = w2v_model
    final_prediction = w2v_prediction
else:
    final_model = models[best_name]
    best_test_data = features[best_result["Vectorizer"]][1]
    final_prediction = final_model.predict(best_test_data)


# ------------------------------------------------------------------------------------
# 13. Final evaluation
# ------------------------------------------------------------------------------------

print("\nClassification report:")
print(classification_report(
    y_test,
    final_prediction,
    target_names=["sentence", "question"]
))

ConfusionMatrixDisplay.from_predictions(
    y_test,
    final_prediction,
    display_labels=["sentence", "question"]
)
plt.title("Confusion Matrix - Best Model")
plt.tight_layout()
plt.show()


# ------------------------------------------------------------------------------------
# 14. Test the model on new sentences
# ------------------------------------------------------------------------------------

def predict_question(text):
    text = clean_text(text)

    if best_result["Vectorizer"] == "Word2Vec":
        words = get_words(text)
        vector = make_sentence_vector(words).reshape(1, -1)
        prediction = final_model.predict(vector)[0]
    else:
        vectorizer = vectorizers[best_result["Vectorizer"]]
        vector = vectorizer.transform([text])
        prediction = final_model.predict(vector)[0]

    if prediction == 1:
        return "Question"
    return "Normal sentence"


print("\nTesting new sentences:")
print(predict_question("What is machine learning?"))
print(predict_question("Machine learning is a part of artificial intelligence."))


# ------------------------------------------------------------------------------------
# 15. Save the model comparison results
# ------------------------------------------------------------------------------------

output_csv = Path(__file__).resolve().parent / "question_identification_model_results.csv"
results_df.to_csv(output_csv, index=False)
print(f"\nModel results saved to {output_csv.name}")


# Conclusion:
# I cleaned the dataset, applied syntactic and semantic vectorization,trained different classification models and compared them using ROC-AUC. The model with the highest ROC-AUC was selected as the final model.
