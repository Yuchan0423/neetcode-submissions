class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = cnt = 0
        for num in nums:
            if num == val:
                cnt += 1
            else:
                nums[res] = num
                res += 1
        for i in range(res,len(nums)):
            nums[i] = 0

        return res