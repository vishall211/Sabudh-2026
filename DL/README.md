# 🧠 Deep Learning (DL) & Neural Networks

This directory contains theoretical foundations, mathematical derivations, and architecture implementations for Deep Learning and Artificial Neural Networks completed during the **Sabudh Foundation Data Science Internship (2026)**.

---

## 📁 Directory Structure

```text
DL/
├── Assignment 01/                                      # Multilayer Perceptron (MLP) Foundations
│   ├── B16 MLP Coursework__1778086319-67c994ac8862f33c4e764a16.pdf # Problem statements & network diagram
│   └── Solution – MLP Assignment 01.pdf                # Analytical solutions & gradient derivations
└── README.md                                           # Deep Learning module documentation
```

---

## 🔬 Coursework Overview: Multilayer Perceptron (MLP)

### Architecture Specification
A feedforward neural network comprising:
- **Input Layer**: 3 input nodes ($x_1, x_2, x_3$)
- **Hidden Layer**: 3 hidden neurons ($H_1, H_2, H_3$) with bias $w_{0j}$ and Sigmoid activation
- **Output Layer**: 1 output neuron ($OP$) with bias $w_{0op}$ and Sigmoid activation ($\hat{y}$)

```text
Inputs (3) ──> [Fully Connected: 3x3 weights + 3 biases] ──> Hidden (3) ──> [3x1 weights + 1 bias] ──> Output (1)
```

- **Total Trainable Parameters**:
  $$\text{Parameters} = (3 \times 3 + 3) + (3 \times 1 + 1) = 12 + 4 = 16$$

---

## 📐 Mathematical Derivations

### 1. Forward Propagation Equations
For each hidden neuron $H_j$ ($j \in \{1, 2, 3\}$):
$$z_{H_j} = w_{0j} + \sum_{i=1}^{3} w_{ij} x_i, \quad H_j = \sigma(z_{H_j}) = \frac{1}{1 + e^{-z_{H_j}}}$$

For the output neuron $OP$:
$$z_{op} = w_{0op} + \sum_{j=1}^{3} w_{jop} H_j, \quad \hat{y} = OP = \sigma(z_{op}) = \frac{1}{1 + e^{-z_{op}}}$$

---

### 2. Backpropagation & Gradients with Mean Squared Error (MSE)
Given the loss function for a single instance:
$$L_{\text{MSE}} = (\hat{y} - y)^2$$

Applying the chain rule ($\frac{\partial L}{\partial w} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z} \cdot \frac{\partial z}{\partial w}$), with $\frac{\partial \hat{y}}{\partial z_{op}} = \hat{y}(1 - \hat{y})$:

#### Output Layer Gradients:
- **Output Weights**:
  $$\frac{\partial L}{\partial w_{jop}} = 2(\hat{y} - y) \cdot \hat{y}(1 - \hat{y}) \cdot H_j \quad (j \in \{1, 2, 3\})$$
- **Output Bias**:
  $$\frac{\partial L}{\partial w_{0op}} = 2(\hat{y} - y) \cdot \hat{y}(1 - \hat{y})$$

#### Hidden Layer Gradients ($H_3$):
Backpropagating error into hidden neuron $H_3$ ($\frac{\partial L}{\partial z_{H_3}} = \frac{\partial L}{\partial z_{op}} \cdot w_{3op} \cdot H_3(1 - H_3)$):
- **Input-to-Hidden Weights**:
  $$\frac{\partial L}{\partial w_{i3}} = 2(\hat{y} - y) \cdot \hat{y}(1 - \hat{y}) \cdot w_{3op} \cdot H_3(1 - H_3) \cdot x_i \quad (i \in \{1, 2, 3\})$$
- **Hidden Bias**:
  $$\frac{\partial L}{\partial w_{03}} = 2(\hat{y} - y) \cdot \hat{y}(1 - \hat{y}) \cdot w_{3op} \cdot H_3(1 - H_3)$$

---

### 3. Structural Variations & Loss Function Impact

#### Multiclass Classification Feasibility
- A single Sigmoid output neuron produces scalar probabilities $\hat{y} \in [0, 1]$, restricted to **binary classification**.
- For $K$-class classification, the network requires $K$ output neurons with **Softmax** activation:
  $$P(Y = k \mid x) = \frac{e^{z_k}}{\sum_{j=1}^{K} e^{z_j}}$$

#### Multi-Output Expansion (2 Output Nodes)
- Expanding to two output units ($OP_1, OP_2$) assigns separate incoming weight vectors:
  $$OP_1 = \sigma\left(w_{01op} + \sum_{j=1}^3 w_{j1op} H_j\right), \quad OP_2 = \sigma\left(w_{02op} + \sum_{j=1}^3 w_{j2op} H_j\right)$$

#### Binary Cross-Entropy (BCE) Simplification
Given BCE loss:
$$L_{\text{BCE}} = -[y \log(\hat{y}) + (1 - y) \log(1 - \hat{y})]$$

Computing the derivative with respect to pre-activation $z_{op}$:
$$\frac{\partial L_{\text{BCE}}}{\partial z_{op}} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z_{op}} = \left(-\frac{y}{\hat{y}} + \frac{1 - y}{1 - \hat{y}}\right) \cdot \hat{y}(1 - \hat{y}) = \hat{y} - y$$

The Sigmoid derivative cancels out, yielding simplified, numerically stable gradient equations:
- **Output Weights**: $\frac{\partial L}{\partial w_{jop}} = (\hat{y} - y) \cdot H_j$
- **Output Bias**: $\frac{\partial L}{\partial w_{0op}} = \hat{y} - y$
- **Hidden Weights ($H_3$)**: $\frac{\partial L}{\partial w_{i3}} = (\hat{y} - y) \cdot w_{3op} \cdot H_3(1 - H_3) \cdot x_i$
- **Hidden Bias ($H_3$)**: $\frac{\partial L}{\partial w_{03}} = (\hat{y} - y) \cdot w_{3op} \cdot H_3(1 - H_3)$

