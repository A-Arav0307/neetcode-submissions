# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2:
            val = l1.val + l2.val + carry 
            if val > 9:
                carry = val // 10
                cur.next = ListNode(val % 10)
                
            else:
                cur.next = ListNode(val)
                
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        if carry:
            cur.next = ListNode(carry)

        return dummy.next