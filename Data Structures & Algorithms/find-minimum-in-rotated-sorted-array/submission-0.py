class Solution:
    def findMin(self, nums: List[int]) -> int:
        def rotate(nums, l, r):
            if nums[l] < nums[r]:
                return nums[l]
            
            if r - l <= 1:
                return nums[r]
            
            mid = (l + r) // 2
            if nums[l] < nums[mid]:
                return rotate(nums, mid , r)
            else:
                return rotate(nums, l, mid)
        
        return rotate(nums, 0, len(nums) - 1)