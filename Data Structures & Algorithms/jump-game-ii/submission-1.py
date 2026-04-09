class Solution:
    def recurse(): 
        memo = {}

        def dfs(i): 
            if i in memo: 
                return memo[i]
            if i >= len(nums)-1: 
                return 0

            ans = float('inf')
            for j in range(1,nums[i]+1):
                ans = min(ans, 1+dfs(i+j))

            memo[i] = ans 
            return memo[i]

        return dfs(0)

    def dp(): 
        dp = [float('inf')]*(len(nums)+1)
        dp[len(nums)-1] = 0 

        for i in range(len(nums)-1, -1, -1): 
            for j in range(nums[i]+1): 
                if (i+j) < len(nums): 
                    dp[i] = min(dp[i], 1+dp[i+j])

        return dp[0]


    def jump(self, nums: List[int]) -> int:
        res = 0 
        l=r=0 
        farthest = 0 

        while r < len(nums)-1: 
            for i in range(l, r+1): 
                farthest = max(farthest, i + nums[i])
            l = r+1 
            r = farthest 
            res+=1 

        return res 

        