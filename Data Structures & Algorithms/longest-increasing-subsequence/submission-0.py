class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        max_start = [1] * len(nums)
        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[len(nums) - i - 1] < nums[len(nums) - j - 1]:
                    max_start[i] = max(max_start[i], 1 + max_start[j])
        
        return max(max_start)
        