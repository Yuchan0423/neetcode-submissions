class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        grid = [[0 for _ in range(COLS + 1)] for _ in range(ROWS + 1)]

        for r in range(1, ROWS + 1):
            for c in range(1, COLS + 1):
                if r * c == 1:
                    grid[r][c] = 1 - obstacleGrid[0][0]
                else:
                    if obstacleGrid[r - 1][c - 1] == 0:
                        grid[r][c] = grid[r - 1][c] + grid[r][c - 1]
        
        return grid[-1][-1]