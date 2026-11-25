class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isSumTree(self, root):

        def check(node):
            if node is None:
                return 0, True

            if node.left is None and node.right is None:
                return node.val, True

            left_sum, left_valid = check(node.left)
            right_sum, right_valid = check(node.right)

            if not left_valid or not right_valid:
                return 0, False

            if node.val != left_sum + right_sum:
                return 0, False

            return node.val + left_sum + right_sum, True

        total, result = check(root)
        return result


# Create the binary tree
root = TreeNode(26)
root.left = TreeNode(10)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(6)
root.right.right = TreeNode(3)

solution = Solution()
result = solution.isSumTree(root)

print("\nInput:", [26, 10, 3, 4, 6, 3])
print("Output:", "The given tree is a SumTree" if result else "The given tree is not a SumTree", "\n")
