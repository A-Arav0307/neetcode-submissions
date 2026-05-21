# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return 
        
        def find_min(root):
            cur = root
            while cur and cur.left:
                cur = cur.left
            return cur

            
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        else:
            if root.left and root.right:
                minimum_node = find_min(root.right)
                root.val = minimum_node.val
                root.right = self.deleteNode(root.right, root.val)
            
            elif not root.left and not root.right:
                root = None 

            elif (root.left and not root.right):
                root.val = root.left.val
                root.left = None

            elif (root.right and not root.left):
                root.val = root.right.val
                root.right = None

        return root
