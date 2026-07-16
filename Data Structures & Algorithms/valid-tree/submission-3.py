class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        visit = [False] * n
        adj_dic = {i : list() for i in range(n)}

        for u, v in edges:
            adj_dic[u].append(v)
            adj_dic[v].append(u)

        def dfs(node, visited):
            visit[node] = True
            for nei in adj_dic[node]:
                if nei not in visited:
                    visited.add(node)
                    dfs(nei, visited)
                    visited.remove(node)
        
        dfs(0, set())

        for i in range(n):
            if visit[i] == False:
                return False
        
        return True