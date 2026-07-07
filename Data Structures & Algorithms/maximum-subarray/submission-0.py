class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        cnt = 0
        for num in nums:
            if num >= 0:
                cnt = 1
        
        if cnt == 0:
            return max(nums)

        max_sum = 0
        curr_sum = 0
        for num in nums:
            curr_sum = max(num + curr_sum , 0)
            max_sum = max(max_sum, curr_sum)
        
        return max_sum