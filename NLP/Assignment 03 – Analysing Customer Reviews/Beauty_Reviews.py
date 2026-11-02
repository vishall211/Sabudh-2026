# Analysing Customer Reviews using NLP

# ------------------------------------------------------------------
# 1. Importing the libraries needed for thiss assignment
# ------------------------------------------------------------------

import warnings
warnings.filterwarnings("ignore")
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import spacy

from wordcloud import WordCloud
from gensim.models import Word2Vec, LdaModel, CoherenceModel
from gensim.corpora import Dictionary

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD, PCA
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, roc_curve, classification_report,
    ConfusionMatrixDisplay
)

# ------------------------------------------------------------------
# 2. Setting the random state and dataset file name
# ------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
RANDOM_STATE = 42
DATA_FILE = SCRIPT_DIR / "beauty_reviews_NLP B02 - beauty_reviews.csv"


# ------------------------------------------------------------------
# 3. Cleaning the dataset
# ------------------------------------------------------------------

def clean_dataset(data):
    data = data.dropna(subset=["review_text", "sentiment"]).copy()
    data["review_text"] = data["review_text"].astype(str).str.strip()
    data["sentiment"] = data["sentiment"].astype(int)

    data = data[data["review_text"] != ""]
    data = data[data["sentiment"].isin([0, 1])]
    data = data.drop_duplicates(subset=["review_text", "sentiment"])

    return data.reset_index(drop=True)


# ------------------------------------------------------------------
# 4. Preparing the two types of text for NLP
# ------------------------------------------------------------------

def preprocess_reviews(data, nlp):
    pos_tokens_list = []
    w2v_tokens_list = []
    entity_list = []

    for doc in nlp.pipe(data["review_text"].tolist(), batch_size=64):
        pos_tokens = []
        w2v_tokens = []

        for token in doc:
            if token.is_space or token.is_punct or token.is_stop:
                continue

            if token.is_alpha:
                word = token.lemma_.lower().strip()

                if word:
                    w2v_tokens.append(word)

                    if token.pos_ in ["NOUN", "ADJ"]:
                        pos_tokens.append(word)

        # NER is done on the original review text.
        entities = []
        for ent in doc.ents:
            if ent.label_ in ["ORG", "PRODUCT", "GPE", "LOC"]:
                if ent.text.strip():
                    entities.append((ent.text.strip(), ent.label_))

        pos_tokens_list.append(pos_tokens)
        w2v_tokens_list.append(w2v_tokens)
        entity_list.append(entities)

    data = data.copy()
    data["pos_tokens"] = pos_tokens_list
    data["w2v_tokens"] = w2v_tokens_list
    data["entities"] = entity_list

    return data


# ------------------------------------------------------------------
# 5. Finding named entities and checking their sentiment
# ------------------------------------------------------------------

def analyse_entities(data):
    entity_rows = []

    for review_id, row in data.iterrows():
        seen_entities = set()

        for name, entity_type in row["entities"]:
            key = (name.lower(), entity_type)

            if key not in seen_entities:
                entity_rows.append({
                    "entity_key": name.lower(),
                    "entity": name,
                    "entity_type": entity_type,
                    "sentiment": row["sentiment"],
                    "review_id": review_id
                })
                seen_entities.add(key)

    entity_data = pd.DataFrame(entity_rows)

    if entity_data.empty:
        print("No matching entities were found by spaCy.")
        return entity_data, pd.DataFrame(
            columns=["entity", "mentions", "mean_sentiment"]
        )

    entity_summary = (
        entity_data.groupby("entity_key", as_index=False)
        .agg(
            entity=("entity", "first"),
            mentions=("review_id", "nunique"),
            mean_sentiment=("sentiment", "mean")
        )
        .sort_values("mentions", ascending=False)
    )

    top_entities = entity_summary.head(20)

    plt.figure(figsize=(12, 7))
    sns.barplot(data=top_entities, x="mentions", y="entity")
    plt.title("Top 20 Mentioned Entities")
    plt.xlabel("Number of reviews")
    plt.ylabel("Entity")
    plt.tight_layout()
    plt.show()

    return entity_data, top_entities


# ------------------------------------------------------------------
# 6. Converting the reviews into TF-IDF vectors
# ------------------------------------------------------------------

def create_tfidf(data):
    pos_text = data["pos_tokens"].apply(lambda words: " ".join(words))

    vectorizer = TfidfVectorizer(max_features=10000, min_df=2)
    matrix = vectorizer.fit_transform(pos_text)

    return vectorizer, matrix, pos_text


# 7. Checking how similar the reviews are
def plot_similarity(data, matrix):
    sample_size = min(50, len(data))
    sample_ids = data.sample(
        n=sample_size, random_state=RANDOM_STATE
    ).index

    sample_matrix = matrix[sample_ids]
    similarity = cosine_similarity(sample_matrix)

    labels = data.loc[sample_ids, "sentiment"].map(
        {1: "Positive", 0: "Negative"}
    )

    plt.figure(figsize=(12, 10))
    sns.heatmap(
        similarity,
        cmap="YlGnBu",
        xticklabels=labels.tolist(),
        yticklabels=labels.tolist()
    )
    plt.title("Cosine Similarity of 50 Reviews")
    plt.xlabel("Sentiment")
    plt.ylabel("Sentiment")
    plt.xticks(rotation=90, fontsize=7)
    plt.yticks(rotation=0, fontsize=7)
    plt.tight_layout()
    plt.show()

    sentiment_values = data.loc[sample_ids, "sentiment"].to_numpy()
    same_scores = []
    different_scores = []

    for i in range(sample_size):
        for j in range(i + 1, sample_size):
            if sentiment_values[i] == sentiment_values[j]:
                same_scores.append(similarity[i, j])
            else:
                different_scores.append(similarity[i, j])

    print("Average similarity for same sentiment:", np.mean(same_scores))
    print("Average similarity for different sentiment:", np.mean(different_scores))


# ------------------------------------------------------------------
# 8. Creating Word2Vec vectors for the reviews
# ------------------------------------------------------------------

def create_word2vec(data):
    sentences = data["w2v_tokens"].tolist()

    model = Word2Vec(
        sentences=sentences,
        vector_size=100,
        window=5,
        min_count=2,
        workers=4,
        sg=1,
        epochs=10,
        seed=RANDOM_STATE
    )

    document_vectors = []

    for words in sentences:
        vectors = [
            model.wv[word] for word in words
            if word in model.wv
        ]

        if vectors:
            document_vectors.append(np.mean(vectors, axis=0))
        else:
            document_vectors.append(np.zeros(100))

    return model, np.array(document_vectors)


# ------------------------------------------------------------------
# 9. Reducing the vectors to 2D and plotting them
# ------------------------------------------------------------------

def plot_embeddings(tfidf_matrix, word2vec_vectors, sentiments):
    # SVD reduces TF-IDF before PCA.
    components = min(50, tfidf_matrix.shape[1] - 1)
    tfidf_reduced = TruncatedSVD(
        n_components=components,
        random_state=RANDOM_STATE
    ).fit_transform(tfidf_matrix)

    tfidf_2d = PCA(n_components=2).fit_transform(tfidf_reduced)
    w2v_2d = PCA(n_components=2).fit_transform(word2vec_vectors)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    axes[0].scatter(
        tfidf_2d[:, 0], tfidf_2d[:, 1],
        c=sentiments, cmap="coolwarm", alpha=0.6
    )
    axes[0].set_title("TF-IDF (SVD + PCA)")
    axes[0].set_xlabel("Component 1")
    axes[0].set_ylabel("Component 2")

    axes[1].scatter(
        w2v_2d[:, 0], w2v_2d[:, 1],
        c=sentiments, cmap="coolwarm", alpha=0.6
    )
    axes[1].set_title("Word2Vec (PCA)")
    axes[1].set_xlabel("Component 1")
    axes[1].set_ylabel("Component 2")

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------------
# 10. Training LDA models and comparing their coherence scores
# ------------------------------------------------------------------

def train_lda_models(data):
    token_lists = data["pos_tokens"].tolist()

    dictionary = Dictionary(token_lists)
    dictionary.filter_extremes(no_below=2, no_above=0.95)
    corpus = [dictionary.doc2bow(words) for words in token_lists]

    models = {}
    scores = []

    for k in [5, 7, 10]:
        print("Training LDA with", k, "topics")

        model = LdaModel(
            corpus=corpus,
            id2word=dictionary,
            num_topics=k,
            random_state=RANDOM_STATE,
            passes=10,
            alpha="auto",
            eta="auto"
        )

        coherence_model = CoherenceModel(
            model=model,
            texts=token_lists,
            dictionary=dictionary,
            coherence="c_v"
        )

        coherence = coherence_model.get_coherence()
        models[k] = model
        scores.append({
            "Number of Topics": k,
            "Coherence": coherence
        })

    coherence_df = pd.DataFrame(scores)
    best_k = int(
        coherence_df.loc[coherence_df["Coherence"].idxmax(), "Number of Topics"]
    )

    return dictionary, corpus, models, coherence_df, models[best_k], best_k


# ------------------------------------------------------------------
# 11. Showing the topics with their important words
# ------------------------------------------------------------------

def show_topics_and_wordclouds(model, number_of_topics):
    topic_words = {}

    fig, axes = plt.subplots(
        number_of_topics, 1,
        figsize=(10, number_of_topics * 3)
    )

    if number_of_topics == 1:
        axes = [axes]

    for topic_id in range(number_of_topics):
        words = dict(model.show_topic(topic_id, topn=15))
        topic_words[topic_id] = words

        print(f"Topic {topic_id + 1}:", ", ".join(words.keys()))

        cloud = WordCloud(
            width=900,
            height=350,
            background_color="white"
        ).generate_from_frequencies(words)

        axes[topic_id].imshow(cloud, interpolation="bilinear")
        axes[topic_id].axis("off")
        axes[topic_id].set_title(f"Topic {topic_id + 1}")

    plt.tight_layout()
    plt.show()

    return topic_words


# ------------------------------------------------------------------
# 12. Checking positive and negative reviews in each topic
# ------------------------------------------------------------------

def analyse_topic_sentiment(data, model, corpus, topic_labels):
    dominant_topics = []

    for bow in corpus:
        topic_probs = model.get_document_topics(
            bow, minimum_probability=0
        )
        dominant_topic = max(topic_probs, key=lambda item: item[1])[0]
        dominant_topics.append(dominant_topic)

    result = data[["sentiment"]].copy()
    result["topic_id"] = dominant_topics
    result["topic_label"] = result["topic_id"].map(topic_labels)

    topic_sentiment = pd.crosstab(
        result["topic_label"],
        result["sentiment"],
        normalize="index"
    ) * 100

    topic_sentiment = topic_sentiment.rename(
        columns={0: "Negative %", 1: "Positive %"}
    )

    return result, topic_sentiment



# ------------------------------------------------------------------
# 13. Splitting the data and preparing it for classification
# ------------------------------------------------------------------

def prepare_classifier_data(data):
    X_train_text, X_test_text, y_train, y_test = train_test_split(
        data["pos_tokens"].apply(lambda words: " ".join(words)),
        data["sentiment"],
        test_size=0.20,
        random_state=42,
        stratify=data["sentiment"]
    )

    vectorizer = TfidfVectorizer(max_features=10000, min_df=2)
    X_train = vectorizer.fit_transform(X_train_text)
    X_test = vectorizer.transform(X_test_text)

    return vectorizer, X_train, X_test, y_train, y_test


# ------------------------------------------------------------------
# 14. Training and comparing the three classification models
# ------------------------------------------------------------------

def train_classifiers(X_train, X_test, y_train, y_test):
    models = {
        "MultinomialNB": MultinomialNB(),
        "BernoulliNB": BernoulliNB(),
        "Logistic Regression": LogisticRegression(max_iter=500)
    }

    results = []
    roc_data = {}
    trained_models = {}

    for name, model in models.items():
        print("Training", name)
        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        scores = model.predict_proba(X_test)[:, 1]

        results.append({
            "Model": name,
            "Accuracy": accuracy_score(y_test, predictions),
            "Precision": precision_score(
                y_test, predictions, zero_division=0
            ),
            "Recall": recall_score(
                y_test, predictions, zero_division=0
            ),
            "F1 Score": f1_score(
                y_test, predictions, zero_division=0
            ),
            "AUC": roc_auc_score(y_test, scores)
        })

        roc_data[name] = roc_curve(y_test, scores)
        trained_models[name] = model

    results_df = pd.DataFrame(results).sort_values(
        "AUC", ascending=False
    )

    return results_df, roc_data, trained_models


# ------------------------------------------------------------------
# 15. Running all the steps in the correct order
# ------------------------------------------------------------------

def main():
    # Loading the dataset
    df = pd.read_csv(DATA_FILE)

    print("Dataset shape:", df.shape)
    print(df.head())
    print("\nMissing values:\n", df.isnull().sum())
    print("\nSentiment counts:\n", df["sentiment"].value_counts())

    df = clean_dataset(df)
    print("\nDataset after cleaning:", df.shape)
    print(df["sentiment"].value_counts())

    nlp = spacy.load("en_core_web_lg")
    df = preprocess_reviews(df, nlp)

    print("\nSample processed reviews:")
    print(df[["review_text", "pos_tokens", "w2v_tokens", "entities"]].head())

    # Finding brands, products and locations in the reviews
    entity_data, top_entities = analyse_entities(df)
    print("\nTop entities:")
    print(top_entities)

    # Creating TF-IDF vectors and checking review similarity
    tfidf_vectorizer, tfidf_matrix, pos_text = create_tfidf(df)
    print("\nTF-IDF matrix shape:", tfidf_matrix.shape)

    plot_similarity(df, tfidf_matrix)

    # Creating Word2Vec vectors and plotting both embeddings
    word2vec_model, word2vec_vectors = create_word2vec(df)
    print("\nWord2Vec document vectors:", word2vec_vectors.shape)

    plot_embeddings(
        tfidf_matrix,
        word2vec_vectors,
        df["sentiment"].to_numpy()
    )

    # Training LDA models and selecting the best number of topics
    dictionary, corpus, lda_models, coherence_df, best_lda, best_k = (
        train_lda_models(df)
    )

    print("\nLDA coherence scores:")
    print(coherence_df)
    print("Best number of topics:", best_k)

    plt.figure(figsize=(7, 5))
    plt.plot(
        coherence_df["Number of Topics"],
        coherence_df["Coherence"],
        marker="o"
    )
    plt.xlabel("Number of topics")
    plt.ylabel("Coherence score (c_v)")
    plt.title("LDA Coherence Comparison")
    plt.xticks([5, 7, 10])
    plt.grid()
    plt.tight_layout()
    plt.show()

    # Displaying the topics and their word clouds
    topic_words = show_topics_and_wordclouds(best_lda, best_k)

    # These keyword labels can be renamed after checking the topic words.
    topic_labels = {
        topic_id: " / ".join(list(words.keys())[:3])
        for topic_id, words in topic_words.items()
    }

    print("\nTopic labels:")
    print(topic_labels)

    # Checking the sentiment split for each topic
    topic_results, topic_sentiment = analyse_topic_sentiment(
        df, best_lda, corpus, topic_labels
    )

    print("\nSentiment split for each topic:")
    print(topic_sentiment.round(2))

    # Preparing the data for the classification models
    classifier_vectorizer, X_train, X_test, y_train, y_test = (
        prepare_classifier_data(df)
    )

    print("\nTraining rows:", X_train.shape[0])
    print("Testing rows:", X_test.shape[0])

    # Training the models and comparing their performance
    classifier_results, roc_data, trained_models = train_classifiers(
        X_train, X_test, y_train, y_test
    )

    print("\nClassifier comparison:")
    print(classifier_results.round(4))

    plt.figure(figsize=(8, 6))

    for name, (fpr, tpr, thresholds) in roc_data.items():
        auc_value = classifier_results.loc[
            classifier_results["Model"] == name, "AUC"
        ].iloc[0]

        plt.plot(
            fpr, tpr,
            label=f"{name} (AUC = {auc_value:.3f})"
        )

    plt.plot([0, 1], [0, 1], "--", label="Random classifier")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curves - Sentiment Classification")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

    # Showing the results of the best model
    best_model_name = classifier_results.iloc[0]["Model"]
    best_classifier = trained_models[best_model_name]
    best_predictions = best_classifier.predict(X_test)

    print("\nBest model:", best_model_name)
    print(classification_report(
        y_test,
        best_predictions,
        target_names=["Negative", "Positive"]
    ))

    ConfusionMatrixDisplay.from_predictions(
        y_test,
        best_predictions,
        display_labels=["Negative", "Positive"]
    )
    plt.title("Confusion Matrix")
    plt.tight_layout()
    plt.show()

    # Saving the final results as CSV files
    classifier_results.to_csv(SCRIPT_DIR / "Results_classifier_comparison.csv", index=False)
    top_entities.to_csv(SCRIPT_DIR / "Results_top_ner_entities.csv", index=False)
    topic_sentiment.to_csv(SCRIPT_DIR / "Results_topic_sentiment_split.csv")

    print("\nAll result files have been saved.")


if __name__ == "__main__":
    main()
