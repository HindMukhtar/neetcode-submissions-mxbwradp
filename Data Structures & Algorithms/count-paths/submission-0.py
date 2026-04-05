class Solution:
    def recurse(): 
        memo = {}
        def dfs(i, j): 
            if (i,j) in memo: 
                return memo[(i,j)]
            if i < 0 or j < 0 or i > m or j > n: 
                return 0 
            if i == m-1 and j == n-1: 
                return 1 

            dirs = [(1,0), (0,1)]
            memo[(i,j)] = 0 
            for di, dj in dirs: 
                memo[(i,j)] += dfs(i+di, j+dj)

            return memo[(i,j)]
        return dfs(0,0)

    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0] * n for _ in range(m)]
        dirs = [(1,0), (0,1)]
        dp[m-1][n-1] = 1
        for i in range(m-1, -1, -1): 
            for j in range(n-1, -1, -1): 
                for di, dj in dirs: 
                    if i+di < m and j+dj < n: 
                        dp[i][j] += dp[i+di][j+dj]

        return dp[0][0]


             
        