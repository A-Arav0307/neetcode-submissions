# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        head = dummy
        carry = False 

        while l1 and l2:
            value = l1.val + l2.val
            if carry: value += 1
            carry = False 
            if value >= 10:
                carry = True 
                head.next = ListNode(value - 10)
            
            else: 
                head.next = ListNode(value)

            head = head.next 
            l1 = l1.next
            l2 = l2.next 

        while l1:
            if carry:
                l1.val += 1 
            carry = False 

            if l1.val >= 10: 
                carry = True 
                head.next = ListNode(l1.val-10)
            else:
                head.next = ListNode(l1.val)

            head = head.next
            l1 = l1.next

        while l2:
            if carry:
                l2.val += 1 
            carry = False 

            if l2.val >= 10: 
                carry = True 
                head.next = ListNode(l2.val-10)
            else:
                head.next = ListNode(l2.val)

            head = head.next
            l2 = l2.next

        if carry: 
            head.next = ListNode(1) 

        return dummy.next 