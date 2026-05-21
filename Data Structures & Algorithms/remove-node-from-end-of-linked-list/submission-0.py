# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #find length of linked list
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        num = length - n
        #reset values
        length = 0
        curr = head
        prev = None
        while length != num:
            prev = curr
            curr = curr.next
            length += 1

        #remove node
        new_node = curr.next
        curr.next = None
        if prev is None:
            return new_node
        prev.next = new_node

        return head
