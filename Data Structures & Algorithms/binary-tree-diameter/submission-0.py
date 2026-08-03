# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_val = 0

        def dfs(node, dist):
            if not node.left and not node.right:
                return 0
            
            dist += 1
            if node.right:
                dfs(node.right, dist)
                self.max_val = max(self.max_val, dist)
            dist -= 1
            if node.left:
                dfs(node.left, dist)
                self.max_val = max(self.max_val, dist)

        dfs(root, 0) 
        return self.max_val + 1