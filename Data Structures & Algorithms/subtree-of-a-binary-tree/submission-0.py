# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
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

        subroot_dfs = dfs(subRoot)

        while root:
            if dfs(root) == subroot_dfs:
                return True
            root = root.left

        return False
            