class Solution:
    def hasOneChild(self, preorder):
        n = len(preorder)

        for i in range(n - 1):
            current = preorder[i]
            next_value = preorder[i + 1]
            last_value = preorder[-1]

            # Check whether both left and right children are possible
            if (current - next_value) * (current - last_value) < 0:
                return False

        return True


preorder = [20, 10, 11, 13, 12]

solution = Solution()
result = solution.hasOneChild(preorder)

print("\nInput:", preorder)
print("Output:", "Yes" if result else "No", "\n")
