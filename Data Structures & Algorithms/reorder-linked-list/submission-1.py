# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first , second = head, head
        length = 1

        while second.next is not None:
            second = second.next
            length += 1
        
        for _ in range(length // 2 - 1):
            third = first.next
            first.next = second
            second.next = third
            first = third
            fourth = second
            second = third
            while second.next != fourth:
                second = second.next
        
        if length % 2 == 0:
            second.next = None
        
        elif length >= 3:
            tmp = first.next
            first.next = second
            second.next = tmp
            tmp.next = None
