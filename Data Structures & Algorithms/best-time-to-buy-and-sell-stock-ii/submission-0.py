class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minus = [0] * len(prices)
        plus = [0] * len(prices)

        minus[0] = -prices[0]

        for i in range(1, len(prices)):
            minus[i] = max(minus[i - 1], plus[i - 1] - prices[i])
            plus[i] = max(plus[i - 1], minus[i] + prices[i])

        return plus[-1]