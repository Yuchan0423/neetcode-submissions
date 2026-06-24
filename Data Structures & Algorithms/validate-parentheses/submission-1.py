class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        ans = [0]
        i = 0
        while(i < n):
            if (ans[-1] == '{' and s[i] == '}') or (ans[-1] == '(' and s[i] == ')') or (ans[-1] == '[' and s[i] == ']'):
                ans.pop()
            else:
                ans.append(s[i])
            i += 1
        if len(ans) == 1:
            return True
        else:
            return False
