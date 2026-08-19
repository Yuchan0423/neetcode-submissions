class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [False for _ in range(len(s))]

        if s[-1] == '1':
            return False
        
        dp[-1] = True

        for i in range(len(s) - 2, -1, -1):
            for j in range(minJump, maxJump + 1):
                if i + j <= len(s) - 1 and s[i] == '0':
                    dp[i] = dp[i] | dp[i + j]
        
        return dp[0]