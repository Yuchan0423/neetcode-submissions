class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        cnt = len(nums)
        for i in range(cnt):
            nums.append(nums[i])
        
        return nums
            