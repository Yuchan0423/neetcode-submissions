class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1,1]
        while len(arr) <= 45:
            arr.append(arr[-1] + arr[-2])
        return arr[n]