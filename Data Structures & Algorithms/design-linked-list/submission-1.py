class ListNode:
    
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while i <= index and curr:
            curr = curr.next
            i += 1
        if curr:
            return curr.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        curr = ListNode(val)
        curr.next = self.head.next
        curr.prev = self.head
        self.head.next = curr
        curr.next.prev = curr

    def addAtTail(self, val: int) -> None:
        curr = ListNode(val)
        curr.prev = self.tail.prev
        curr.next = self.tail
        self.tail.prev = curr
        curr.prev.next = curr

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        i = 0
        while i < index and curr:
            curr = curr.next
            i += 1
        if curr is not None:
            pov = ListNode(val)
            pov.next = curr.next
            curr.next = pov
            pov.prev = curr
            pov.next.prev = pov

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        i = 0
        while i <= index and curr:
            curr = curr.next
            i += 1
        if curr.next is not None:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        else:
            curr.prev.next = None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)