# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node, val):
            if not node.left and not node.right:
                return val == targetSum
            if node.left and dfs(node.left, val + node.left.val):
                return True

            if node.right and dfs(node.right, val + node.right.val):
                return True

            return False

        if dfs(root, root.val):
            return True
        return False