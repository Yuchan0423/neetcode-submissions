class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ROWS, COLS = len(grid), len(grid[0])

        fruit_set = set()
        added_fruit = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    added_fruit.append((r,c))
                if grid[r][c] == 1:
                    fruit_set.add((r,c))
        time = 0

        while added_fruit and fruit_set:
            for _ in range(len(added_fruit)):
                (r, c) = added_fruit.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) in fruit_set:
                        fruit_set.remove((nr, nc))
                        added_fruit.append((nr, nc))
            time += 1
        
        return -1 if fruit_set else time
        