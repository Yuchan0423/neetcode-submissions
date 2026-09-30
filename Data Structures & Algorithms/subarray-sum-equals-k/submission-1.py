class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_array = [0]
        su = 0
        for i in range(len(nums)):
            su += nums[i]
            sum_array.append(su)
        
        cnt = 0
        counter = {}
        for i in range(len(nums), -1, -1):
            cnt += counter.get(sum_array[i] + k, 0)
            counter[sum_array[i]] = 1 + counter.get(sum_array[i], 0)
    
        return cnt