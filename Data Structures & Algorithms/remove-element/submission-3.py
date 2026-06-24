class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0
        
        for num in nums:
            if num is not val:
                nums[res] = num
                res += 1
        for i in range(res,len(nums)):
            nums[i] = 0

        return res