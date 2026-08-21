"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        copy = {None:None}
        curr = head
        while curr:
            copy[curr] = Node(curr.val) 
            curr = curr.next 
        new_curr = head
        while new_curr:
            copy[new_curr].next = copy[new_curr.next]
            copy[new_curr].random = copy[new_curr.random]
            new_curr = new_curr.next
        
        
        return copy[head]