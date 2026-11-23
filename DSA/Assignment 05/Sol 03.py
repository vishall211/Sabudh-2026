class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for i in range(rows):

            # Update heights for the current row
            for j in range(cols):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Find the largest rectangle using a stack
            stack = []

            for j in range(cols + 1):
                if j == cols:
                    curr_height = 0
                else:
                    curr_height = heights[j]

                while stack and heights[stack[-1]] > curr_height:
                    height = heights[stack.pop()]
                    if stack:
                        width = j - stack[-1] - 1
                    else:
                        width = j

                    area = height * width
                    max_area = max(max_area, area)
                stack.append(j)

        return max_area


# Input data
matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]

# Run the solution
solution = Solution()
result = solution.maximalRectangle(matrix)

print("\nInput:")
for row in matrix:
    print(row)

print("\nOutput:", result,"\n")
