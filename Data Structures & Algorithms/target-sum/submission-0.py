class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        if (target - sum(nums)) % 2 != 0:
            return 0
        
        target = (sum(nums) - target) // 2

        if target > sum(nums) or target < 0:
            return 0
        cnt = 0
        copy_num = list()

        for num in nums:
            if num == 0:
                cnt += 1
            else:
                copy_num.append(num)
        
        nums = copy_num

        
        ans = [[0 for _ in range(len(nums) + 1)] for _ in range(target + 1)]
        
        for i in range(len(nums) + 1):
            ans[0][i] = 1
        
        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                if j >= nums[i - 1]:
                    ans[j][i] = ans[j - nums[i - 1]][i - 1] + ans[j][i - 1]
                else:
                    ans[j][i] = ans[j][i - 1]
        
        return ans[-1][-1] * (2 ** cnt)
        