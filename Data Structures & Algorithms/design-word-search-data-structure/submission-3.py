class TrieNode: 
    def __init__(self): 
        self.children = {}
        self.word_end = False 

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word: 
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]

        curr.word_end = True 

    def _traverse(self, curr, word, idx):

        for i in range(idx, len(word)): 
            if word[i] == '.': 
                for child_node in curr.children.values(): 
                    if self._traverse(child_node, word, i+1): 
                        return True 
                return False 

            if word[i] not in curr.children: 
                return False 
                
            curr = curr.children[word[i]]

        return curr.word_end 
   
    def search(self, word: str) -> bool:
        return self._traverse(self.root,word, 0)

        
