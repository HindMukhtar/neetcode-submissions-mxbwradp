class trieNode: 
    def __init__(self): 
        self.children = {}
        self.is_end = False 

class trie: 
    def __init__(self): 
        self.root = trieNode() 

    def add_word(self, word): 

        node = self.root 

        for ch in word: 
            if ch not in node.children: 
                node.children[ch] = trieNode() 
            node = node.children[ch]

        node.is_end = True 

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        dict_trie = trie()

        for word in dictionary: 
            dict_trie.add_word(word)

        n = len(s)
        dp = [0]*(n+1)

        for i in range(n-1, -1, -1): 

            dp[i] = 1 + dp[i+1]

            node = dict_trie.root 

            for j in range(i, n): 
                if s[j] not in node.children: 
                    break 
                
                node = node.children[s[j]]

                if node.is_end: 
                    dp[i] = min(dp[i], dp[j+1])

        return dp[0]





        