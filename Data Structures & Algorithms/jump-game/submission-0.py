class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        jump = [False] * (len(nums) - 1)
        jump.append(True)

        for i in range(len(nums) - 2, -1 , -1):
            check = 0
            for j in range(i + 1, i + nums[i] + 1):
                if check == 0 and j < len(nums) and jump[j] is True:
                    check = 1
                    jump[i] = True
        
        return jump[0]
        