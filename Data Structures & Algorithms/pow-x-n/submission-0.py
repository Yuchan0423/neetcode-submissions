class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        
        if n == 0:
            return 1
        
        if n < 0:
            return self.myPow(1 / x, - n)
        
        dp = [1 for _ in range(n + 1)]

        for i in range(n):
            dp[i + 1] = x * dp[i]
        
        return dp[-1]