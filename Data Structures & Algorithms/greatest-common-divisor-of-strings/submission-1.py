class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)
        def checker(s, x):
            if len(s) % x != 0:
                return False
            
            for i in range(x, len(s)):
                if s[i] != s[i - x]:
                    return False
            
            return True
        
        for l in range(min(l1, l2), 0, -1):
            if checker(str1, l) and checker(str2, l) and str1[:l] == str2[:l]:
                return str1[:l]
        
        return ""