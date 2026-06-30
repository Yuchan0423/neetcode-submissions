from typing import List

class TreeMap:
    def __init__(self, key=None, val=None):
        self.key = key
        self.value = val
        self.left = None
        self.right = None

    def insert(self, key: int, val: int) -> None:
        if self.key is None or self.key == key:
            self.key = key
            self.value = val
        elif self.key > key:
            if self.left is None:
                self.left = TreeMap(key, val)
            else:
                self.left.insert(key, val)
        else:
            if self.right is None:
                self.right = TreeMap(key, val)
            else:
                self.right.insert(key, val)

    def get(self, key: int) -> int:
        if self.key is None:
            return -1
        if self.key == key:
            return self.value
        elif self.key < key:
            if self.right is None:
                return -1
            return self.right.get(key)
        else:
            if self.left is None:
                return -1
            return self.left.get(key)

    def getMin(self) -> int:
        if self.key is None:
            return -1
        curr = self
        while curr.left is not None:
            curr = curr.left
        return curr.value

    def getMax(self) -> int:
        if self.key is None:
            return -1
        curr = self
        while curr.right is not None:
            curr = curr.right
        return curr.value

    def remove(self, key: int) -> None:
        if self.key is None:
            return None
        elif self.key < key:
            if self.right is None:
                return None
            self.right.remove(key)
            if self.right.key is None:
                self.right = None
        elif self.key > key:
            if self.left is None:
                return None
            self.left.remove(key)
            if self.left.key is None:
                self.left = None
        else:
            if self.left is None and self.right is None:
                self.key = None
                self.value = None
            elif self.left is None:
                child = self.right
                self.key = child.key
                self.value = child.value
                self.left = child.left
                self.right = child.right
            elif self.right is None:
                child = self.left
                self.key = child.key
                self.value = child.value
                self.left = child.left
                self.right = child.right
            else:
                succ = self.right
                while succ.left is not None:
                    succ = succ.left
                self.key = succ.key
                self.value = succ.value
                self.right.remove(succ.key)
                if self.right.key is None:
                    self.right = None

    def getInorderKeys(self) -> List[int]:
        if self.key is None:
            return []
        arr = []
        def getkey(n):
            if n.key is None:
                return
            if n.left is not None:
                getkey(n.left)
            arr.append(n.key)
            if n.right is not None:
                getkey(n.right)
        getkey(self)
        return arr