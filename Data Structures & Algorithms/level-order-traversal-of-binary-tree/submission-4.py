# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        def max_depth(root):
            if not root:
                return 0
            left_height = 1 + max_depth(root.left)
            right_height = 1 + max_depth(root.right)
            return max(left_height, right_height) 
        height = max_depth(root)

        final_list = [ [] for _ in range(height) ]

        queue = deque([[root, 0]])
        while queue:
            node, level = queue.popleft()
            if node: 
                final_list[level].append(node.val)
                queue.append([node.left, level+1])
                queue.append([node.right, level+1])
            
        return final_list