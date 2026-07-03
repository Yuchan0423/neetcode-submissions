class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        ROWS, COLS = len(grid), len(grid[0])
        length = 0
        total = set()
        total.add((0,0))
        quere = deque()
        quere.append((0,0))

        while quere:
            for _ in range(len(quere)):
                (r, c) = quere.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 1 or (nr, nc) in total:
                        continue
                    quere.append((nr, nc))
                    total.add((nr, nc))
            length += 1

        return -1