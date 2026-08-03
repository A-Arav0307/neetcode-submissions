# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head.next
        while slow and fast.next:
            if slow.val == fast.next.val:
                return True
            fast = fast.next.next
            slow = slow.next

        return False