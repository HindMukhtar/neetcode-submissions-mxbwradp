class Solution:
    def dp(): 
        dp = [float('inf')]*(amount+1) 
        dp[0] = 0 

        for a in range(1, amount+1): 
            for c in coins: 
                if a-c >=0: 
                    dp[a] = min(dp[a], 1+dp[a-c])

        return -1  if dp[amount] == float('inf') else dp[amount]

    def recusrse(): 
        memo = {}

        def dfs(i):
            if i in memo: 
                return memo[i]
            if i > amount: 
                return float('inf') 
            if i == amount: 
                return 0

            memo[i] = float('inf')
            for c in coins: 
                memo[i] = min(memo[i], 1+dfs(i+c))

            return memo[i]

        ans = dfs(0)

        return -1 if ans == float('inf') else ans


    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0 

        for a in range(1, amount+1): 
            for c in coins:
                if (a-c) >= 0: 
                    dp[a] = min(dp[a], 1+dp[a-c])

        return -1 if dp[amount] == float('inf') else dp[amount]




                    