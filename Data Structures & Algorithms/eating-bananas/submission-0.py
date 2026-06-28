class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eatspeed(arr, num):
            s = 0
            for food in arr:
                s += (food - 1) // num
                s += 1
            return s
        L = 1
        R = max(piles)
        while L < R:
            mid = (L+R) // 2
            if eatspeed(piles, mid) <= h:
                R = mid
            elif eatspeed(piles, mid) > h:
                L = mid + 1

        return L
        