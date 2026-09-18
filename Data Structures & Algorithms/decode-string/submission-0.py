class Solution:
    def decodeString(self, s: str) -> str:
        if len(s) == 0:
            return ""

        if "a" <= s[0] and s[0] <= "z":
            return s[0] + self.decodeString(s[1 : ])
        
        else:
            i = 0
            num = ""
            while s[i] != "[":
                num += s[i]
                i += 1
            
            num = int(num)

            cntr = 1
            j = i

            while cntr > 0:
                j += 1
                if s[j] == "[":
                    cntr += 1
                elif s[j] == "]":
                    cntr -= 1
            
            return num * self.decodeString(s[i + 1 : j]) + self.decodeString(s[j + 1 : ])