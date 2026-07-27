class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_matrix = {}
        for i, j in edges:
            if i not in adj_matrix:
                adj_matrix[i] = set()
            if j not in adj_matrix:
                adj_matrix[j] = set()
            adj_matrix[i].add(j)
            adj_matrix[j].add(i)
        
        def valid(edge):
            start, end = edge[0], edge[1]
            valid = set()
            def dfs(point):
                if point == start:
                    return True
                
                if point in valid:
                    return False
                
                valid.add(point)
                for nei in adj_matrix[point]:
                    if point != end or nei != start:
                        if dfs(nei):
                            return True
                valid.remove(point)

                return False

            return dfs(end)
        
        for i in range(1, len(edges) + 1):
            if valid(edges[- i]):
                return edges[- i]
                