class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        ROWS, COLS = len(matrix), len(matrix[0])

        row = list()
        col = list()

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    if r not in row:
                        row.append(r)
                    if c not in col:
                        col.append(c)
        
        for r in row:
            for c in range(COLS):
                matrix[r][c] = 0
        
        for c in col:
            for r in range(ROWS):
                matrix[r][c] = 0
        
