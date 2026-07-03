class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        arr = [(sr,sc)]
        val = image[sr][sc]
        total = arr[:]
        ROWS, COLS = len(image), len(image[0])
        while len(arr) > 0:
            pop = []
            for (r,c) in arr:
                if r >= 1 and image[r - 1][c] == val and (r - 1, c) not in total:
                    pop.append((r - 1,c))
                if c >= 1 and image[r][c - 1] == val and (r, c - 1) not in total:
                    pop.append((r,c - 1))
                if r + 1 < ROWS and image[r + 1][c] == val and (r + 1, c) not in total:
                    pop.append((r + 1,c))
                if c + 1 < COLS and image[r][c + 1] == val and (r, c + 1) not in total:
                    pop.append((r,c + 1))
            total += pop
            arr = pop
        for (r,c) in total:
            image[r][c] = color

        return image
                    

        