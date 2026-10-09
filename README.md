# 🎓 Sabudh Foundation — Data Sciecne Internship

[![Python Version](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Academic%20Use-green.svg)](#)
[![Dataiku](https://img.shields.io/badge/Dataiku-Core%20Designer%20Certified-orange.svg)](Dataiku/Core%20Designer%20Certificate.pdf)
[![Machine Learning](https://img.shields.io/badge/Domain-Data%20Science%20%26%20AI-purple.svg)](#)

> Comprehensive repository of coursework, algorithmic problem sets, machine learning pipelines, natural language processing scrapers, and applied mobility research completed during the **Sabudh Foundation Data Analytics & AI Fellowship (2026)**.

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
   - [5. Passion Project: Digital Twin for Urban Mobility](#5-passion-project-digital-twin-for-urban-mobility)
   - [6. Certifications & Curriculum](#6-certifications--curriculum)
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
│   └── README.md
│
├── ML/                                             # Machine Learning & Applied Analytics
│   ├── Assignment 01 – Linear Regression/          # Multi-variate Linear Regression from scratch
│   ├── Assignment 02 – Logistic Regression/        # Logistic Regression & label flipping simulation
│   ├── Assignment 03 – Bayesian Learning Problem Set/ # Bayesian inference & coursework
│   ├── Assignment 04 – YouTube Analytics Coursework/  # End-to-end Machine Learning pipeline (40k+ videos)
│   ├── linear_algebra_for_machine_learning.md      # Comprehensive Linear Algebra study notes
│   ├── Logistic_Regression.pdf                     # Core classification lecture slides & notes
│   └── README.md
│
├── NLP/                                            # Natural Language Processing & Scraping
│   ├── Assignment 01 – Scraping News Articles/     # Indian Express news scraper (BeautifulSoup)
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
- **Foundational Notes**: Detailed tutorial guide on Linear Algebra for Machine Learning (`linear_algebra_for_machine_learning.md`).

👉 *Details in [`ML/README.md`](ML/README.md)*

---

### 4. Natural Language Processing (NLP)
- **Assignment 01 (Automated Web Scraping Pipeline)**:
  - Scrapes news headlines and content dynamically from *The Indian Express*.
  - Extracts clean article bodies using `BeautifulSoup` parsing from the `.story_details` container.
  - Robust error recovery, rate limiting, and output persistence to `Vishal_Indian_express_news.csv`.

👉 *Details in [`NLP/README.md`](NLP/README.md)*

---

### 5. Passion Project: Digital Twin for Urban Mobility
- **Vision**: Designing a multimodal Digital Twin leveraging real-time GTFS transit telemetry and autonomous multi-agent systems to alleviate urban congestion and optimize route scheduling.
- **Deliverables**:
  - Preliminary Research Report (17 Sep 2026).
  - Literature Review Presentation Deck (`.pptx`).
  - Synthesized research notes on AI Agent frameworks and decentralized mobility coordination.

👉 *Details in [`Passion Project – Digital Twin for Urban Mobility/README.md`](Passion%20Project%20%E2%80%93%20Digital%20Twin%20for%20Urban%20Mobility/README.md)*

---

### 6. Certifications & Curriculum
- **Dataiku Core Designer Certificate**: Verified credential demonstrating competency in visual data prep, flow orchestration, exploratory analytics, and machine learning deployments.
- **Fellowship Curriculum (`DA-Curriculum.pdf`)**: Comprehensive program roadmap detailing Python, DSA, Statistics, Machine Learning, and Big Data modules.

👉 *Details in [`Dataiku/README.md`](Dataiku/README.md)*

---

## 🛠 Environment Setup & Installation

### Prerequisites
- Python 3.10+ (Recommended: Python 3.11 or 3.12 / 3.13)
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

---

## 💻 How to Run

All scripts utilize portable dynamic relative pathing, allowing them to be run either from the repository root or directly from their respective subdirectories:

```bash
# 1. Run YouTube Analytics Task 01
python "ML/Assignment 04 – YouTube Analytics Coursework/Task 01 - Load Dataset & Define Targets.py"

# 2. Run Linear Regression from Scratch
python "ML/Assignment 01 – Linear Regression/Sol_1.py"

# 3. Run DSA Linked List Middle Element Finder
python "DSA/Assignment 02/Sol_01.py"

# 4. Run Python Pandas Data Cleaning & Aggregation
python "Python/Assignment 04/task2_pandas.py"
```

---

## 📦 Tech Stack & Dependencies

| Category | Technologies / Libraries |
|---|---|
| **Programming Language** | Python 3.x |
| **Numerical & Data Analysis** | NumPy, Pandas, SciPy |
| **Data Visualization** | Matplotlib, Seaborn |
| **Machine Learning** | Scikit-Learn |
| **Web Scraping & NLP** | Requests, BeautifulSoup4 |
| **Enterprise Platform** | Dataiku DSS |
| **Version Control** | Git, GitHub |

