class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1

        for i in range(len(s)):
            check_one = 0 if s[len(s) - i - 1] == "0" else 1
            check_two = 1 if i >= 1 and 10 * int(s[len(s) - i - 1]) + int(s[len(s) - i]) <= 26 and check_one == 1 else 0
            dp[i + 1] = check_one * dp[i] + check_two * dp[i - 1]

        return dp[-1] 
        