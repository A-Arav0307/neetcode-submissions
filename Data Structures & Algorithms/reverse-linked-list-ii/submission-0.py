# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        new_l, new_r = left-1, right-1
        new_head = head
        l, r = 0, 0
        prev = None
        def reverse(head):
            curr = head
            prev = None
        
            while curr:
                nxt = curr.next  
                curr.next = prev  
                prev = curr       
                curr = nxt        
                
            return prev

        while l != new_l: 
            l += 1
            prev = new_head
            new_head = new_head.next
        r = l
        tail = new_head 
        while r != new_r: 
            r += 1
            tail = tail.next
        to_connect = tail.next
        tail.next = None

        reversed_head = reverse(new_head)
        if prev: 
            prev.next = tail
        new_head.next = to_connect
        if prev:
            return head
        return tail