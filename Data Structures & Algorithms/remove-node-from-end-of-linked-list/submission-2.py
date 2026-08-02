# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #find length of linked list
        length = 0
        dummy = ListNode()
        dummy.next = head
        old_head = head
        while old_head:
            length += 1
            old_head = old_head.next

        target = length - n
        new_head = head 
        prev = None
        reach = 0
        while target != reach:
            reach += 1
            prev = new_head
            new_head = new_head.next
        if prev is None:
            dummy.next = new_head.next
        else:
            prev.next = new_head.next
            new_head.next = None

        return dummy.next