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
        dp = [[0, 0] for _ in range(n+2)]
        # dp[i][0] -> can buy
        # dp[i][1] -> holding stock

        for i in range(n-1, -1, -1): 
            # buying
            buy = dp[i+1][1] - prices[i]
            cooldown = dp[i+1][0]
            dp[i][0] = max(buy, cooldown) 
            # not buying 
            sell = dp[i+2][0] + prices[i]
            cooldown = dp[i+1][1]
            dp[i][1] = max(sell, cooldown)

        return dp[0][0]

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n+2)]
        # dp[i][0] -> can buy
        # dp[i][1] -> holding stock
        nxt_buy = 0 # dp[i+1][1]
        nxt2_buy = 0  #dp[i+2][0]
        nxt_hold = 0 

        for i in range(n-1, -1, -1): 
            # can buy 
            can_buy = max(nxt_hold - prices[i], nxt_buy) 
            # can't buy
            holding = max(nxt2_buy + prices[i], nxt_hold)

            nxt2_buy = nxt_buy 
            nxt_buy = can_buy 
            nxt_hold = holding

        return nxt_buy





        