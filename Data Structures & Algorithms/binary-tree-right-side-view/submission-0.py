# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if not root:
            return []
        
        res = []
        queue = deque([[root, 0]])
        level_set = set()
        #level_set = set() -- checks whether height has already been visited
        #stack = [[1, 0], [3, 1], [2, 1], [4, 2], [5, 2]] -- [node, height]

        while queue:
            node, level = queue.popleft()
            if node.right:
                queue.append([node.right, level + 1])
            if node.left:
                queue.append([node.left, level + 1])
            if node:
                if level not in level_set:
                    res.append(node.val)
                    level_set.add(level) 
            
            
                

        return res
                