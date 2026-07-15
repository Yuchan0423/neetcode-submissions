class TreeNode:

    def __init__(self,val = None):
        self.word = False
        self.child = dict()
class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.child:
                cur.child[w] = TreeNode()
            
            cur = cur.child[w]
        
        cur.word = True
            
    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w not in cur.child:
                return False
            
            cur = cur.child[w]
        
        return cur.word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            if w not in cur.child:
                return False
            
            cur = cur.child[w]

        return True
        
        