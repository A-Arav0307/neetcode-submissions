# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find mid
        dummy = ListNode()
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        

        #reverse list
        new_head = slow.next
        slow.next = None
        prev = None
        curr = new_head 

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        #merge lists

        while head and prev:
            head_node = head.next
            prev_node = prev.next

            head.next = prev
            prev.next = head_node

            head = head_node
            prev = prev_node

        
