# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()

        cop = ans

        carry = 0

        curr = None

        while l1 and l2:
            ans.val = (carry + l1.val + l2.val) % 10
            carry = (carry + l1.val + l2.val) // 10

            curr = ans
            ans.next = ListNode()
            ans = ans.next

            l1 = l1.next
            l2 = l2.next
        
        while l1:
            ans.val = (carry + l1.val) % 10
            carry = (carry + l1.val) // 10

            curr = ans
            ans.next = ListNode()
            ans = ans.next

            l1 = l1.next
        
        while l2:
            ans.val = (carry + l2.val) % 10
            carry = (carry + l2.val) // 10

            curr = ans
            ans.next = ListNode()
            ans = ans.next

            l2 = l2.next
        
        if carry == 1:
            ans.val = 1
        
        else:
            curr.next = None
        
        return cop


