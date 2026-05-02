
class TireNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False
        
class WordDictionary:

    def __init__(self):
        self.root = TireNode()

    def addWord(self, word: str) -> None:
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
        def dfs(root , word):
           
            if not word and root.endOfWord:
                return True 
            if not word and not root.endOfWord:
                return False
            for i in range(len(word)):
                w = word[i]
                if w==".":
                    for j in root.children:
                        if j and dfs(j, word[i+1: ]):
                            return True
                    return False
                else:
                    idx = ord(w) - ord("a")
                    if not root.children[idx]:
                        return False
                    root = root.children[idx]
           
            return root.endOfWord

        return dfs(root , word)
        
