class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def count(strs):
            dic = {}
            for char in strs:
                dic[char] = 1 if char not in dic else dic[char] + 1
            string = ""
            key = dic.keys()
            key = sorted(key)
            for letter in key:
                while dic[letter] > 0:
                    dic[letter] -= 1
                    string += letter
                
            return string

        anagram_group = {}
        for char in strs:
            if count(char) in anagram_group:
                anagram_group[count(char)].append(char)
            else:
                anagram_group[count(char)] = []
                anagram_group[count(char)].append(char)
        
        return list(anagram_group.values())
            
        