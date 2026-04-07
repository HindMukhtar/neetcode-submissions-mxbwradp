class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        n = len(word1)
        m = len(word2)

        def dfs(i,j): 
            if (i,j) in memo: 
                return memo[(i,j)]

            if i == n: 
                return m-j

            if j == m: 
                return n-i
            
            if word1[i] == word2[j]: 
                memo[(i,j)] = dfs(i+1, j+1)
            else: 
                delete = 1 + dfs(i+1, j)
                replace = 1 + dfs(i+1, j+1)
                insert = 1 + dfs(i, j+1)
                memo[(i,j)] = min(delete, replace, insert)

            return memo[(i,j)]

        return dfs(0,0)

                    