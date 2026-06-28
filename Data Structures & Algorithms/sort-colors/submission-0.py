class Solution:
    def sortColors(self, nums: List[int]) -> None:
        col = [0,0,0]
        for n in nums:
            col[n] += 1
        for i in range(3):
            for j in range(col[i]):
                nums.pop(0)
                nums.append(i)
        
        