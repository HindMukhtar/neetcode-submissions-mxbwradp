class Solution:
    def recurse(): 
        memo = {}
        n = len(nums)
        if n == 1: 
            return nums[0]
        
        def dfs(left, right): 
            if (left, right) in memo: 
                return memo[(left, right)]

            if left >= right: 
                return 0 

            memo[(left, right)] = max(dfs(left+1, right), dfs(left+2, right) + nums[left])

            return memo[(left, right)]

        return max(dfs(0, n-1), dfs(1, n))

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]

        def rob_line(arr): 
            dp = [0]*(len(arr)+2) 

            for i in range(len(arr)-1, -1, -1): 
                dp[i] = max(arr[i] + dp[i+2], dp[i+1])

            return dp[0]

        return max(rob_line(nums[:-1]), rob_line(nums[1:]))