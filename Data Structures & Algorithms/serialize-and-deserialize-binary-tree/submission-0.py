# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        from collections import deque
        if not root:
            return 'N'
        
        string = ""
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                string += str(node.val) + ','
            if node is None:
                string += "N,"

        return string[:-1]

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        from collections import deque
        values = data.split(',')
        i = 1
        if values[0] == 'N':
            return None 
        root = TreeNode(int(values[0]))
        queue = deque([root])
        while queue:
            node = queue.popleft()
            
            if values[i] != 'N':
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
           

            else:
                node.left = None

            i += 1 

            if values[i] != 'N':
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            else:
                node.right = None

            i += 1

        return root
            

