# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        head = res
        carry=0
        suma=0
        while l1 and l2:
            suma = l1.val + l2.val + carry
            val = suma % 10
            carry = suma // 10
            l1=l1.next
            l2=l2.next
            res.next=ListNode(val)
            res= res.next

        while l1:
            suma = l1.val + carry
            val = suma % 10
            carry = suma // 10
            l1=l1.next
            res.next=ListNode(val)
            res= res.next

        while l2:
            suma = l2.val + carry
            val = suma % 10
            carry = suma // 10
            l2=l2.next
            res.next=ListNode(val)
            res= res.next

        if carry > 0:
            res.next = ListNode(carry)
            res = res.next

        return head.next
            
        