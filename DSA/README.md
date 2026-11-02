# ⚡ Data Structures & Algorithms (DSA)

This directory contains weekly coding challenges, optimal algorithmic problem-solving patterns, and data structure implementations completed during the **Sabudh Foundation Data Analytics & AI Fellowship (2026)**.

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
├── Assignment 02/          # Singly Linked List Data Structures & Algorithms
│   ├── Sol_01.py           # Find middle node of linked list (Fast & Slow pointers)
│   ├── Sol_02.py           # Delete middle node of linked list
│   ├── Sol_03.py           # Remove duplicate elements from sorted linked list
│   ├── Sol_04.py           # Reverse singly linked list in-place
│   ├── Sol_05.py           # Add 1 to a number represented as linked list
│   ├── Sol_06.py           # Add two numbers represented as linked lists
│   ├── Sol_07.py           # Find the second-last node in a linked list
│   └── Weekly Code 2.pdf
│
└── Assignment 03/          # Advanced Data Structures, Heaps, Cache & Linked Lists
    ├── Sol_01.py           # Product of Array Except Self (Prefix/Suffix accumulation)
    ├── Sol_02.py           # Search a 2D Matrix (O(m + n) staircase search)
    ├── Sol_03.py           # Add Two Numbers represented as Linked Lists
    ├── Sol_04.py           # Merge K Sorted Lists (Min-Heap / Priority Queue in O(N log K))
    ├── Sol_05.py           # LRU Cache implementation (OrderedDict O(1) get/put)
    ├── Sol_06.py           # Remove Duplicates from Sorted Linked List
    ├── Sol_07.py           # Count Consistent Strings (Set membership validation)
    ├── Sol_08.py           # Remove All Adjacent Duplicates in String (LIFO Stack)
    └── Weekly Code 3 .pdf
```

---

## 💡 Algorithmic Concepts & Patterns

### 1. Hash Maps & Prefix Sums
- **Longest Subarray with Sum K (`Assignment 01/Sol 01.py`)**: Uses a hash map to track prefix sums and their first occurrence indices, achieving optimal $O(n)$ time complexity compared to naive $O(n^2)$.
- **Product of Array Except Self (`Assignment 03/Sol_01.py`)**: Computes prefix and postfix product passes directly within the output buffer to solve the problem without division in $O(n)$ time and $O(1)$ auxiliary space.

### 2. Two-Pointer & Matrix Traversal
- **Triplets & 3Sum (`Assignment 01/Sol 02.py`, `Sol 03.py`)**: Sorting combined with converging left/right pointers to find target sums while eliminating duplicate results.
- **Trapping Rainwater (`Assignment 01/Sol 04.py`)**: Two-pointer approach keeping track of `left_max` and `right_max` to calculate bounded water height in $O(n)$ time and $O(1)$ auxiliary space.
- **Search a 2D Matrix (`Assignment 03/Sol_02.py`)**: Staircase traversal starting from the top-right corner to eliminate a full row or column at each step in $O(m + n)$ time.

### 3. Binary Search & Logarithmic Bounds
- **Successful Pairs of Spells and Potions (`Assignment 01/Sol 07.py`)**: Sorting the potions array and utilizing `bisect_left` logarithmic search to rapidly evaluate matching pairs across extensive arrays.

### 4. Linked List Manipulation
- **Fast & Slow Pointer Pattern (Tortoise & Hare)**: Determining list midpoints and deletion boundaries in a single traversal pass (`Assignment 02/Sol_01.py`, `Sol_02.py`).
- **Pointer Reversal**: Reversing pointers in-place without auxiliary list allocation (`Assignment 02/Sol_04.py`).
- **List Arithmetic & Carry Propagation**: Emulating base-10 addition with carry handling on linked list digits (`Assignment 02/Sol_06.py`, `Assignment 03/Sol_03.py`).
- **In-Place Duplicate Removal**: Skipping adjacent duplicate values in sorted lists (`Assignment 02/Sol_03.py`, `Assignment 03/Sol_06.py`).

### 5. Priority Queues, Heaps & Caches
- **Merge K Sorted Lists (`Assignment 03/Sol_04.py`)**: Leverages Python's `heapq` module to dynamically extract the minimum node across $K$ linked lists in $O(N \log K)$ time.
- **LRU Cache (`Assignment 03/Sol_05.py`)**: Implements an eviction-ready Least Recently Used cache with $O(1)$ read and write complexity using `collections.OrderedDict`.
- **Stack-based String Reductions (`Assignment 03/Sol_08.py`)**: Evaluates adjacent character equivalence using a LIFO stack to cancel duplicate pairs in linear time.

---

## 🚀 How to Run

Execute any algorithm solution directly:

```bash
# Assignment 01
python "DSA/Assignment 01/Sol 01.py"

# Assignment 02
python "DSA/Assignment 02/Sol_01.py"

# Assignment 03
python "DSA/Assignment 03/Sol_01.py"
python "DSA/Assignment 03/Sol_04.py"
python "DSA/Assignment 03/Sol_05.py"
```
