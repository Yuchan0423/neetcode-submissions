class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        total = set(nums)
        check = {n : False for n in nums}

        max_len = 0
        for i in range(len(nums)):
            if check[nums[i]] is False:
                j = nums[i]
                while j in total:
                    check[j] = True
                    j += 1
                max_len = max(j - nums[i], max_len)
        
        return max_len

        
