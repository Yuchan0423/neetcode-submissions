class Solution:
    def isHappy(self, n: int) -> bool:

        num_set = set()

        while n not in num_set and n != 1:

            num_set.add(n)
            num = 0
            while n != 0:
                num += (n % 10) ** 2
                n = n // 10
            n = num

        return n == 1
        