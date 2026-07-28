class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(len(nums) - (k % len(nums))):
            val = nums.pop(0)
            nums.append(val)
        