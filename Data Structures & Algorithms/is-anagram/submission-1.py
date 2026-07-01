class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        nums = {}
        numt = {}
        for num in s:
            if num in nums:
                nums[num] += 1
            else:
                nums[num] = 1
        
        for num in t:
            if num in numt:
                numt[num] += 1
            else:
                numt[num] = 1
        
        if len(s) != len(t):
            return False

        for num in nums:
            if num not in numt or nums[num] != numt[num]:
                return False

        return True
        