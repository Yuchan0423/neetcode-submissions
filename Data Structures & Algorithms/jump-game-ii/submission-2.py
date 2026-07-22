class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0
        
        L = 1
        R = nums[0]
        cnt = 1

        while L <= R:
            if R >= len(nums) - 1:
                return cnt

            max_interval = 0
            for i in range(L, R + 1):
                max_interval = max(max_interval, i + nums[i])
            L, R = R + 1, max_interval

            cnt += 1
        