class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countmap = {}
        while nums != []:
            num = nums.pop()
            if num in countmap:
                return True
            else:
                countmap[num] = 1
        return False
        