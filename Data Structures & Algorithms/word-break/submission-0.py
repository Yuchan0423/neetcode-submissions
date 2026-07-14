class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        output = [False] * len(s)
        output.append(True)

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if len(word) <= len(s) - i and s[i: i + len(word)] == word:
                    output[i] = output[i] or output[i + len(word)]
        
        return output[0]
        