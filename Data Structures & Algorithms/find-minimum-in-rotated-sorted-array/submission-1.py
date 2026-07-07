class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while right - left >= 2:
            mid = (left + right) // 2
            if nums[left] < nums[right]:
                return nums[left]
            if nums[left] < nums[mid]:
                left = mid
            else:
                right = mid

        return min(nums[left], nums[right])