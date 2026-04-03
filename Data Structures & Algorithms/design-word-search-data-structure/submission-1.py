class Trie: 
    def __init__(self): 
        self.children = {}
        self.word_end = False 

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word: 
            if ch not in curr.children:
                curr.children[ch] = Trie()
            curr = curr.children[ch]

        curr.word_end = True 

    def __traverse__(self, curr, word, idx):

        for i in range(idx, len(word)): 
            if word[i] == '.': 
                for child_val, child_node in curr.children.items(): 
                    if self.__traverse__(child_node, word, i+1): 
                        return True 
            if word[i] not in curr.children: 
                return False 
            curr = curr.children[word[i]]

        return curr.word_end 

            
    def search(self, word: str) -> bool:
        curr = self.root
        return self.__traverse__(curr,word, 0)

        
