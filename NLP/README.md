# Natural Language Processing (NLP) & Text Analytics

This directory contains natural language processing pipelines, web crawlers, text vectorization benchmarks, topic models, and sentiment classification systems developed during the **Sabudh Foundation Data Analytics & AI Fellowship (2026)**.

---

## 📁 Directory Structure

```text
NLP/
├── Assignment 01 – Scraping News Articles/
│   ├── sol_01.py                           # Automated web scraper using BeautifulSoup & requests
│   ├── Vishal_Indian_express_news.csv      # Scraped dataset with metadata and full article text
│   └── Scraping News Articles _ B17.pdf    # Assignment problem statement & requirements
│
├── Assignment 02 – Question Identification/
│   ├── Question_Identification.py          # Complete ML pipeline for question vs sentence classification
│   ├── Question_Identification.ipynb       # Interactive notebook with visualizations and ROC analysis
│   ├── Sol_01.py                           # Solution wrapper entrypoint
│   ├── question_identification_model_results.csv # Benchmarked classifier metrics table
│   ├── Data Set _Question Identification.csv # Raw lecture transcripts dataset (235k+ rows)
│   └── Question Identification.pdf         # Coursework problem statement
│
└── Assignment 03 – Analysing Customer Reviews/
    ├── Beauty_Reviews.py                   # End-to-end NLP analysis (spaCy, Word2Vec, LDA, Classifiers)
    ├── Beauty_Reviews.ipynb                # Interactive notebook with WordClouds, PCA, and ROC plots
    ├── beauty_reviews_NLP B02.csv          # Amazon beauty products customer review dataset
    ├── Results_classifier_comparison.csv   # Model comparison (Logistic Regression, BernoulliNB, MNB)
    ├── Results_top_ner_entities.csv        # Top 20 extracted entities and sentiment breakdown
    ├── Results_topic_sentiment_split.csv   # LDA discovered topics with positive/negative percentages
    └── Question.pdf                        # Assignment brief & specifications
```

---

## 🔍 Module Breakdown

### Assignment 01: Indian Express News Web Scraper
- **Objective**: Automate the collection of clean, unstructured news bodies from *The Indian Express* for downstream text mining and NLP pipelines.
- **HTTP Request Management**: Custom headers emulate modern browser sessions to prevent blocking.
- **Targeted Link Extraction**: Evaluates DOM hierarchy (`h1`, `h2`, `h3` tags with `/article/` routing patterns) maintaining a unique set to prevent redundant scraping.
- **Body Extraction**: Targets primary `.story_details` article content containers while stripping boilerplate.
- **Politeness & Fault Tolerance**: Enforces a 1-second delay between queries, graceful timeout/exception handling, and structured export to `Vishal_Indian_express_news.csv`.

---

### Assignment 02: Question Identification in Lecture Transcripts
- **Objective**: Accurately classify educational transcript utterances into binary categories: `question` vs. `sentence`.
- **Text Preprocessing**: Normalization, case folding, deduplication, and label sanitization.
- **Syntactic Representations**:
  - Bag of Words (`CountVectorizer` with unigrams and bigrams).
  - Word-level TF-IDF (`TfidfVectorizer`).
  - Character n-gram TF-IDF (`ngram_range=(2, 5)`).
- **Semantic Representations**:
  - Continuous Word2Vec embeddings trained via Gensim.
  - Mean document vector pooling across tokens.
- **Evaluated Models**: Linear Support Vector Machine (`LinearSVC`), Logistic Regression, and Multinomial Naive Bayes.
- **Key Benchmark Results**:
  | Vectorizer | Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
  |---|---|---|---|---|---|---|
  | **Character TF-IDF** | **Linear SVM** | **0.9912** | **0.9952** | **0.9892** | **0.9922** | **0.9986** |
  | Character TF-IDF | Logistic Regression | 0.9843 | 0.9892 | 0.9832 | 0.9861 | 0.9977 |
  | Bag of Words | Logistic Regression | 0.9821 | 0.9862 | 0.9822 | 0.9842 | 0.9967 |
  | TF-IDF | Linear SVM | 0.9825 | 0.9877 | 0.9815 | 0.9846 | 0.9964 |
  | TF-IDF | Logistic Regression | 0.9811 | 0.9871 | 0.9795 | 0.9833 | 0.9962 |
  | Bag of Words | Linear SVM | 0.9757 | 0.9800 | 0.9772 | 0.9786 | 0.9949 |
  | Word2Vec | Logistic Regression | 0.9621 | 0.9731 | 0.9597 | 0.9664 | 0.9877 |
  | Bag of Words | Naive Bayes | 0.9458 | 0.9592 | 0.9448 | 0.9519 | 0.9887 |
  | TF-IDF | Naive Bayes | 0.9240 | 0.9275 | 0.9397 | 0.9335 | 0.9798 |

---

### Assignment 03: Analysing Customer Beauty Reviews
- **Objective**: Conduct comprehensive exploratory, unsupervised, and supervised NLP analysis on real-world Amazon beauty product reviews.
- **Linguistic Pipeline with spaCy (`en_core_web_lg`)**:
  - POS tag filtering: Filters for `NOUN` and `ADJ` tokens to isolate informative descriptors for topic modeling and vectorization.
  - Lemmatization & Stopword elimination.
  - Named Entity Recognition (NER): Targets `ORG`, `PRODUCT`, `GPE`, and `LOC` entities.
- **Entity Sentiment Analytics**: Aggregates entity occurrences and calculates mean customer sentiment per brand/entity (identifying dominant brands such as Amazon, Norelco, Braun, and Ulta).
- **Document Similarity & Embedding Projections**:
  - Cosine similarity matrices evaluated over TF-IDF space.
  - Continuous Word2Vec document embeddings.
  - 2D dimensionality reduction using TruncatedSVD and PCA colored by sentiment polarity.
- **LDA Topic Modeling & Coherence Optimization**:
  - Gensim Latent Dirichlet Allocation (LDA) models tuned across $K \in \{5, 7, 10\}$ topics.
  - Evaluated using Gensim's `CoherenceModel` ($c_v$ metric) to select the optimal topic count.
  - Generates topic word clouds and assigns interpretable domain labels (e.g., `brush / small / bottle`, `color / nail / product`, `good / quality / great`).
  - Calculates topic-specific sentiment splits (positive vs negative review ratios).
- **Supervised Sentiment Classification**:
  - Classifiers benchmarked: Logistic Regression, Bernoulli Naive Bayes, Multinomial Naive Bayes.
  - Metrics logged: Accuracy, Precision, Recall, F1 Score, and ROC-AUC.
  - **Best Model**: **Logistic Regression** achieving **0.8524 Accuracy** and **0.9235 ROC-AUC**.

---

## 🚀 How to Run

Ensure dependencies are installed and the spaCy language model is downloaded:

```bash
# Install requirements
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_lg
```

Run any assignment script directly from anywhere:

```bash
# 1. Run Indian Express News Scraper
python "NLP/Assignment 01 – Scraping News Articles/sol_01.py"

# 2. Run Question Identification Pipeline
python "NLP/Assignment 02 – Question Identification/Question_Identification.py"

# 3. Run Beauty Reviews NLP Pipeline
python "NLP/Assignment 03 – Analysing Customer Reviews/Beauty_Reviews.py"
```
