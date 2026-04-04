class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        if n == 1: 
            return nums[0]
        
        def dfs(left, right): 
            if (left, right) in memo: 
                return memo[(left, right)]

            if left > right: 
                return 0 

            memo[(left, right)] = max(dfs(left+1, right), dfs(left+2, right) + nums[left])

            return memo[(left, right)]

        return max(dfs(0, n-2), dfs(1, n-1))