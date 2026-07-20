class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        current = [0 for _ in range(len(cost) + 2)]
        for i in range(len(cost) - 1, -1, -1):
            current[i] = cost[i] + min(current[i + 1], current[i + 2])
        
        return min(current[0], current[1])