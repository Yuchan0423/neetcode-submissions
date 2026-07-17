class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return (sum(nums) - (max(nums) * (max(nums) + 1) // 2)) // (len(nums) - max(nums))
        
