class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        L = 0
        check = set()

        for R in range(len(nums)):

            if nums[R] in check:
                return True

            check.add(nums[R])

            if R - L + 1 > k:
                check.remove(nums[L])
                L += 1

        return False