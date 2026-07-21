class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        
        if n == 0:
            return 1
        
        if n < 0:
            return self.myPow(1 / x, - n)
        
        dp = []
        ans = 1

        while n != 0:
            if n % 2 == 0:
                dp.append(0)
            else:
                dp.append(1)
            n = n // 2
        
        for i in range(len(dp) - 1, -1, -1):
            if dp[i] == 1:
                ans = x * ans * ans
            else:
                ans = ans * ans
        
        return ans