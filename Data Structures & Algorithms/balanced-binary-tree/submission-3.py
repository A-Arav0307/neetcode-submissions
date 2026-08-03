# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 
        
        def maxDepth(root):
            if root is None:
                return 0
            return 1 + max(maxDepth(root.left), maxDepth(root.right))

        if root.left:
            left_height = maxDepth(root.left)
        else:
            left_height = 0
        if root.right: 
            right_height = maxDepth(root.right)
        else:
            right_height = 0

        if abs(right_height - left_height) <= 1:
            return True
        return False 