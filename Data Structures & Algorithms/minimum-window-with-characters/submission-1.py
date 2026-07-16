class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        dict_t = dict()
        dict_s = dict()

        for word in t:
            if word not in dict_t:
                dict_t[word] = 0
            
            dict_t[word] += 1
        
        word_list = list(set(dict_t.keys()))
        word_set = set(dict_t.keys())

        for w in word_list:
            dict_s[w] = 0

        end = 0
        for w in word_list:
            while end < len(s) and dict_s[w] < dict_t[w]:
                if s[end] in word_set:
                    dict_s[s[end]] += 1
                end += 1
            if dict_s[w] < dict_t[w]:
                return ""

        end = end - 1
        
        start = 0
        min_sub = end - start

        actual_start = 0
        actual_end = end

        while end < len(s):
            if s[start] not in word_set:
                start += 1
                if end - start < min_sub:
                    actual_end , actual_start = end, start
                    min_sub = end - start
            else:
                if dict_s[s[start]] > dict_t[s[start]]:
                    dict_s[s[start]] -= 1
                    start += 1
                    if end - start < min_sub:
                        actual_end , actual_start = end, start
                        min_sub = end - start
                else:
                    end += 1
                    while end < len(s) and s[end] != s[start]:
                        if s[end] in word_set:
                            dict_s[s[end]] += 1
                        end += 1
                    start += 1
        
        return s[actual_start : actual_end + 1] 


            