import numpy as np
import pandas as pd

# Answer 01 : Numpy array creation and manipulation
def create_arrays():
    num1 = np.random.randint(0, 100, 10)
    num2 = np.random.randint(-10, 11, (3, 4))
    flat_num2 = num2.flatten()
    
    num1_copy = num1.copy()
    num1_copy[0] = -1
    every_second = num1[::2]

    return num1, num2, flat_num2, num1_copy, every_second


# Answer 02 : Numpy array indexing and slicing
def indexing(num1, num2):
    third_num = num1[2]
    last_num = num2[-1, -1]
    first_two_rows = num2[:2, -2:]
    second_row = num2[1]
    first_column = num2[:, 0]

    return third_num, last_num, first_two_rows, second_row, first_column


# Answer 03 : Numpy array operations
def operations(num1, num2):
    numbers = np.arange(1, 11)
    added = num1 + numbers
    double_num2 = num2 * 2
    matrix_result = num2 @ double_num2.T
    means = np.array([num1.mean(), num2.mean(), double_num2.mean()])

    return numbers, added, double_num2, matrix_result, means


# Answer 04 : Numpy array aggregation
def aggregation(num1, num2, double_num2):
    num1_sum = num1.sum()
    num2_min = num2.min()
    double_num2_max = double_num2.max()

    return num1_sum, num2_min, double_num2_max


if __name__ == "__main__":

# --------------------------------------------------------------------------|
    num1, num2, flat_num2, num1_copy, every_second = create_arrays()

    print("------------ Answer 01 ------------\n")
    print("num1:", num1)
    print("num2:\n", num2)
    print("flat_num2:", flat_num2)
    print("num1_copy:", num1_copy)
    print("every_second:", every_second)

# --------------------------------------------------------------------------|
    third_num, last_num, first_two_rows, second_row, first_column = indexing(num1, num2)

    print("\n\n------------ Answer 02 ------------")
    print("\nThird element of num1:", third_num)
    print("Last element of num2:", last_num)
    print("First two rows and last two columns:\n", first_two_rows)
    print("Second row of num2:", second_row)
    print("First column of num2:", first_column)

# --------------------------------------------------------------------------|
    numbers, added, double_num2, matrix_result, means = operations(num1, num2)

    print("\n\n------------ Answer 03 ------------")
    print("\nnumbers:", numbers)
    print("added:", added)
    print("double_num2:\n", double_num2)
    print("matrix_result:\n", matrix_result)
    print("means:", means)

# --------------------------------------------------------------------------|
    num1_sum, num2_min, double_num2_max = aggregation(num1, num2, double_num2)

    print("\n\n------------ Answer 04 ------------")
    print("\nnum1_sum:", num1_sum)
    print("num2_min:", num2_min)
    print("double_num2_max:", double_num2_max)