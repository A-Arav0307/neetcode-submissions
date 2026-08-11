# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dfs(node, skip):
            if not node: 
                return 0 
            
            if (node, skip) in memo: 
                return memo[(node, skip)] 
            
            if skip:
                max_point = dfs(node.left, False) + dfs(node.right, False)
            
            else:
                rob_current = node.val + dfs(node.left, True) + dfs(node.right, True)
                skip_current = dfs(node.left, False) + dfs(node.right, False)
                max_point = max(rob_current, skip_current)

            memo[(node, skip)] = max_point
            return max_point 

        return max(dfs(root, True), dfs(root, False))