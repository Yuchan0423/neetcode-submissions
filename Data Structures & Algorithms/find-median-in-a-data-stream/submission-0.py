

class MedianFinder:

    def __init__(self):
        self.arr = list()

    def addNum(self, num: int) -> None:
        
        L = 0
        R = len(self.arr) - 1

        if len(self.arr) == 0 or num > self.arr[-1]:
            self.arr.append(num)
        
        elif num < self.arr[0]:
            self.arr.insert(0, num)
        
        else:
            while R - L >= 2:
                mid = (L + R) // 2
                if self.arr[mid] < num:
                    L = mid
                else:
                    R = mid
            self.arr.insert(R, num)

        

    def findMedian(self) -> float:

        return float(self.arr[(len(self.arr) - 1) // 2] + self.arr[len(self.arr) // 2]) / 2
        