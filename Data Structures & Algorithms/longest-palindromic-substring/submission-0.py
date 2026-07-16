class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        ans_left, ans_right = 0, 0
        for p in range(len(s)):
            left, right = p, p
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left = left - 1
                right = right + 1
            
            left = left + 1
            right = right - 1
            if right - left + 1 > max_len:
                ans_left = left
                ans_right = right
                max_len = right - left + 1
            
        for p in range(len(s) - 1):
            left, right = p, p + 1
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left = left - 1
                right = right + 1
            
            left = left + 1
            right = right - 1
            if right - left + 1 > max_len:
                ans_left = left
                ans_right = right
                max_len = right - left + 1
        
        return s[ans_left : ans_right + 1]