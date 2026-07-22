class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        component_group = dict()
        
        ans = 0
        N = len(points)
        group = N

        for i in range(N):
            component_group[i] = set()
            component_group[i].add(i)
        
        heap = []
        for i in range(N - 1):
            for j in range(i + 1, N):
                heapq.heappush(heap, (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
        
        while group != 1:
            (value, node1, node2) = heapq.heappop(heap)
            if component_group[node1] != component_group[node2]:
                ans += value
                group -= 1
                combine = component_group[node1] | component_group[node2]
                for node in combine:
                    component_group[node] = combine
        
        return ans
            