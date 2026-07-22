class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)

        if len(s3) != m + n:
            return False

        first = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        second = [[False for _ in range(n + 1)] for _ in range(m + 1)]

        first[0][0] = True
        second[0][0] = True

        for i in range(m + 1):
            for j in range(n + 1):
                if i >= 1 and first[i - 1][j] and s1[- i] == s3[- i - j]:
                    first[i][j] = True
                if i >= 1 and second[i - 1][j] and s1[- i] == s3[- i - j]:
                    first[i][j] = True
                if j >= 1 and first[i][j - 1] and s2[- j] == s3[- i - j]:
                    second[i][j] = True
                if j >= 1 and second[i][j - 1] and s2[- j] == s3[- i - j]:
                    second[i][j] = True
        
        return first[-1][-1] or second[-1][-1]