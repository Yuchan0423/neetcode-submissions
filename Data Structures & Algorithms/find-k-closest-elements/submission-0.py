class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        L, R = -1, len(arr)

        while L + 1 < R:
            mid = (L + R) // 2
            if arr[mid] >= x:
                R = mid
            else:
                L = mid
        
        while R - L <= k:
            if L <= -1:
                R += 1
            elif R >= len(arr):
                L -= 1
            elif abs(x - arr[L]) <= abs(x - arr[R]):
                L -= 1
            else:
                R += 1
        
        return arr[L + 1 : R]
