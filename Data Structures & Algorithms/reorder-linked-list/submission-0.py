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

        first = head
        second = prev

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next
