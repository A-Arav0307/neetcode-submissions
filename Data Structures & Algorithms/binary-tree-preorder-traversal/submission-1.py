# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        from collections import deque
        
        if not root: 
            return []
        final_list = [root.val]
        cur = root
        left, right = deque([root.left]), deque([root.right])
        
        if root.left:
            cur = root.left
            while left:
                 node = left.popleft()
                 if node: 
                    final_list.append(node.val)
                    left.append(node.left)
                    left.append(node.right)

        if root.right: 
            cur = root.right
            while right:
                node = right.popleft()
                if node:
                    final_list.append(node.val)
                    right.append(node.left)
                    right.append(node.right)

        return final_list
