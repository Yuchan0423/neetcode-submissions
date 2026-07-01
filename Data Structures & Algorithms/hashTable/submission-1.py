class Pair:
    def __init__(self, key, value):
        self.key = key
        self.val = value

class HashTable:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        arr = []
        for i in range(self.cap):
            arr.append(None)
        self.map = arr

    def index(self, key):
        return key % self.cap

    def insert(self, key: int, value: int) -> None:
        index = self.index(key)
        checkpoint = True
        while self.map[index] != None:
            if self.map[index].key == key:
                self.map[index].val = value
                checkpoint = False
            index = (index + 1) % self.cap
        if checkpoint:
            self.size += 1
            self.map[index] = Pair(key, value)
            if 2 * self.size >= self.cap:
                self.resize()

    def get(self, key: int) -> int:
        index = self.index(key)
        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
            index = (index + 1) % self.cap
        return -1

    def remove(self, key: int) -> bool:
        index = self.index(key)
        while self.map[index] != None:
            if self.map[index].key == key:
                self.map[index] = None
                self.size -= 1
                return True
            index = (index + 1) % self.cap
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.cap

    def resize(self) -> None:
        self.cap = self.cap * 2
        check = self.map[:]
        arr = []
        for i in range(self.cap):
            arr.append(None)
        self.map = arr
        self.size = 0
        for pair in check:
            if pair:
                self.insert(pair.key, pair.val)
