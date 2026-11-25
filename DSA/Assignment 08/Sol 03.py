class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isSubtreeSum(self, root, target):
        self.found = False

        def calculateSum(node):
            if node is None:
                return 0

            left_sum = calculateSum(node.left)
            right_sum = calculateSum(node.right)

            total = node.val + left_sum + right_sum

            if total == target:
                self.found = True

            return total

        calculateSum(root)
        return self.found


# Create the binary tree
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(6)

root.left.left = TreeNode(5)
root.left.right = TreeNode(9)
root.right.left = TreeNode(8)

target = 17

solution = Solution()
result = solution.isSubtreeSum(root, target)

print("\nInput: Binary tree")
print("Target Sum:", target)
print("Output:", "Yes" if result else "No", "\n")
