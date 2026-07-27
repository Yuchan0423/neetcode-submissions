class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])
        
        for j in range(9):
            col = set()
            for i in range(9):
                if board[i][j] != ".":
                    if board[i][j] in col:
                        return False
                    col.add(board[i][j])
        
        for i in range(3):
            for j in range(3):
                box = set()
                for k in range(3):
                    for l in range(3):
                        if board[3 * i + k][3 * j + l] != ".":
                            if board[3 * i + k][3 * j + l] in box:
                                return False
                        box.add(board[3 * i + k][3 * j + l])
        
        return True