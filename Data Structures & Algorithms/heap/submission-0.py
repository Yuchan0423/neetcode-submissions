class MinHeap:
    
    def __init__(self):
        self.num = [0]

    def push(self, val: int) -> None:

        self.num.append(val)
        i = len(self.num) - 1

        while i >= 2 and self.num[i] < self.num[i//2]:
            self.num[i], self.num[i//2] = self.num[i//2], self.num[i]
            i = i//2

    def pop(self) -> int:
        if self.num == [0]:
            return -1
        
        if len(self.num) == 2:
            return self.num.pop()
        
        val = self.num[1]
        self.num[1] = self.num.pop()
        i = 1
        while 2 * i < len(self.num):
            if (2 * i + 1 < len(self.num)) and self.num[i] > self.num[2 * i + 1] and self.num[2 * i + 1] < self.num[2 * i]:
                self.num[i], self.num[2 * i + 1] = self.num[2 * i + 1], self.num[i]
                i = 2 * i + 1
            elif self.num[i] > self.num[2 * i]:
                self.num[i], self.num[2 * i] = self.num[2 * i], self.num[i]
                i = 2 * i
            else:
                break
        return val

    def top(self) -> int:

        if self.num == [0]:
            return -1

        return self.num[1]

    def heapify(self, nums: List[int]) -> None:
        self.num += nums
        cur = (len(self.num) - 1)//2
        while cur > 0:
            i = cur
            while 2 * i < len(self.num):
                if (2 * i + 1 < len(self.num)) and self.num[i] > self.num[2 * i + 1] and self.num[2 * i + 1] < self.num[2 * i]:
                    self.num[i], self.num[2 * i + 1] = self.num[2 * i + 1], self.num[i]
                    i = 2 * i + 1
                elif self.num[i] > self.num[2 * i]:
                    self.num[i], self.num[2 * i] = self.num[2 * i], self.num[i]
                    i = 2 * i
                else:
                    break
            cur -= 1
    