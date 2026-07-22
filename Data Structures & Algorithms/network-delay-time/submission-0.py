class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_matrix = dict()

        for time in times:
            if time[0] not in adj_matrix:
                adj_matrix[time[0]] = list()
            adj_matrix[time[0]].append((time[2], time[1], time[0]))

        done_values = dict()
        done_values[k] = 0

        heap = []

        if k not in adj_matrix:
            return -1

        for edge in adj_matrix[k]:
            heapq.heappush(heap,edge)
        
        while heap:
            (value, node, out) = heapq.heappop(heap)
            if node in done_values:
                done_values[node] = min(done_values[node], value)
            else:
                done_values[node] = value
                if node in adj_matrix:
                    for edge in adj_matrix[node]:
                        if edge[1] not in done_values:
                            edge = (edge[0] + done_values[node], edge[1], edge[2])
                            heapq.heappush(heap, edge)
        
        return max(done_values.values()) if len(done_values) == n else -1

