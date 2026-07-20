class TimeMap:

    def __init__(self):
        self.dic = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.dic:
            self.dic[key] = [[],[]]
        
        self.dic[key][0].append(timestamp)
        self.dic[key][1].append(value)


    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.dic:
            return ""
        
        keylist = self.dic[key][0]

        L = -1
        R = len(keylist)

        while L + 1 < R:
            mid = (L + R) // 2
            if keylist[mid] <= timestamp:
                L = mid
            else:
                R = mid
        
        return self.dic[key][1][L] if L != -1 else ""
        
            
