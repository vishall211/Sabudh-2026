# 🎓 Sabudh Foundation — Data Science Internship

[![Python Version](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Academic%20Use-green.svg)](#)
[![Dataiku](https://img.shields.io/badge/Dataiku-Core%20Designer%20Certified-orange.svg)](Dataiku/Core%20Designer%20Certificate.pdf)
[![Machine Learning](https://img.shields.io/badge/Domain-Data%20Science%20%26%20AI-purple.svg)](#)

> Comprehensive repository of coursework, algorithmic problem sets, machine learning pipelines, natural language processing models, relational database architectures, and applied mobility research completed during the **Sabudh Foundation Data Analytics & AI Fellowship (2026)**.

---

## 👨‍💻 Author & Fellow Details
- **Fellow**: Vishal Singh
- **GitHub**: [@vishall211](https://github.com/vishall211)
- **Institution**: Sabudh Foundation
- **Program**: Data Science Internship

---

## 📑 Table of Contents
1. [Repository Architecture](#-repository-architecture)
2. [Module Overviews](#-module-overviews)
   - [1. Python Programming](#1-python-programming)
   - [2. Data Structures & Algorithms (DSA)](#2-data-structures--algorithms-dsa)
   - [3. Machine Learning (ML)](#3-machine-learning-ml)
   - [4. Natural Language Processing (NLP)](#4-natural-language-processing-nlp)
   - [5. Structured Query Language (SQL)](#5-structured-query-language-sql)
   - [6. Passion Project: Digital Twin for Urban Mobility](#6-passion-project-digital-twin-for-urban-mobility)
   - [7. Certifications & Curriculum](#7-certifications--curriculum)
3. [Environment Setup & Installation](#-environment-setup--installation)
4. [How to Run](#-how-to-run)
5. [Tech Stack & Dependencies](#-tech-stack--dependencies)

---

## 🗂 Repository Architecture

```text
SABUDH - 26/
├── Python/                                         # Python Foundations & Data Analysis
│   ├── Assignment 01/                              # Control flow, loops, number & string logic
│   ├── Assignment 02/                              # 3Sum, matrix rotation, Roman numerals
│   ├── Assignment 03/                              # Native data structures (Lists, Tuples, Dicts)
│   ├── Assignment 04/                              # Scientific computing (NumPy & Pandas on sports cars)
│   ├── Assignment 05/                              # Object-Oriented Programming (OOP)
│   └── README.md
│
├── DSA/                                            # Data Structures & Algorithms
│   ├── Assignment 01/                              # Arrays, Prefix Sums, Two-Pointers, Binary Search
│   ├── Assignment 02/                              # Singly Linked Lists (Pointers, Reversal, Math)
│   ├── Assignment 03/                              # Heaps, LRU Cache, Matrices & Linked Lists
│   └── README.md
│
├── ML/                                             # Machine Learning & Applied Analytics
│   ├── Assignment 01 – Linear Regression/          # Multi-variate Linear Regression from scratch
│   ├── Assignment 02 – Logistic Regression/        # Logistic Regression & label flipping simulation
│   ├── Assignment 03 – Bayesian Learning Problem Set/ # Bayesian inference & coursework
│   ├── Assignment 04 – YouTube Analytics Coursework/  # End-to-end Machine Learning pipeline (40k+ videos)
│   ├── Assignment 05 – Model Evaluation/           # Precision, Recall, ROC-AUC & Error Diagnostics
│   ├── linear_algebra_for_machine_learning.md      # Comprehensive Linear Algebra study notes
│   ├── Logistic_Regression.pdf                     # Core classification lecture slides & notes
│   └── README.md
│
├── NLP/                                            # Natural Language Processing & Text Analytics
│   ├── Assignment 01 – Scraping News Articles/     # Indian Express news scraper (BeautifulSoup)
│   ├── Assignment 02 – Question Identification/    # Syntactic & Semantic Question vs Sentence Classification
│   ├── Assignment 03 – Analysing Customer Reviews/ # spaCy NER, Word2Vec, LDA Topic Modeling & Sentiment Classifiers
│   └── README.md
│
├── SQL/                                            # Relational Database Analytics & Modeling
│   ├── Final Coursework/                           # FinanceHub Banking & Financial Services Database
│   │   ├── Financial Services Database.sql         # Schema DDL & comprehensive seed data
│   │   ├── Vishal Singh_FinanceHub_Assignment.sql  # 25 analytical SQL solutions & BI queries
│   │   └── SQL Coursework_ FINANCIAL SERVICES DATABASE.pdf
│   └── README.md
│
├── Passion Project – Digital Twin for Urban Mobility/ # Capstone Research Project
│   ├── Presentations/                              # Literature review slide decks
│   ├── Digital Twin – Resources/                   # Research reports & multi-agent AI notes
│   └── README.md
│
├── Dataiku/                                        # Enterprise Data Science Certifications
│   ├── Core Designer Certificate.pdf               # Verified Dataiku DSS Certificate
│   └── README.md
│
├── DA-Curriculum.pdf                               # Comprehensive Fellowship Syllabus & Roadmap
├── requirements.txt                                # Python package dependencies
├── .gitignore                                      # Production Git ignore patterns
└── README.md                                       # Master repository documentation
```

---

## 📘 Module Overviews

### 1. Python Programming
- **Assignment 01**: Foundational logic using pure control flow (loops, condition branching, manual digit reversing, series calculations, string deduplication).
- **Assignment 02**: Mathematical and array problem-solving (Two-pointer 3Sum, alternating positive/negative arrangement, Roman-integer converter, clockwise matrix rotation).
- **Assignment 03**: Deep dive into native collections (`task1_lists.py`, `task2_tuples.py`, `task3_dictionary.py`).
- **Assignment 04**:
  - `task1_operations_in_numpy.py`: Multidimensional array creation, matrix arithmetic, masking, and aggregation.
  - `task2_pandas.py`: Full data cleaning lifecycle on real-world vehicle data (`1_Sport car price.csv`), summary statistics, category grouping, and cleaned dataset export.
- **Assignment 05**: Advanced OOP design patterns and modular classes.

👉 *Details in [`Python/README.md`](Python/README.md)*

---

### 2. Data Structures & Algorithms (DSA)
- **Assignment 01 (Arrays & Pointers)**:
  - Optimal prefix sum with hash tables for longest subarray sum $K$ in $O(n)$ time.
  - Trapping rainwater with $O(1)$ auxiliary space two-pointer approach.
  - In-place next lexicographical permutation.
  - 2D spiral matrix clockwise unwrapping.
  - Binary search pair matching with `bisect_left`.
- **Assignment 02 (Linked Lists)**:
  - Fast & slow pointer (tortoise & hare) midpoint discovery and deletion.
  - Duplicate elimination in sorted lists.
  - In-place singly linked list reversal.
  - Base-10 arithmetic addition on linked list numbers.
- **Assignment 03 (Advanced Structures & Patterns)**:
  - Product of Array Except Self without division ($O(n)$ time, $O(1)$ space).
  - Staircase 2D matrix search ($O(m + n)$ time).
  - Merge $K$ sorted lists using min-heap priority queue ($O(N \log K)$).
  - LRU Cache with $O(1)$ `get` and `put` operations via `OrderedDict`.
  - Stack-based adjacent duplicate character elimination.

👉 *Details in [`DSA/README.md`](DSA/README.md)*

---

### 3. Machine Learning (ML)
- **Assignment 01 (Linear Regression from Scratch)**:
  - Synthetic data generation with Gaussian noise $\epsilon \sim \mathcal{N}(0, \sigma^2)$.
  - Batch Gradient Descent optimizer minimizing Mean Squared Error (MSE).
  - Empirical report evaluating the effect of sample sizes ($n \in \{50, 500, 5000\}$) and noise standard deviations.
- **Assignment 02 (Logistic Regression & Robustness)**:
  - Sigmoid activation and binary cross-entropy loss.
  - Label noise simulation: Stochastic label-flipping by probability $\theta \in [0, 1]$.
  - Object-Oriented `Regression` class implementation.
- **Assignment 03 (Bayesian Learning)**: Theoretical formulation of Bayes theorem, MAP estimation, and likelihood updating.
- **Assignment 04 (End-to-End YouTube Analytics Project)**:
  - Explores **40,949 trending US YouTube videos**.
  - Formulates predictive targets: continuous `views` and binary `viral` classification (top 25% percentile).
  - Two-sample independent t-tests validating the statistical significance of engagement metrics ($p < 0.05$).
  - Feature engineering (title length, channel encoding, categorical scaling).
  - **Linear Regression**: $R^2 = 0.904$ for view prediction.
  - **Logistic Regression**: $93.77\%$ accuracy, $98.26\%$ ROC-AUC.
  - 5-Fold cross-validation and comparative analysis between `StandardScaler` and `MinMaxScaler`.
- **Assignment 05 (Model Evaluation Diagnostics)**:
  - Rigorous evaluation of precision, recall, specificity, and $F_\beta$ scores under class skew.
  - Decision threshold optimization, ROC-AUC trade-offs, and confusion matrix error decomposition.
- **Foundational Notes**: Detailed tutorial guide on Linear Algebra for Machine Learning (`linear_algebra_for_machine_learning.md`).

👉 *Details in [`ML/README.md`](ML/README.md)*

---

### 4. Natural Language Processing (NLP)
- **Assignment 01 (Automated Web Scraping Pipeline)**:
  - Scrapes news headlines and content dynamically from *The Indian Express*.
  - Extracts clean article bodies using `BeautifulSoup` parsing from the `.story_details` container.
  - Robust error recovery, polite rate limiting, and output persistence to `Vishal_Indian_express_news.csv`.
- **Assignment 02 (Question Identification in Educational Transcripts)**:
  - Preprocesses over 235k lecture transcript utterances into clean text pairs.
  - Benchmarks syntactic (BoW, Word TF-IDF, Character TF-IDF) and semantic (Word2Vec) representations.
  - Evaluates Linear SVM, Logistic Regression, and Naive Bayes classifiers.
  - **Top Benchmark**: **Character TF-IDF + Linear SVM** achieving **0.9912 Accuracy** and **0.9986 ROC-AUC**.
- **Assignment 03 (Customer Reviews & Sentiment Analytics)**:
  - End-to-end analysis on Amazon beauty product customer reviews.
  - spaCy linguistic pipeline with POS filtering (Nouns/Adjectives) and Named Entity Recognition (NER).
  - TF-IDF cosine similarity matrices and continuous Word2Vec embeddings projected into 2D via TruncatedSVD & PCA.
  - Latent Dirichlet Allocation (LDA) topic modeling tuned with Gensim's `CoherenceModel` ($c_v$), word clouds, and topic-specific sentiment distributions.
  - Supervised sentiment classifiers (MultinomialNB, BernoulliNB, Logistic Regression); **Logistic Regression** achieves **0.8524 Accuracy** and **0.9235 ROC-AUC**.

👉 *Details in [`NLP/README.md`](NLP/README.md)*

---

### 5. Structured Query Language (SQL)
- **FinanceHub Banking & Financial Services Database**:
  - Relational schema spanning 11 core banking entities (Customers, Accounts, Transactions, Loans, LoanPayments, CreditCards, CardTransactions, Investments, Employees, Branches, FraudAlerts).
  - **Advanced Querying**: 25 comprehensive analytical queries solving real-world financial operations.
  - **Window Functions**: Running account balances (`FIRST_VALUE` + `SUM OVER`), credit card utilization ranking (`RANK OVER PARTITION`), month-over-month growth (`LAG OVER`), and balance percentile ranks (`PERCENT_RANK OVER`).
  - **Recursive CTEs**: Multi-level employee-manager organizational reporting hierarchies (`WITH RECURSIVE`).
  - **Data Auditing**: Automated detection of negative balances, loan over-extensions, and ledger discrepancies.
  - **Executive BI Dashboard**: Aggregates customer risk tiers, cash flows, card utilization, and loan health into a consolidated KPI report.

👉 *Details in [`SQL/README.md`](SQL/README.md)*

---

### 6. Passion Project: Digital Twin for Urban Mobility
- **Vision**: Designing a multimodal Digital Twin leveraging real-time GTFS transit telemetry and autonomous multi-agent systems to alleviate urban congestion and optimize route scheduling.
- **Deliverables**:
  - Preliminary Research Report.
  - Literature Review Presentation Deck (`.pptx`).
  - Synthesized research notes on AI Agent frameworks and decentralized mobility coordination.

👉 *Details in [`Passion Project – Digital Twin for Urban Mobility/README.md`](Passion%20Project%20%E2%80%93%20Digital%20Twin%20for%20Urban%20Mobility/README.md)*

---

### 7. Certifications & Curriculum
- **Dataiku Core Designer Certificate**: Verified credential demonstrating competency in visual data prep, flow orchestration, exploratory analytics, and machine learning deployments.
- **Fellowship Curriculum (`DA-Curriculum.pdf`)**: Comprehensive program roadmap detailing Python, DSA, Statistics, Machine Learning, and Big Data modules.

👉 *Details in [`Dataiku/README.md`](Dataiku/README.md)*

---

## 🛠 Environment Setup & Installation

### Prerequisites
- Python 3.10+ (Recommended: Python 3.11 or 3.12)
- MySQL 8.0+ (or compatible RDBMS / SQL client such as DBeaver)
- `git`

### Quickstart

1. **Clone the repository**:
   ```bash
   git clone https://github.com/vishall211/Sabudh-2026.git
   cd Sabudh-2026
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # On macOS / Linux:
   python3 -m venv .venv
   source .venv/bin/activate

   # On Windows:
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Download spaCy language model** (for NLP assignments):
   ```bash
   python -m spacy download en_core_web_lg
   ```

---

## 💻 How to Run

### Python & Machine Learning Scripts
```bash
# 1. Run Machine Learning YouTube Analytics
python "ML/Assignment 04 – YouTube Analytics Coursework/Task 01 - Load Dataset & Define Targets.py"

# 2. Run NLP Question Identification
python "NLP/Assignment 02 – Question Identification/Question_Identification.py"

# 3. Run NLP Customer Beauty Reviews Pipeline
python "NLP/Assignment 03 – Analysing Customer Reviews/Beauty_Reviews.py"

# 4. Run DSA LRU Cache / Heap Merging
python "DSA/Assignment 03/Sol_05.py"

# 5. Run Python Pandas Data Cleaning
python "Python/Assignment 04/task2_pandas.py"
```

### SQL Relational Database Queries
```bash
# Initialize FinanceHub database
mysql -u root -p < "SQL/Final Coursework/Financial Services Database.sql"

# Execute assignment solutions
mysql -u root -p FinanceHub < "SQL/Final Coursework/Vishal Singh_FinanceHub_Assignment.sql"
```

---

## 📦 Tech Stack & Dependencies

| Category | Technologies / Libraries |
|---|---|
| **Programming Language** | Python 3.x |
| **Relational Databases & SQL** | MySQL, Window Functions, Recursive CTEs, DDL/DML |
| **Numerical & Data Analysis** | NumPy, Pandas, SciPy |
| **Data Visualization** | Matplotlib, Seaborn, WordCloud |
| **Machine Learning** | Scikit-Learn |
| **Natural Language Processing (NLP)** | spaCy, Gensim |
| **Web Scraping** | Requests, BeautifulSoup4 |
| **Interactive Computing** | Jupyter Notebook, IPython Kernel |
| **Enterprise Platform** | Dataiku DSS |
| **Version Control** | Git, GitHub |
