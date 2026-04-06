class Solution:
    def recurse(): 
        memo = {}
        n = len(coins)

        def dfs(i, target): 

            if (i, target) in memo: 
                return memo[(i, target)]
            if target == amount: 
                return 1 
            if target > amount or i >=n : 
                return 0 

            memo[(i, target)] = dfs(i, target+coins[i]) + dfs(i+1, target)

            return memo[(i, target)]

        return dfs(0,0)

    def dp(): 
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n+1)]

        for i in range(n + 1):
            dp[i][amount] = 1

        for i in range(n-1, -1, -1): 
            for t in range(amount, -1, -1): 
                if t+coins[i] <= amount: 
                    dp[i][t] = dp[i][t+coins[i]] + dp[i+1][t]
                else: 
                    dp[i][t] = dp[i+1][t]

        return dp[0][0]

    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0]*(amount+1) 
        dp[amount] = 1

        for i in range(n-1, -1, -1): 
            for t in range(amount, -1, -1): 
                if t+coins[i] <= amount: 
                    dp[t] = dp[t+coins[i]] + dp[t]

        return dp[0]




            
        