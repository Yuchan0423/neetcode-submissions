class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = k = 0
        n = len(nums)
        while i < len(nums):
            if(nums[i] == val):
                nums.remove(val)
            else:
                i += 1
                k += 1
        return i
