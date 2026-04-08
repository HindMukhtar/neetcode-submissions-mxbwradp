class Solution:
    def recurse(): 
        memo = {}
        n = len(nums)-1
        def dfs(i): 
            if i in memo: 
                return memo[i]
            if i >= n: 
                return True
            if nums[i] == 0: 
                return False 
                
            ans = False 
            
            for j in range(nums[i]+1): 
                ans = ans or dfs(i+j)

            memo[i] = ans 

            return memo[i]

        return dfs(0)

    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]*(len(nums)) 
        dp[-1] = True 

        for i in range(len(nums)-2, -1, -1): 
            for j in range(1, nums[i]+1): 
                if j < len(nums) and (i+j) < len(nums): 
                    dp[i] =  dp[i] or dp[i+j]
        return dp[0]

        