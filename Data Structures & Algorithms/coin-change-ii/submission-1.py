class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        track = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]

        for i in range(len(coins) + 1):
            track[i][0] = 1
        
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    track[i][j] = track[i][j - coins[i - 1]] + track[i - 1][j]
                else:
                    track[i][j] = track[i - 1][j]
        
        return track[-1][-1]