# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        
        while head:
            nxt = head.next  # 1. Save the next node
            head.next = prev # 2. Reverse the pointer
            prev = head      # 3. Move prev forward
            head = nxt       # 4. Move curr forward
            
        return prev    


