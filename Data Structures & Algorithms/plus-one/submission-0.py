class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        q = deque()
        i = 1
        while i <= len(digits) and digits[- i] == 9:
            q.appendleft(0)
            i += 1

        if i == len(digits) + 1:
            q.appendleft(1)
            return list(q)
        
        q.appendleft(digits[- i] + 1)

        i += 1

        while i <= len(digits):
            q.appendleft(digits[- i])
            i += 1
        
        return list(q)
