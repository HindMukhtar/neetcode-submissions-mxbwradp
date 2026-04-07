class Solution:
    def recurse(): 
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

    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[0]*(m+1) for _ in range(n+1)]

        for j in range(m): 
            dp[n][j] = m-j 
        
        for i in range(n): 
            dp[i][m] = n-i

        for i in range(n-1, -1, -1): 
            for j in range(m-1, -1, -1): 
                if word1[i] == word2[j]: 
                    dp[i][j] = dp[i+1][j+1]
                else: 
                    delete = 1 + dp[i+1][j]
                    replace = 1 + dp[i+1][j+1]
                    insert = 1 + dp[i][j+1]
                    dp[i][j] = min(delete, replace, insert)

        return dp[0][0]                   