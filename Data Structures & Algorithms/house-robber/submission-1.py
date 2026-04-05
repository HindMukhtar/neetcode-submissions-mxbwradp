class Solution:
    def recursive(): 
        memo = {}
        n = len(nums)
        
        def dfs(house): 
            if house in memo: 
                return memo[house]
            if house >= n: 
                return 0

            memo[house] = max(dfs(house+1), dfs(house+2) + nums[house])

            return memo[house]

        return dfs(0)

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*(n+2)

        for i in range(n-1, -1, -1): 
            dp[i] = max(dp[i+1], dp[i+2] + nums[i])

        return dp[0]
