class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
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

        