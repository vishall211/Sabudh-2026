# 🤖 Machine Learning Coursework & Projects

This directory contains foundational mathematical notes, from-scratch algorithmic implementations, and an end-to-end applied data science project completed as part of the **Sabudh Foundation Data Analytics & AI Fellowship (2026)**.

---

## 📁 Directory Structure

```text
ML/
├── Assignment 01 – Linear Regression/           # Linear Regression from Scratch
│   ├── Sol_1.py                                # Synthetic data generation with Gaussian noise
│   ├── Sol_2.py                                # Gradient descent & cost function convergence
│   ├── Sol_3.py                                # Empirical experiment report (Sample size & noise impact)
│   └── Linear regression_Assignment.pdf
│
├── Assignment 02 – Logistic Regression/         # Logistic Regression & Classification
│   ├── Sol_01.py                               # Probabilistic binary data generation with Sigmoid
│   ├── Sol_02.py                               # Binary cross-entropy loss & gradient descent
│   ├── Sol_03.py                               # Noise simulation: Label flipping with parameter theta
│   ├── Sol_04.py                               # Evaluating model stability under noise
│   ├── Sol_05.py                               # Object-Oriented Regression class implementation
│   └── Logistic Regression _ B16 Coursework.pdf
│
├── Assignment 03 – Bayesian Learning Problem Set/
│   └── Bayesian - Coursework.pdf               # Bayesian inference and probability theory
│
├── Assignment 04 – YouTube Analytics Coursework/ # End-to-End Real World Machine Learning Project
│   ├── Task 01 - Load Dataset & Define Targets.py
│   ├── Task 02 - Distributions and Relationships.py
│   ├── Task 03 - Hypothesis Testing.py
│   ├── Task 04 - Preprocess Features.py
│   ├── Task 05 - Linear Regression.py
│   ├── Task 06 - Logistic Regression.py
│   ├── Task 07 - Cross-Validation and Scaling Comparison.py
│   ├── Task 08 - Report & Insights.py
│   ├── USvideos.csv                            # US YouTube Trending dataset (40,949 records)
│   └── Youtube Analytics.pdf
│
├── linear_algebra_for_machine_learning.md       # Comprehensive study guide on Linear Algebra for ML
└── Logistic_Regression.pdf                     # Core concepts presentation & notes
```

---

## 🔬 Assignments In Detail

### Assignment 01: Multi-variate Linear Regression (From Scratch)
- **Mathematical Data Generation**: Generates synthetic feature matrices $X \in \mathbb{R}^{n \times (m+1)}$ with an added bias/intercept column, true parameter vector $\beta$, and Gaussian noise $\epsilon \sim \mathcal{N}(0, \sigma^2)$.
- **Gradient Descent Optimization**: Implements batch gradient descent minimizing Mean Squared Error (MSE):
  $$\nabla_\beta J(\beta) = \frac{1}{n} X^T (X\beta - y)$$
- **Empirical Sensitivity Analysis**: Evaluates parameter recovery precision across dataset sizes ($n \in \{50, 500, 5000\}$) and varying noise standard deviations ($\sigma$).

### Assignment 02: Logistic Regression & Noise Robustness
- **Sigmoid Activation**: Maps linear predictions into probabilistic bounds: $\sigma(z) = \frac{1}{1 + e^{-z}}$.
- **Binary Cross-Entropy Loss**: Optimizes the log-loss cost function via gradient updates.
- **Label Flipping Simulation**: Simulates real-world sensor/label noise by stochastically flipping target labels $Y$ with probability $\theta \in [0, 1]$ and quantifies decision boundary degradation.
- **OOP Architecture**: Encapsulates model behavior inside an extensible `Regression` class (`fit`, `predict`, `cost_function`, `gradient`).

### Assignment 03: Bayesian Learning Problem Set
- Formal study of Bayesian prior-likelihood updates, maximum a posteriori (MAP) estimation, and Naive Bayes formulations.

### Assignment 04: End-to-End YouTube Analytics Project
An applied machine learning workflow conducted on over 40,000 trending YouTube videos:
1. **Target Definitions**: Continuous prediction of `views` and classification of `viral` videos (top 75th percentile).
2. **Exploratory Data Analysis**: Log transforms, distributions, engagement correlations (likes, dislikes, comments).
3. **Statistical Hypothesis Testing**: Two-sample independent t-tests (`scipy.stats.ttest_ind`) proving statistically significant view disparities between high and low engagement tiers ($p < 0.05$).
4. **Feature Engineering & Preprocessing**: Title length feature extraction, one-hot encoding for channel and categories, and standard scaling.
5. **Linear Regression**: Achieved an $R^2$ score of **0.904** in predicting total video views.
6. **Logistic Regression**: Achieved **93.77% accuracy** and **98.26% ROC-AUC** for viral classification.
7. **Cross-Validation & Scaling Study**: 5-fold cross-validation benchmarking `StandardScaler` against `MinMaxScaler`.
8. **Business Intelligence Report**: Practical creator and marketing recommendations derived from quantitative insights.

---

## 🚀 How to Run

```bash
# Run Linear Regression from scratch
python "ML/Assignment 01 – Linear Regression/Sol_1.py"

# Run YouTube Analytics Task 01
python "ML/Assignment 04 – YouTube Analytics Coursework/Task 01 - Load Dataset & Define Targets.py"
```

