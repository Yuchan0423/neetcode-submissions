class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        arr = self.stack
        arr.append(val)
        self.stack = arr

    def pop(self) -> None:
        arr = self.stack
        arr.pop()
        self.stack = arr

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        arr = self.stack
        return min(arr)
            
