class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        track = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]
        for j in range(len(s) + 1):
            track[-1][j] = 1

        for i in range(len(t) - 1, -1, -1):
            for j in range(len(s) - 1, -1, -1):
                if t[i] == s[j]:
                    track[i][j] = track[i + 1][j + 1] + track[i][j + 1]
                else:
                    track[i][j] = track[i][j + 1]
        
        return track[0][0]