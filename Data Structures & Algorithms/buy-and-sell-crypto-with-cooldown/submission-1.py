class Solution:
    def recurse(prices):
        memo = {}
        n = len(prices)

        def dfs(i, buying): 
            if i >= n: 
                return 0 
            if (i, buying) in memo: 
                return memo[(i, buying)]

            cooldown = dfs(i+1, buying)
            if buying: 
                buy = dfs(i+1, not buying) - prices[i]
                memo[(i,buying)] = max(buy, cooldown)
            else: 
                sell = dfs(i+2, not buying) + prices[i]
                memo[(i,buying)] = max(sell, cooldown)

            return memo[(i, buying)]

        return dfs(0, True)

    def dp(): 
        n = len(prices)
        dp = [[0]*2 for _ in range(n+2)]
        # col = 0 -> buying, col = 1 -> not buying
        dp[0][0] = -prices[0]

        #for i in range(n): 
        #    for j in range(2): 
        #        dp[i][j] = 

    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        n = len(prices)

        def dfs(i, buying): 
            if i >= n: 
                return 0 
            if (i, buying) in memo: 
                return memo[(i, buying)]

            cooldown = dfs(i+1, buying)
            if buying: 
                buy = dfs(i+1, not buying) - prices[i]
                memo[(i,buying)] = max(buy, cooldown)
            else: 
                sell = dfs(i+2, not buying) + prices[i]
                memo[(i,buying)] = max(sell, cooldown)

            return memo[(i, buying)]

        return dfs(0, True)




        