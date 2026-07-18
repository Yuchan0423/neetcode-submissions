class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        checker = 0
        while 2 * numbers[checker] < target:
            checker += 1
        
        L = checker - 1
        R = checker

        while numbers[L] + numbers[R] != target:
            if numbers[L] + numbers[R] < target:
                R += 1
            else:
                L -= 1
        
        return [L + 1, R + 1]
        