class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if s == "":
            return list()
        
        count_list = Counter(s)
        
        cnt = count_list[s[0]]
        i = 0
        till = {s[0]}

        while cnt > 0:
            if s[i] not in till:
                till.add(s[i])
                cnt += count_list[s[i]]

            cnt -= 1
            i += 1
        
        
        return [i] + self.partitionLabels(s[i : ])