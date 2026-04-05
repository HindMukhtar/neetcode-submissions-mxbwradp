class Solution:
    def recusrive(): 
        memo = {}
        n = len(cost)

        def dfs(state): 
            if state in memo: 
                return memo[state]
            if state >= n: 
                return 0

            memo[state] = cost[state] + min(dfs(state+1), dfs(state+2))

            return memo[state]
        return min(dfs(0), dfs(1))

    def dp(): 
        n = len(cost)
        dp = [0]*(n+2)

        for i in range(n-1, -1, -1): 
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])

        return min(dp[0], dp[1])


    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0]*(n+2)

        cost_one = 0 
        cost_two = 0 

        for i in range(n-1, -1, -1): 
            ans = cost[i] + min(cost_one, cost_two) 
            cost_two = cost_one 
            cost_one = ans 

        return min(cost_one, cost_two)


        