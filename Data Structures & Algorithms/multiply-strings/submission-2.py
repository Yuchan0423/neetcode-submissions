class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        N, M = len(num1), len(num2)
        arr = list()
        place = 0
        num = 0
        while place < N + M - 1:
            for i in range(N):
                if 0 <= place - i < M:
                    num += int(num1[- i - 1]) * int(num2[- place + i - 1])
            
            arr.append(str(num % 10))
            num = num // 10
            place += 1
        
        while num != 0:
            arr.append(str(num % 10))
            num = num // 10
        
        return ''.join(arr[::-1])