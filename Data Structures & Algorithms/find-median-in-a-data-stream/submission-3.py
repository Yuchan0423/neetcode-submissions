import heapq
class MedianFinder:

    def __init__(self):
        self.big = [float('inf')]
        self.small = [float('inf')]
        self.diff = 0

    def addNum(self, num: int) -> None:
        if self.diff == 0:
            if num < self.big[0]:
                heapq.heappush(self.small, -num)
            else:
                small = heapq.heappop(self.big)
                heapq.heappush(self.small, -small)
                heapq.heappush(self.big, num)
        else:
            if num > -self.small[0]:
                heapq.heappush(self.big, num)
            else:
                big = -heapq.heappop(self.small)
                heapq.heappush(self.big, big)
                heapq.heappush(self.small, -num)

        self.diff = 1 - self.diff

    def findMedian(self) -> float:
        if self.diff == 1:
            return -self.small[0]
        else:
            return (self.big[0] - self.small[0])/2.0
        