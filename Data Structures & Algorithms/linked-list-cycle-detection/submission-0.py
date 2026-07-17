# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visit_list = set()
        while head is not None:
            if head in visit_list:
                return True
            visit_list.add(head)
            head = head.next
        
        return False