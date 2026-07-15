class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def dfs(r, c, word, visited):
            if word == "":
                return True

            if r < 0 or r >= ROWS or c < 0 or c >= COLS or word[0] != board[r][c] or (r,c) in visited:
                return False
            
            visited.add((r, c))
            for dr, dc in direction:
                if dfs(r + dr, c + dc, word[1:], visited):
                    return True
            
            visited.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, word, set()):
                    return True
        
        return False
            
        