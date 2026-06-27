# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return head
        else:
            curr = self.reverseList(head.next)
            prev = curr
            if curr is None:
                return head
            else:
                while curr.next is not None:
                    curr = curr.next
                curr.next = head
                head.next = None
        return prev

        