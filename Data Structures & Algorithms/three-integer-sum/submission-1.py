class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        num_set = set(nums)
        check = set()
        ans = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                if - nums[i] - nums[j] in num_set:
                    if nums[i] == 0 and nums[j] == 0 and count[0] == 2:
                        continue
                    if 2 * nums[i] + nums[j] == 0 and count[nums[i]] == 1:
                        continue
                    if 2 * nums[j] + nums[i] == 0 and count[nums[j]] == 1:
                        continue
                    triplet = [nums[i], nums[j], -nums[i] - nums[j]]
                    triplet.sort()
                    tuple_triplet = tuple(triplet)
                    if tuple_triplet not in check:
                        check.add(tuple_triplet)
                        ans.append(triplet)
        
        return ans
