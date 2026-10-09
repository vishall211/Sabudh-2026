# ⚡ Data Structures & Algorithms (DSA)

This directory contains weekly coding challenges and algorithmic implementations completed during the **Sabudh Foundation Data Analytics & AI Fellowship (2026)**.

---

## 📁 Directory Structure

```text
DSA/
├── Assignment 01/          # Arrays, Two Pointers, Sliding Window & Binary Search
│   ├── Sol 01.py           # Longest subarray with sum K (Hash Map prefix sum)
│   ├── Sol 02.py           # Maximum product of a triplet in an array
│   ├── Sol 03.py           # 3Sum: Triplet sum to target with two-pointer technique
│   ├── Sol 04.py           # Trapping Rain Water (Two-pointer optimal O(n) time, O(1) space)
│   ├── Sol 05.py           # Next Permutation (Lexicographical rearrangement)
│   ├── Sol 06.py           # Spiral Matrix traversal
│   ├── Sol 07.py           # Successful pairs of spells and potions (Binary Search)
│   └── Weekly coding challenge - 1.pdf
│
└── Assignment 02/          # Singly Linked List Data Structures & Algorithms
    ├── Sol_01.py           # Find middle node of linked list (Fast & Slow pointers)
    ├── Sol_02.py           # Delete middle node of linked list
    ├── Sol_03.py           # Remove duplicate elements from sorted linked list
    ├── Sol_04.py           # Reverse singly linked list in-place
    ├── Sol_05.py           # Add 1 to a number represented as linked list
    ├── Sol_06.py           # Add two numbers represented as linked lists
    ├── Sol_07.py           # Find the second-last node in a linked list
    └── Weekly Code 2.pdf
```

---

## 💡 Algorithmic Concepts & Patterns

### 1. Hash Maps & Prefix Sums
- **Longest Subarray with Sum K (`Sol 01.py`)**: Uses a hash map to track prefix sums and their first occurrence indices, achieving an optimal $O(n)$ time complexity compared to naive $O(n^2)$.

### 2. Two-Pointer & Sliding Window
- **Triplets & 3Sum (`Sol 02.py`, `Sol 03.py`)**: Sorting combined with converging left/right pointers to find target sums while eliminating duplicate results.
- **Trapping Rainwater (`Sol 04.py`)**: Two-pointer approach keeping track of `left_max` and `right_max` to calculate bounded water height in $O(n)$ time and $O(1)$ auxiliary space.

### 3. Binary Search
- **Successful Pairs of Spells and Potions (`Sol 07.py`)**: Sorting the potions array and utilizing `bisect_left` logarithmic search to rapidly evaluate matching pairs across extensive arrays.

### 4. Linked List Manipulation
- **Fast & Slow Pointer Pattern (Tortoise & Hare)**: Determining list midpoints and deletion boundaries in a single traversal pass.
- **Pointer Reversal**: Reversing pointers in-place without auxiliary list allocation.
- **List Arithmetic**: Emulating base-10 addition with carry handling on linked list digits.

---

## 🚀 How to Run

Execute any algorithm solution directly:

```bash
python "DSA/Assignment 01/Sol 01.py"
python "DSA/Assignment 02/Sol_01.py"
```

