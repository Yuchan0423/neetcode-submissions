class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        check = []
        for i in range(len(s)):
            L = 0
            R = i
            while L < R and s[L] == s[R]:
                L += 1
                R -= 1
            if L >= R:
                check.append(i)

        for ch in check:
            if ch != len(s) - 1:
                for li in self.partition(s[ch + 1 : ]):
                    pal = [s[:ch + 1]]
                    pal.extend(li)
                    ans.append(pal)
            else:
                ans.append([s])
        
        return ans
        