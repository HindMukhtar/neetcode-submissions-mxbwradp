class Solution:
    def recusrive(): 
        memo = {}
        n = len(nums)

        def dfs(i, total): 
            if (i, total) in memo: 
                return memo[(i, total)]
            if i == n: 
                return 1 if total == target else 0  

            memo[(i, total)] = dfs(i+1, total+nums[i]) + dfs(i+1, total-nums[i])

            return memo[(i, total)]

        return dfs(0, 0)

    def dp(): 
        n = len(nums)
        S = sum(nums)

        if abs(target) > S: 
            return 0 

        dp = [[0]*(2*S+1) for _ in range(n+1)]
        offset = S

        dp[n][target+offset] = 1 

        for i in range(n-1, -1, -1): 
            for t in range(-S, S+1): 
                ways = 0 
                if -S <= (t+nums[i]) <= S: 
                    ways+= dp[i+1][t+offset+nums[i]]
                if -S <= (t+nums[i]) <= S: 
                    ways+= dp[i+1][t+offset-nums[i]]

                dp[i][t+offset] = ways

        return dp[0][offset]


    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        S = sum(nums)

        if abs(target) > S: 
            return 0 

        dp = [0]*(2*S+1)
        offset = S

        dp[target+offset] = 1 

        for i in range(n-1, -1, -1): 
            nxt = [0]*(2*S+1)
            for t in range(-S, S+1): 
                ways = 0 
                if -S <= (t+nums[i]) <= S: 
                    ways += dp[t+offset+nums[i]]
                if -S <= (t-nums[i]) <= S: 
                    ways += dp[t+offset-nums[i]]

                nxt[t+offset] = ways
            dp = nxt

        return dp[offset]

        