class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = dict()
        for num in nums:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1
        
        set_nums = list(dic.keys())
        set_nums.sort(key = lambda s : dic[s])

        return set_nums[-k : ]
        