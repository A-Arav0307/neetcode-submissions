# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []

        def in_order(node):
            if node is None:
                return 0 
            
            in_order(node.left)
            nodes.append(node.val)
            in_order(node.right)

        in_order(root)

        return nodes[k-1]