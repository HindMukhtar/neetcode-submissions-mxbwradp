class Solution:
    def recursive(): 
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

    def dp():
        dp = [0]*(n+2)
        dp[n] = 1

        for i in range(n-1, -1, -1): 
            dp[i] = dp[i+1] + dp[i+2]

        return dp[i]

    def climbStairs(self, n: int) -> int:

        one_step = 1 
        two_step = 0 

        for i in range(n-1, -1, -1): 
            ans = one_step + two_step 
            two_step = one_step 
            one_step = ans 

        return ans


        