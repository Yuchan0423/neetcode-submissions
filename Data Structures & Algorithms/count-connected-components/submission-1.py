class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = [[] for _ in range(n)]
        visit = [False] * n
        num = 0
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def bfs(node):
            q = deque([node])
            visit[node] = True
            while q:
                cur = q.popleft()
                for nei in adj[cur]:
                    if not visit[nei]:
                        visit[nei] = True
                        q.append(nei)
            
        for node in range(n):
            if not visit[node]:
                bfs(node)
                num += 1
            
        return num
        