class TrieNode: 
    def __init__(self): 
        self.children = {}
        self.word = None 

class Trie: 
    def __init__(self): 
        self.root = TrieNode() 

    def add_word(self, word): 
        curr = self.root 

        for ch in word: 
            if ch not in curr.children: 
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]

        curr.word = word 

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        word_trie = Trie()
        for w in words: 
            word_trie.add_word(w)

        rows = len(board)
        cols = len(board[0])

        visited = [[False]*cols for _ in range(rows)]
        output = set()

        def dfs(i, j, curr): 

            if i < 0 or j < 0 or i >= rows or j >= cols: 
                return 

            if visited[i][j]: 
                return 

            if board[i][j] not in curr.children: 
                return 

            visited[i][j] = True 
            curr = curr.children[board[i][j]]

            if curr.word: 
                output.add(curr.word)
                curr.word = None

            dfs(i-1, j, curr)
            dfs(i+1, j, curr)
            dfs(i, j-1, curr)
            dfs(i, j+1, curr)

            visited[i][j] = False 

        for i in range(rows): 
            for j in range(cols): 
                dfs(i, j, word_trie.root)

        return list(output)       