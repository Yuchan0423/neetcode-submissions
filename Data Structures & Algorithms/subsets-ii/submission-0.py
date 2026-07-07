class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        if nums == []:
            return [[]]
    

        li = self.subsetsWithDup(nums[1 : ])

        ans = []

        for subset in li:
            clone = subset[:]
            ans.append(clone)

        for subset in li:

            subset.append(nums[0])
            subset.sort()

            if subset not in ans:
                ans.append(subset)

        return ans
        

