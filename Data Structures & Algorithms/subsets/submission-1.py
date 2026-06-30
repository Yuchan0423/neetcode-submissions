class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]
        else:
            num = nums[:-1]
            arr = []
            for li in self.subsets(num):
                arr.append(li)
                lis = li[:]
                lis.append(nums[-1])
                arr.append(lis)
            return arr
        