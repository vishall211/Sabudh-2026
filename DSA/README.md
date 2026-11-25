# ⚡ Data Structures & Algorithms (DSA)

This directory contains weekly coding challenges, optimal algorithmic problem-solving patterns, and data structure implementations completed during the **Sabudh Foundation Data Science Internship (2026)**.

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
├── Assignment 03/          # Advanced Data Structures, Heaps, Cache & Linked Lists
│   ├── Sol_01.py           # Product of Array Except Self (Prefix/Suffix accumulation)
│   ├── Sol_02.py           # Search a 2D Matrix (O(m + n) staircase search)
│   ├── Sol_03.py           # Add Two Numbers represented as Linked Lists
│   ├── Sol_04.py           # Merge K Sorted Lists (Min-Heap / Priority Queue in O(N log K))
│   ├── Sol_05.py           # LRU Cache implementation (OrderedDict O(1) get/put)
│   ├── Sol_06.py           # Remove Duplicates from Sorted Linked List
│   ├── Sol_07.py           # Count Consistent Strings (Set membership validation)
│   ├── Sol_08.py           # Remove All Adjacent Duplicates in String (LIFO Stack)
│   └── Weekly Code 3 .pdf
│
├── Assignment 04/          # Linked Lists, Bit Manipulation, Kadane's Algorithm & Sparse Vectors
│   ├── Sol_01.py           # Insert a node at the beginning of a Linked List (O(1))
│   ├── Sol_02.py           # Maximum Twin Sum of a Linked List (Equidistant pair sums)
│   ├── Sol_03.py           # Merge Two Sorted Linked Lists (Iterative with dummy head)
│   ├── Sol_04.py           # Single Number III (Bitwise XOR & rightmost set bit partitioning)
│   ├── Sol_05.py           # Dot Product of Two Sparse Vectors (Index-Hash representation)
│   ├── Sol_06.py           # Trapping Rain Water (Two-pointer bounded water computation)
│   ├── Sol_07.py           # Maximum Subarray Sum (Kadane's Algorithm in O(n) time)
│   └── Week_4_coding challenge.pdf
│
├── Assignment 05/          # Linked Lists, Monotonic Stacks, Min Stack & Stack/Queue Design
│   ├── Sol 01.py           # Reverse Linked List II (In-place reversal between bounds left and right)
│   ├── Sol 02.py           # Odd Even Linked List (Reorder nodes by parity of their index in O(1) space)
│   ├── Sol 03.py           # Maximal Rectangle (Largest rectangle in binary matrix via monotonic stack)
│   ├── Sol 04.py           # Min Stack (LIFO stack with O(1) push, pop, top, and getMin)
│   ├── Sol 05.py           # Implement Stack using Queues (LIFO stack using collections.deque)
│   ├── Sol 06.py           # Implement Queue using Stacks (FIFO queue using two stacks with amortized O(1))
│   └── Weekly Code 5 - B16 (1)__1793707486-67c994ac8862f33c4e764a16.pdf
│
├── Assignment 06/          # Linked Lists, Stack Simplification, Greedy & Intervals
│   ├── Sol 01.py           # Remove Nodes From Linked List (Reverse, filter by running max, reverse back)
│   ├── Sol 02.py           # Simplify Path (Unix canonical path using a stack)
│   ├── Sol 03.py           # Jump Game (Greedy max-reach traversal in O(n) time)
│   ├── Sol 04.py           # Merge Intervals (Sort and merge overlapping intervals)
│   ├── Sol 05.py           # Insert Interval (Linear scan to insert and merge into sorted intervals)
│   └── Coding challenge Week 6 - Sabudh Foundation__1794232932-67c994ac8862f33c4e764a16.pdf
│
├── Assignment 07/          # Dynamic Programming, Hash Sets, Binary Search & BST
│   ├── Sol 01.py           # Longest Common Subsequence (2D DP in O(m * n) time)
│   ├── Sol 02.py           # Longest Consecutive Sequence (Hash set in O(n) time)
│   ├── Sol 03.py           # Longest Increasing Subsequence (Binary search tails in O(n log n) time)
│   ├── Sol 04.py           # Check if each internal node of a BST has one child (Preorder O(n) check)
│   ├── Sol 05.py           # Find Smallest Missing Element from Sorted Array (Binary search in O(log n))
│   ├── Sol 06.py           # Edit Distance (2D DP for insert, delete, replace operations)
│   └── Coding challenge Week 7 - B16__1778157037-67c994ac8862f33c4e764a16.pdf
│
└── Assignment 08/          # Binary Trees & Singly Linked Lists
    ├── Sol 01.py           # Maximum Depth of Binary Tree (Recursive DFS)
    ├── Sol 02.py           # Identical Binary Trees (Recursive structure & value comparison)
    ├── Sol 03.py           # Subtree with Given Sum (Post-order subtree sum check)
    ├── Sol 04.py           # SumTree Validation (O(n) bottom-up subtree sum verification)
    ├── Sol 05.py           # Insert Node Before Middle of Linked List (Fast & slow pointers)
    ├── Sol 06.py           # Delete Last Occurrence in Linked List (Single-pass pointer tracking)
    ├── Sol 07.py           # Rotate Linked List Right by k Places (Circular link & break)
    └── Weekly coding challenge - 8 B16__1778568272-67c994ac8862f33c4e764a16.pdf
```

---

## 💡 Algorithmic Concepts & Patterns

### 1. Hash Maps & Prefix Sums
- **Longest Subarray with Sum K (`Assignment 01/Sol 01.py`)**: Uses a hash map to track prefix sums and their first occurrence indices, achieving optimal $O(n)$ time complexity compared to naive $O(n^2)$.
- **Product of Array Except Self (`Assignment 03/Sol_01.py`)**: Computes prefix and postfix product passes directly within the output buffer to solve without division in $O(n)$ time and $O(1)$ auxiliary space.
- **Sparse Vector Dot Product (`Assignment 04/Sol_05.py`)**: Models high-dimensional sparse vectors using dictionary index mappings, computing dot products only over overlapping non-zero entries in $O(\min(L_1, L_2))$ time.

### 2. Two-Pointer & Matrix Traversal
- **Triplets & 3Sum (`Assignment 01/Sol 02.py`, `Sol 03.py`)**: Sorting combined with converging left/right pointers to find target sums while eliminating duplicate results.
- **Trapping Rainwater (`Assignment 01/Sol 04.py`, `Assignment 04/Sol_06.py`)**: Two-pointer approach keeping track of `left_max` and `right_max` to calculate bounded water height in $O(n)$ time and $O(1)$ auxiliary space.
- **Search a 2D Matrix (`Assignment 03/Sol_02.py`)**: Staircase traversal starting from the top-right corner to eliminate a full row or column at each step in $O(m + n)$ time.

### 3. Binary Search & Logarithmic Bounds
- **Successful Pairs of Spells and Potions (`Assignment 01/Sol 07.py`)**: Sorting the potions array and utilizing `bisect_left` logarithmic search to rapidly evaluate matching pairs across extensive arrays.

### 4. Linked List Manipulation
- **Head Insertion (`Assignment 04/Sol_01.py`)**: Direct pointer redirection in $O(1)$ time.
- **Fast & Slow Pointer Pattern (Tortoise & Hare)**: Determining list midpoints and deletion boundaries in a single traversal pass (`Assignment 02/Sol_01.py`, `Sol_02.py`).
- **Pointer Reversal & Merging**: In-place pointer reversal (`Assignment 02/Sol_04.py`) and iterative sorted list merging using a dummy node (`Assignment 04/Sol_03.py`).
- **Equidistant Twin Sums (`Assignment 04/Sol_02.py`)**: Evaluates symmetrical node pairs across the midpoint to compute the maximum twin sum in linear time.
- **List Arithmetic & Carry Propagation**: Emulating base-10 addition with carry handling on linked list digits (`Assignment 02/Sol_06.py`, `Assignment 03/Sol_03.py`).

### 5. Bit Manipulation
- **Single Number III (`Assignment 04/Sol_04.py`)**: Finds two unique numbers among duplicates in $O(n)$ time and $O(1)$ space by taking the cumulative XOR and partitioning elements using the rightmost set bit (`xor & -xor`).

### 6. Dynamic Programming & Greedy
- **Maximum Subarray Sum (`Assignment 04/Sol_07.py`)**: Implements **Kadane's Algorithm** to compute the maximum contiguous subarray sum in a single linear pass ($O(n)$ time and $O(1)$ auxiliary space).

### 7. Priority Queues, Heaps & Caches
- **Merge K Sorted Lists (`Assignment 03/Sol_04.py`)**: Leverages Python's `heapq` module to dynamically extract the minimum node across $K$ linked lists in $O(N \log K)$ time.
- **LRU Cache (`Assignment 03/Sol_05.py`)**: Implements an eviction-ready Least Recently Used cache with $O(1)$ read and write complexity using `collections.OrderedDict`.
- **Stack-based String Reductions (`Assignment 03/Sol_08.py`)**: Evaluates adjacent character equivalence using a LIFO stack to cancel duplicate pairs in linear time.

### 8. Stacks, Queues & Monotonic Data Structures
- **Sublist Reversal & Parity Partitioning (`Assignment 05/Sol 01.py`, `Sol 02.py`)**: In-place reversal of sublists between index bounds and grouping nodes by odd-even index parity in $O(n)$ time and $O(1)$ auxiliary space.
- **Maximal Rectangle (`Assignment 05/Sol 03.py`)**: Converts binary matrix rows into running histogram heights and computes the maximal rectangular area using a monotonic increasing stack in $O(R \times C)$ time.
- **Min Stack (`Assignment 05/Sol 04.py`)**: Tracks running minimums alongside the main stack to achieve $O(1)$ time for push, pop, top, and getMin.
- **Cross-Structure Implementations (`Assignment 05/Sol 05.py`, `Sol 06.py`)**: Implements a LIFO stack using FIFO queues (`deque`) and a FIFO queue using dual LIFO stacks with amortized $O(1)$ push and pop operations.

### 9. Intervals, Greedy & Path Simplification
- **Remove Nodes From Linked List (`Assignment 06/Sol 01.py`)**: Reverses the list, filters out nodes smaller than the running maximum in $O(n)$ time and $O(1)$ space, then reverses back.
- **Simplify Path (`Assignment 06/Sol 02.py`)**: Parses Unix-style directory tokens with a stack to resolve `.` and `..` into a canonical path.
- **Jump Game (`Assignment 06/Sol 03.py`)**: Tracks the furthest reachable index greedily in a single $O(n)$ pass with $O(1)$ space.
- **Merge & Insert Intervals (`Assignment 06/Sol 04.py`, `Sol 05.py`)**: Merges overlapping intervals after sorting ($O(n \log n)$) and inserts a new interval into an already sorted list in a single $O(n)$ pass.

### 10. Dynamic Programming, Trees & Binary Search
- **Longest Common Subsequence & Edit Distance (`Assignment 07/Sol 01.py`, `Sol 06.py`)**: Classic 2D dynamic programming tables solving string subsequence matching and minimum edit operations (insert, delete, replace) in $O(m \cdot n)$ time.
- **Longest Increasing Subsequence (`Assignment 07/Sol 03.py`)**: Maintains a sorted tails array with binary search to compute LIS length in $O(n \log n)$ time.
- **Longest Consecutive Sequence (`Assignment 07/Sol 02.py`)**: Uses a `set` to count consecutive runs only from sequence starting points in $O(n)$ time.
- **BST Preorder & Sorted Missing Element (`Assignment 07/Sol 04.py`, `Sol 05.py`)**: Verifies single-child BST internal nodes in $O(n)$ time and finds the smallest missing non-negative integer in a sorted array via binary search in $O(\log n)$ time.

### 11. Binary Trees & Linked List Operations
- **Tree Depth & Equivalence (`Assignment 08/Sol 01.py`, `Sol 02.py`)**: Computes maximum binary tree depth and checks structural and value equivalence between two trees recursively in $O(n)$ time.
- **Subtree Sums & SumTree (`Assignment 08/Sol 03.py`, `Sol 04.py`)**: Uses bottom-up post-order traversal to detect subtrees matching a target sum and validate SumTree properties in a single $O(n)$ pass.
- **Linked List Insertion, Deletion & Rotation (`Assignment 08/Sol 05.py`, `Sol 06.py`, `Sol 07.py`)**: Inserts a node before the middle via fast/slow pointers, deletes the last occurrence of a key in one pass, and rotates a list right by $k$ places by forming and breaking a cycle.

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
python "DSA/Assignment 03/Sol_05.py"

# Assignment 04
python "DSA/Assignment 04/Sol_03.py"
python "DSA/Assignment 04/Sol_04.py"
python "DSA/Assignment 04/Sol_07.py"

# Assignment 05
python "DSA/Assignment 05/Sol 01.py"
python "DSA/Assignment 05/Sol 03.py"
python "DSA/Assignment 05/Sol 04.py"

# Assignment 06
python "DSA/Assignment 06/Sol 01.py"
python "DSA/Assignment 06/Sol 02.py"
python "DSA/Assignment 06/Sol 04.py"

# Assignment 07
python "DSA/Assignment 07/Sol 01.py"
python "DSA/Assignment 07/Sol 03.py"
python "DSA/Assignment 07/Sol 06.py"

# Assignment 08
python "DSA/Assignment 08/Sol 01.py"
python "DSA/Assignment 08/Sol 04.py"
python "DSA/Assignment 08/Sol 07.py"
```
