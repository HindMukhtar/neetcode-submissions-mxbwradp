class Solution:
    def recurse(): 
        memo = {}
        n = len(s)
        m = len(t)

        def dfs(i, j): 
            if (i,j) in memo: 
                return memo[(i,j)]
            if j == m: 
                return 1 
            if i == n: 
                return 0
            
            if s[i] == t[j]: 
                memo[(i,j)] = dfs(i+1, j+1) + dfs(i+1, j)
            else: 
                memo[(i,j)] = dfs(i+1, j)

            return memo[(i,j)]

        return dfs(0,0)

    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)     

        dp = [[0]*(m+1) for _ in range(n+1)] 
        for i in range(n+1):
            dp[i][m] = 1 

        for i in range(n-1, -1, -1): 
            for j in range(m-1, -1, -1): 
                if s[i] == t[j]: 
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                else: 
                    dp[i][j] = dp[i+1][j]  
        
        return dp[0][0]
