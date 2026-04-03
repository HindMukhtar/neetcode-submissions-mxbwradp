class TrieNode: 
    def __init__(self): 
        self.children = {}
        self.is_end = False 

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word: 
            if ch not in node.children: 
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.is_end = True 

    def __traverse__(self, word): 
        node = self.root 
        
        for ch in word: 
            if ch not in node.children:
                return None 
            node = node.children[ch]
        return node 
        
    def search(self, word: str) -> bool:
        node = self.__traverse__(word)

        return node.is_end if node else False 
        
    def startsWith(self, prefix: str) -> bool:
        node = self.__traverse__(prefix)

        return True if node else False 
        