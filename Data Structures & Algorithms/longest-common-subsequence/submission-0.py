class Solution:
    def recursive(): 
        memo = {}
        n = len(text1)
        m = len(text2)

        def dfs(i, j): 
            if (i,j) in memo: 
                return memo[(i,j)]
            if i >= n or j >= m: 
                return 0 

            if text1[i] == text2[j]: 
                memo[(i,j)] = 1+dfs(i+1, j+1)
            else: 
                memo[(i,j)] = max(dfs(i, j+1), dfs(i+1, j))

            return memo[(i,j)]

        return dfs(0,0)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n-1, -1, -1): 
            for j in range(m-1, -1, -1): 
                if text1[i] == text2[j]: 
                    dp[i][j] = 1 + dp[i+1][j+1]
                else: 
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])

        return dp[0][0]

