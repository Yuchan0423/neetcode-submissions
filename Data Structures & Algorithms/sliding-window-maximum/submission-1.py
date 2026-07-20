class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        ans = list()

        shorten_nums = list()

        if k == 1:
            return nums
        
        if k == 2:
            for i in range(n - 1):
                ans.append(max(nums[i], nums[i + 1]))
            return ans
            

        ans = list()

        shorten_nums = list()

        for i in range(n // 2):
            shorten_nums.append(max(nums[2 * i], nums[2 * i + 1]))

        if k % 2 == 1:
            max_slide = self.maxSlidingWindow(shorten_nums, k //2)
            for i in range(n - k):
                if i % 2 == 0 :
                    ans.append(max(max_slide[i // 2], nums[i + k - 1]))
                else:
                    ans.append(max(max_slide[i // 2 + 1], nums[i]))
            if n % 2 == 0:
                ans.append(max(max_slide[-1], nums[-k]))
            else:
                ans.append(max(max_slide[-1], nums[-1]))
        
        else:
            max_slide = self.maxSlidingWindow(shorten_nums, k //2 - 1)
            for i in range(n - k):
                if i % 2 == 0 :
                    ans.append(max(max_slide[i // 2], nums[i + k - 2], nums[i + k - 1]))
                else:
                    ans.append(max(max_slide[i // 2 + 1], nums[i], nums[i + k - 1]))
            if n % 2 == 0:
                ans.append(max(max_slide[-1], nums[-k], nums[-k + 1]))
            else:
                ans.append(max(max_slide[-1], nums[-1], nums[-k]))

        return ans
