# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        out = ListNode()
        head = out
        carry = 0
        
        while l1 != None or l2 != None:
            v1, v2 = l1.val if l1 else 0, l2.val if l2 else 0
            carry, total = divmod(v1 + v2 + carry, 10)
            head.next = ListNode(val=total)
            head = head.next
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None

        if carry > 0:
            head.next = ListNode(val=carry)
        return out.next
