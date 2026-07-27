class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_count = Counter(s1)

        s2_count = Counter(s2[:len(s1)])

        s3_count = {alp : s1_count[alp] - s2_count.get(alp, 0) for alp in s1_count}

        cnt = sum((s3_count[alp] ** 2 for alp in s1_count))

        i = 0
        
        while i + len(s1) < len(s2) and cnt != 0:
            if s2[i] in s1_count:
                cnt = cnt + 2 * s3_count[s2[i]] + 1
                s3_count[s2[i]] += 1
            
            if s2[i + len(s1)] in s1_count:
                cnt = cnt - 2 * s3_count[s2[i + len(s1)]] + 1
                
                s3_count[s2[i + len(s1)]] -= 1
            
            i += 1
        
        return True if cnt == 0 else False

        