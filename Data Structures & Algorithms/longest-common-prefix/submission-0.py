class TrieNode: 
    def __init__(self): 
        self.children = {}
        self.char = None 
        self.is_end = False 

class prefixTree: 
    def __init__(self): 
        self.root = TrieNode() 

    def add_word(self, word): 
        node = self.root 

        for ch in word: 
            if ch not in node.children: 
                node.children[ch] = TrieNode() 
                node.children[ch].char = ch 
            node = node.children[ch]
        
        node.is_end = True 

    def common_prefix(self): 
        node = self.root
        ans = []

        while len(node.children) == 1 and not node.is_end: 
            ch = next(iter(node.children))
            ans.append(ch)
            node = node.children[ch]

        return ''.join(ans)
        

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        pf = prefixTree() 

        for word in strs: 
            pf.add_word(word)

        return pf.common_prefix()


        