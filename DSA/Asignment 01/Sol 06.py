def spiral_order(matrix):

    ans = []
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:

        # Add the top row
        for i in range(left, right + 1):
            ans.append(matrix[top][i])
        top += 1

        # Add the right column
        for i in range(top, bottom + 1):
            ans.append(matrix[i][right])
        right -= 1

        # Check before adding the bottom row
        if top <= bottom:
            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1

        # Check before adding the left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1

    return ans


# Default input
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = spiral_order(matrix)
print("\nSpiral order is : ", result,"\n")