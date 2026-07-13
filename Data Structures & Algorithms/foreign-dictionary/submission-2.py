class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        order = dict() # for order
        checklist = list() # to keep track of words
        checklist.append(words)
        letters = list()

        for word in words:
            for char in word:
                if char not in letters:
                    letters.append(char)

        while checklist:
            sliced = checklist.pop()
            small_order = list() # smaller order
            small_words = list() # to append to checklist
            initial_check = 1
            prev_word = ""
            for word in sliced:
                if word[0] != prev_word and word[0] in small_order:
                    return ""
                    
                elif word[0] not in small_order:
                    initial_check = 0
                    if small_words:
                        checklist.append(small_words)
                    small_words = list()
                    small_order.append(word[0])

                elif len(word) == 1 and initial_check == 1:
                    return ""
                
                if len(word) >= 2:
                        small_words.append(word[1:])
                        initial_check = 1
                
                if small_words:
                    checklist.append(small_words)

                prev_word = word[0]
            

            for i in range(len(small_order) - 1):
                for j in range(i + 1, len(small_order)):
                    if small_order[i] not in order:
                        order[small_order[i]] = []
                    if small_order[j] not in order[small_order[i]]:
                        order[small_order[i]].append(small_order[j])
            
            if len(small_order) >= 2 and small_order[-1] not in order:
                order[small_order[-1]] = []
        
        indegree = {w: 0 for w in order}
        for node in order:
            for neighbor in order[node]:
                indegree[neighbor] = indegree.get(neighbor, 0) + 1

        path = list()

        words = list(indegree.keys())


        while indegree:
            check = 1
            for parent in words:
                if indegree[parent] == 0:
                    check = 0
                    path.append(parent)
                    indegree.pop(parent)
                    for child in order[parent]:
                        if child in indegree:
                            indegree[child] -= 1
        
            if check == 1:
                return ""

            words = list(indegree.keys())

        output = ""

        for word in letters:
            if word not in path:
                output = output + word

        for word in path:
            output = output + word 
        
        return output
        