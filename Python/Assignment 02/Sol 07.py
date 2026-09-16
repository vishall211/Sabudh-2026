def rotateMatrix(matrix):
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
    return matrix

# Checking function
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
print(rotateMatrix(matrix1))
