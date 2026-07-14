class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        include_first = [0] * (len(nums) + 1)
        exclude_first = [0] * (len(nums) + 2)

        for i in range(len(nums) - 2, 1, -1):
            include_first[i] = max(include_first[i + 1], include_first[i + 2] + nums[i])
        
        for i in range(len(nums) - 1, 0, -1):
            exclude_first[i] = max(exclude_first[i + 1], exclude_first[i + 2] + nums[i])
        
        return max(nums[0] + include_first[2], exclude_first[1])
