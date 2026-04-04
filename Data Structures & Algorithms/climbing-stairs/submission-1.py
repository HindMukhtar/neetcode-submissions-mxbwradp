class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}

        def dfs(state): 
            if state in memo: 
                return memo[state]
            if state > n: 
                return 0 
            if state == n: 
                return 1

            memo[state] = dfs(state+1) + dfs(state+2)

            return memo[state]


        return dfs(0)


        