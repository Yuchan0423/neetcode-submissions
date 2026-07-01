class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_num = {}
        t_num = {}
        for num in s:
            if num in s_num:
                s_num[num] += 1
            else:
                s_num[num] = 1
        
        for num in t:
            if num in t_num:
                t_num[num] += 1
            else:
                t_num[num] = 1
        
        return t_num == s_num
        