class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for _ in range(len(temperatures))]
        
        q = list()

        for i, temp in enumerate(temperatures):
            while q and q[-1][0] < temp:
                index = q.pop()[1]
                ans[index] = i - index

            q.append((temp, i))

        return ans