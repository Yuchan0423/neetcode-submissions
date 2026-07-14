class Solution:
    def countSubstrings(self, s: str) -> int:

        output = [[0 for _ in range(len(s))] for _ in range(len(s))]
        
        total = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if 0 <= j - i <= 1:
                        output[i][j] = 1
                        total += 1
                    else:
                        output[i][j] = output[i + 1][j - 1]
                        total += output[i + 1][j - 1]
        
        return total
        
        
        

            


            