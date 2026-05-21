# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        def dfs(root):
            values = []
            stack = [root]

            while stack:
                node = stack.pop()
                if node:
                    values.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)
                else:
                    values.append(None)
                

            return values

        p_values, q_values = dfs(p), dfs(q)
        if p_values == q_values:
            return True
        return False