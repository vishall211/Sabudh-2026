class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isIdentical(self, root1, root2):
        if root1 is None and root2 is None:
            return True

        if root1 is None or root2 is None:
            return False

        if root1.val != root2.val:
            return False

        return (self.isIdentical(root1.left, root2.left) and
                self.isIdentical(root1.right, root2.right))


# Create first tree
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)

# Create second tree
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)

solution = Solution()
result = solution.isIdentical(root1, root2)

print("\nInput: Two binary trees")
print("Output:", "Both trees are identical" if result else "Trees are not identical", "\n")
