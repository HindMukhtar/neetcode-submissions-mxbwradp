class Solution:
    def recursive(): 
        memo = {}
        
        def dfs(i): 
            if i >= len(s): 
                return 1
            if s[i] == "0": 
                return 0
            if i in memo: 
                return memo[i]

            ways = dfs(i+1)
            if (i+1 < len(s)) and (10 <= int(s[i:i+2]) <= 26): 
                ways+=dfs(i+2)

            memo[i] = ways 
            return memo[i]

        return dfs(0)      

    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+2)
        dp[n] = 1
        for i in range(n-1, -1, -1): 
            if s[i] == '0': 
                dp[i] = 0 
            elif i < len(s) and int(s[i:i+2]) >= 10 and int(s[i:i+2]) <= 26: 
                dp[i] = dp[i+1] + dp[i+2]
            else: 
                dp[i] = dp[i+1]

        return dp[0]

      