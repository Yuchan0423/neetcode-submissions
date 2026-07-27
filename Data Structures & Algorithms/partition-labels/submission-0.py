class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if s == "":
            return list()
        
        i = 1
        while set(s[: i]) & set(s[i : ]) != set():
            i += 1
        
        return [i] + self.partitionLabels(s[i : ])