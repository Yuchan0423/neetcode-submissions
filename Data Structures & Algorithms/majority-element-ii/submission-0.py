class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)

        ans = []

        for key in counts.keys():
            if 3 * counts[key] - 1 >= len(nums):
                ans.append(key)
        
        return ans