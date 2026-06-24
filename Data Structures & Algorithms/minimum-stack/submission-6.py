class MinStack:

    def __init__(self):
        self.arr = []
        self.sm = 2 ** 31 - 1

    def push(self, val: int) -> None:
        self.sm = min(self.sm , val)
        self.arr.append(self.sm)
        self.arr.append(val)

    def pop(self) -> None:
        self.arr.pop()
        self.arr.pop()
        self.sm = 2 ** 31 - 1 if self.arr == [] else self.arr[-2] 
    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.arr[-2]
        
