class WordDictionary():

    def __init__(self, val = None):
        self.val = val
        self.child = list()

    def addWord(self, word: str) -> None:
        curr = self
        i = 0
        check = 1
        while i < len(word) and check == 1:
            check = 0
            children = curr.child

            for child in children:
                if child.val == word[i]:
                    check = 1
                    curr = child
            i = i + 1
        if check == 0:
            i = i - 1
        
        while i < len(word):
            curr.child.append(WordDictionary(word[i]))
            curr = curr.child[-1]
            i = i + 1
        
        curr.child.append(WordDictionary("0"))
        
    def search(self, word: str) -> bool:
        curr = self
        if word == "":
            for child in curr.child:
                if child.val == "0":
                    return True

            return False
       
        if word[0] != ".":
            for child in curr.child:
                if child.val == word[0]:
                    return child.search(word[1 : ])
            return False
        
        for child in curr.child:
            if child.search(word[1 : ]):
                return True
        
        return False
        