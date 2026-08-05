class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0 for _ in range(len(prices) + 2)]

        max_dp = [0 for _ in range(len(prices) + 2)]

        high = [0 for _ in range(len(prices) + 1)]

        max_high = [0 for _ in range(len(prices) + 1)]

        for i in range(len(prices) - 1, -1, -1):
            dp[i] = max_high[i + 1] - prices[i]
            max_dp[i] = max(max_dp[i + 1], dp[i])
            high[i] = max_dp[i + 2] + prices[i]
            max_high[i] = max(max_high[i + 1], high[i])


        return max_dp[0] 
        