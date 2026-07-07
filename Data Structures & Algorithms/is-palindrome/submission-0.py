class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric_s = list()
        for char in s:
            if "0" <= char <= "9":
                alphanumeric_s.append(char)
            elif "a" <= char <= "z":
                alphanumeric_s.append(char)
            elif "A" <= char <= "Z":
                alphanumeric_s.append(char.lower())
        
        for i in range(len(alphanumeric_s) // 2):
            if alphanumeric_s[i] != alphanumeric_s[len(alphanumeric_s) - i - 1]:
                return False
        
        return True
                
        