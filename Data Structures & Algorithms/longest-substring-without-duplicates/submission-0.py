class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        
        max_len = 1
        i, j = 0, 0
        num_set = set()
        num_set.add(s[0])
        
        while j < len(s) - 1:
            if s[j + 1] not in num_set:
                num_set.add(s[j + 1])
                j = j + 1
                if j - i + 1 > max_len:
                    max_len = j - i + 1
            else:
                num_set.remove(s[i])
                i = i + 1
        
        return max_len