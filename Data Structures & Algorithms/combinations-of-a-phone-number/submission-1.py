class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return list()
        
        num_to_alp = {2 : ["a", "b", "c"], 3 : ["d", "e", "f"] , 4 : ["g", "h", "i"], 5 : ["j", "k", "l"] , 6: ["m", "n", "o"], 7 : ["p", "q", "r", "s"], 8 : ["t", "u", "v"] , 9 : ["w", "x", "y", "z"]}

        if len(digits) == 1:
            return num_to_alp[int(digits[0])]
        
        result = []

        for string in self.letterCombinations(digits[1 : ]):
            for alp in num_to_alp[int(digits[0])]:
                result.append(alp + string)
        
        return result