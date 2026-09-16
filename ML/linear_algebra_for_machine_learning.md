# Linear Algebra for Machine Learning

## Learning Approach

We will learn **one concept at a time**, from absolute beginner level.

The goal is **not** to become a mathematician. The goal is to understand enough linear algebra to understand how Machine Learning works.

---

# Lesson 1 — What is Linear Algebra?

## 1. What is Algebra?

Algebra is working with **numbers and variables**.

For example:

$$
2x + 5 = 15
$$

We find:

$$
x = 5
$$

---

## 2. What is Linear Algebra?

**Linear Algebra is the mathematics of vectors, matrices, and linear relationships.**

For Machine Learning, think of it like this:

> **Linear Algebra gives us a way to represent data using numbers and perform calculations on that data.**

That's why Machine Learning needs it.

---

## 3. Why does Machine Learning need Linear Algebra?

Imagine you want to predict house prices.

| House | Size | Bedrooms | Age |
|---|---:|---:|---:|
| A | 1000 | 2 | 10 |
| B | 1500 | 3 | 5 |
| C | 2000 | 4 | 2 |

A computer can represent one house as:

$$
[1000, 2, 10]
$$

Another house:

$$
[1500, 3, 5]
$$

All houses together:

$$
\begin{bmatrix}
1000 & 2 & 10\\
1500 & 3 & 5\\
2000 & 4 & 2
\end{bmatrix}
$$

This introduces the basic objects of linear algebra:

**Vector → Matrix**

These are used everywhere in Machine Learning.

---

## 4. What does "Linear" mean?

A linear relationship is one where things change in a consistent way.

For example:

$$
y = 2x
$$

If:

$$
x = 1 \rightarrow y = 2
$$

$$
x = 2 \rightarrow y = 4
$$

$$
x = 3 \rightarrow y = 6
$$

For now, you do not need to study the strict mathematical definition of linearity.

---

## 5. The Three Basic Things You Need to Know

### 1. Scalar

A **single number**.

Examples:

```text
5
10
-2
0.5
```

### 2. Vector

A **collection of numbers**.

```text
[10, 20, 30]
```

### 3. Matrix

A **collection of vectors arranged in rows and columns**.

```text
[10  20  30]
[40  50  60]
```

Later, you may learn about **tensors**, especially in Deep Learning.

But not yet.

---

## 6. Why Learn This Before Machine Learning?

Eventually, you may see something like:

$$
y = Xw + b
$$

The goal is not to memorize it right now.

Eventually, you should be able to think:

> "X might be a matrix, w might be a vector, and this calculation produces a prediction."

You do not need to become a mathematician.

You need to understand **what the mathematics is doing**.

---

## 7. First Mental Model

Remember this:

```text
Real World
    ↓
Data
    ↓
Numbers
    ↓
Vectors / Matrices
    ↓
Mathematical Operations
    ↓
ML Model
    ↓
Prediction
```

Example:

```text
House
 ↓
[1500, 3, 5]
 ↓
Vector
 ↓
Mathematical calculation
 ↓
ML model
 ↓
₹80 lakh prediction
```

---

# Lesson 2 — Scalar

## 1. What is a Scalar?

A **scalar is simply a single number**.

Examples:

$$
5
$$

$$
-10
$$

$$
3.14
$$

$$
0.5
$$

That's all.

> **Scalar = one numerical value**

---

## 2. Scalar vs Vector vs Matrix

### Scalar

```text
5
```

### Vector

```text
[5, 10, 15]
```

### Matrix

```text
[5   10]
[15  20]
```

So:

- **Scalar** → One number
- **Vector** → Collection of numbers
- **Matrix** → Numbers arranged in rows and columns

---

## 3. Scalars in Machine Learning

Scalars are everywhere in Machine Learning.

Example:

```python
learning_rate = 0.01
```

`0.01` is a scalar.

Another example:

```python
age = 22
```

`22` is a scalar.

Another:

```python
prediction = 85.5
```

`85.5` is a scalar.

Whenever you see a **single numerical value**, it is a scalar.

---

## 4. Basic Scalar Operations

### Addition

$$
5 + 3 = 8
$$

### Subtraction

$$
5 - 3 = 2
$$

### Multiplication

$$
5 \times 3 = 15
$$

### Division

$$
\frac{5}{2} = 2.5
$$

---

## 5. Scalar Multiplication

This becomes important when we study vectors.

Suppose:

$$
x = [2, 4, 6]
$$

Multiply it by the scalar:

$$
3
$$

Then:

$$
3x = [6, 12, 18]
$$

Step by step:

```text
3 × [2, 4, 6]

= [3×2, 3×4, 3×6]

= [6, 12, 18]
```

We multiply **every element** of the vector by the scalar.

---

## 6. Real Machine Learning Examples

Suppose a model predicts:

$$
prediction = 75
$$

`75` is a scalar.

Suppose the model's error is:

$$
error = 5
$$

`5` is a scalar.

Suppose:

$$
learning\ rate = 0.01
$$

`0.01` is a scalar.

Scalar simply means **one number used in a mathematical calculation**.

---

## 7. Key Takeaways

Remember:

1. **Scalar = a single number**
2. Scalars can be added, subtracted, multiplied, and divided.
3. In Machine Learning, scalars can represent:
   - Learning rate
   - Error
   - Prediction
   - Age
   - A single numerical value

---

# Next Topic — Vector

We will learn:

- What exactly is a vector?
- Why Machine Learning uses vectors
- Vector dimensions
- Components/elements
- Vector representation
- Simple vector operations
- Real Machine Learning examples

We will continue adding each new lesson to this learning path.
