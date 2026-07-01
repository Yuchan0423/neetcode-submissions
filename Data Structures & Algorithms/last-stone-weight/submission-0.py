class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone = [-s for s in stones]
        heapq.heapify(stone)
        while len(stone) >= 2:
            x = heapq.heappop(stone)
            y = heapq.heappop(stone)
            if x != y:
                heapq.heappush(stone, x - y)
        return -sum(stone)