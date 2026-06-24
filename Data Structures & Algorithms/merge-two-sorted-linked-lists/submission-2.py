# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        if head1 is None:
            return head2
            
        elif head2 is None:
            return head1

        if head1.val < head2.val:
            head = head1
            head1 = head1.next
        else:
            head = head2
            head2 = head2.next

        pos = head

        while head1 and head2:
            if head1.val < head2.val:
                head.next =  head1
                head = head.next
                head1 = head1.next
            else:
                head.next = head2
                head = head.next
                head2 = head2.next
        
        if head1:
            head.next = head1
        else:
            head.next = head2

        return pos
