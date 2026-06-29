class Deque:
    
    def __init__(self):
        self.quere = []

    def isEmpty(self) -> bool:
        return self.quere == []

    def append(self, value: int) -> None:
        self.quere.append(value)

    def appendleft(self, value: int) -> None:
        arr = [value]
        if self.quere != []:
            for val in self.quere:
                arr.append(val)
        self.quere = arr

    def pop(self) -> int:
        if self.quere == []:
            return -1
        val = self.quere[-1]
        self.quere.pop()
        return val

    def popleft(self) -> int:
        if self.quere == []:
            return -1
        return self.quere.pop(0)
