class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        sub, contain = len(text1), len(text2)
        
        checklist = [0] * (sub + 1)

        for i in range(contain - 1, -1, -1):
            if text2[i] in text1:
                arr = checklist[:]
                for j in range(sub - 1, -1, -1):
                    if text2[i] == text1[j]:
                        checklist[j] = 1 + max(arr[j + 1 :])
            
        return max(checklist)


