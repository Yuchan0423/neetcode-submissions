class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ROWS, COLS = len(heights), len(heights[0])

        pacific = deque([(0, i) for i in range(COLS)] + [(j, 0) for j in range(1, ROWS)])

        atlantic = deque([(ROWS - 1, i) for i in range(COLS)] + [(j, COLS - 1) for j in range(ROWS - 1)])

        valid_pacific = set()
        valid_atlantic = set()

        while pacific:
            (r, c) = pacific.popleft()
            valid_pacific.add((r, c))
            for dr, dc in directions:
                sr = r + dr
                sc = c + dc
                if 0 <= sr < ROWS and 0 <= sc < COLS and (sr, sc) not in valid_pacific and heights[sr][sc] >= heights[r][c]:
                    pacific.append((sr, sc))
        
        while atlantic:
            (r, c) = atlantic.popleft()
            valid_atlantic.add((r, c))
            for dr, dc in directions:
                sr = r + dr
                sc = c + dc
                if 0 <= sr < ROWS and 0 <= sc < COLS and (sr, sc) not in valid_atlantic and heights[sr][sc] >= heights[r][c]:
                    atlantic.append((sr, sc))
        
        return list(valid_atlantic & valid_pacific)
        


