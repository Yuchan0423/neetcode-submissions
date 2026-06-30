class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if nums == [] and target == 0:
            return [[]]
        elif nums == []:
            return []
        nums.sort()
        if target < nums[-1]:
            return self.combinationSum(nums[:-1], target)
        else:
            arr = [subset + [nums[-1]] for subset in self.combinationSum(nums,target-nums[-1])]
            return arr + self.combinationSum(nums[:-1],target)
        