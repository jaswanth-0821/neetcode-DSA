class TireNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False
class PrefixTree:

    def __init__(self):
        self.root = TireNode()

    def insert(self, word: str) -> None:
        root = self.root
        
        for i in word:
            idx = ord(i) - ord("a")
         
            if root.children[idx]:
                root = root.children[idx]
                continue
           
            root.children[idx] = TireNode()
            root = root.children[idx]
        root.endOfWord =True

    def search(self, word: str) -> bool:
        root = self.root
        for w in word:
            idx = ord(w) - ord("a")
            if not root.children[idx]:
                return False
            root = root.children[idx]
        if not root.endOfWord:
            return False
        return True
    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for w in prefix:
            idx = ord(w) - ord("a")
           
            if not root.children[idx]:
                return False
            root = root.children[idx]
        return True
        