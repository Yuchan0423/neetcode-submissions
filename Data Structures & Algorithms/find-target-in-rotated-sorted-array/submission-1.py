class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        length = len(nums)

        if nums[0] < nums[-1]:
            L = R
        
        while L < R:
            mid = (L + R) // 2
            if nums[L] < nums[mid]:
                L = mid
            else:
                R = mid
        
        check = (L + 1) % length

        L = check
        R = len(nums) + check - 1

        while L <= R:
            mid = (L + R) // 2
            if nums[mid % length] < target:
                L = mid + 1
            elif nums[mid % length] > target:
                R = mid - 1
            else:
                return mid % length
        
        return -1