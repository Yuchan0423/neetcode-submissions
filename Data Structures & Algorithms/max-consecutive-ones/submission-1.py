class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        for i in range(len(nums)):
            cnt = 0
            while i < len(nums) and nums[i] == 1:
                cnt = cnt+1
                i = i+1
            if(cnt > max_ones):
                max_ones = cnt
        return max_ones