class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        checklist = [-1] * amount
        checklist.append(0)

        for i in range(amount - 1, -1, -1):
            check = 0
            min_cnt = float("inf")
            for coin in coins:
                if coin + i <= amount and checklist[coin + i] != -1:
                    min_cnt = min(min_cnt, 1 + checklist[coin + i])
                    check = 1
            
            if check == 1:
                checklist[i] = min_cnt
        
        return checklist[0]
            
        