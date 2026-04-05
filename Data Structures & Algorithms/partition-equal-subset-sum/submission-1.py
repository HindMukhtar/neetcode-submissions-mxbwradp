class Solution:
    def recursive(): 
        memo = {}
        target = sum(nums)//2 

        if sum(nums)%2 != 0 : 
            return False 

        def dfs(i, total): 

            if total == target: 
                return True  
            if total > target: 
                return False 
            if i == len(nums): 
                return False 
            if (i, total) in memo:
                return memo[(i, total)]

            memo[(i, total)] = dfs(i+1, total) or dfs(i+1, total+nums[i])

            return memo[(i, total)]

    def canPartition(self, nums: List[int]) -> bool:

        target = sum(nums)//2 

        if sum(nums)%2 != 0 : 
            return False 

        dp = [False]*(target+1)
        dp[0] = True 

        for num in nums: 
            for t in range(target, num-1, -1): 
                dp[t] = dp[t] or dp[t-num]
        
        return dp[target]