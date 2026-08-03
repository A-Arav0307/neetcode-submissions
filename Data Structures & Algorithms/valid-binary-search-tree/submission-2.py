# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        from collections import deque
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if (node.left and node.left.val >= root.val) or (node.right and node.right.val <= root.val):
                return False
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

        return True 