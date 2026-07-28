class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        visited = set()
        depth = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    depth.append((r, c))
                    visited.add((r, c))
        
        deep = 0
        while depth:
            instant = deque()
            for _ in range(len(depth)):
                (r, c) = depth.popleft()
                grid[r][c] = deep
                for dr, dc in directions:
                    if 0 <= r + dr < ROWS and 0 <= c + dc < COLS and grid[r + dr][c + dc] > 0 and (r + dr, c + dc) not in visited:
                        instant.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))
            
            depth = instant
            deep += 1
            

