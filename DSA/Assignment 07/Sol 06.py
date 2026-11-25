class Solution:
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Handle empty strings
        for i in range(m + 1):
            dp[i][0] = i

        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    insert = dp[i][j - 1]
                    delete = dp[i - 1][j]
                    replace = dp[i - 1][j - 1]

                    dp[i][j] = 1 + min(insert, delete, replace)

        return dp[m][n]


word1 = "Army"
word2 = "Public"

solution = Solution()
result = solution.minDistance(word1, word2)

print("\nInput:", word1, word2)
print("Output:", result, "\n")
