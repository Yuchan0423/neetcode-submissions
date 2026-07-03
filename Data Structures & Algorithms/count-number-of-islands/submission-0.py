class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        ones = set()
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    ones.add((r,c))
        
        while len(ones) > 0:
            (sr, sc) = ones.pop()
            arr = set()
            arr.add((sr, sc))
            total = arr
            while len(arr) > 0:
                plus = set()
                while len(arr) > 0:
                    (r, c) = arr.pop()
                    if (r, c + 1) in ones and (r, c + 1) not in total:
                        plus.add((r, c + 1))
                    if (r, c - 1) in ones and (r, c - 1) not in total:
                        plus.add((r, c - 1))
                    if (r + 1, c) in ones and (r + 1, c) not in total:
                        plus.add((r + 1, c))
                    if (r - 1, c) in ones and (r - 1, c) not in total:
                        plus.add((r - 1, c)) 
                arr = plus
                total = total | arr
            cnt += 1
            ones = ones - total
            
        return cnt