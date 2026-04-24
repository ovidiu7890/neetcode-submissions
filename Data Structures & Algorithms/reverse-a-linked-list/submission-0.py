# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        top = head
        if top == None:
            return top
        dummy = ListNode(top.val)
        top = top.next
        while top!=None:
            ceva = ListNode(top.val)
            ceva.next = dummy
            dummy = ceva
            top = top.next
        return dummy
        