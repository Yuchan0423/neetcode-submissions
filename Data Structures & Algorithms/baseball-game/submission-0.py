class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for val in operations:
            if val == "+":
                arr.append(arr[-1] + arr[-2])
            elif val == "C":
                arr.pop()
            elif val == "D":
                arr.append(2 * arr[-1])
            else:
                arr.append(int(val))

        return sum(arr)