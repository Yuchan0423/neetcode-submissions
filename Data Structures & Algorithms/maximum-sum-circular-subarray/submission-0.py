class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        cnt = 0
        for num in nums:
            if num > 0:
                cnt = 1
        
        if cnt == 0:
            return max(nums)

        cnt = 0

        for num in nums:
            if num < 0:
                cnt = 1
        
        if cnt == 0:
            return sum(nums)

        max_sum = 0
        curr_sum = 0

        for num in nums:
            curr_sum = max(curr_sum + num , 0)
            max_sum = max(max_sum, curr_sum)
        
        min_sum = 0
        curr_sum = 0

        for num in nums:
            curr_sum = min(curr_sum + num, 0)
            min_sum = min(min_sum, curr_sum)
        
        return max(max_sum, sum(nums) - min_sum)