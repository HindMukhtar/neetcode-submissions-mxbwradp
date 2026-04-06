class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        n = len(nums)

        def dfs(i, total): 
            if (i, total) in memo: 
                return memo[(i, total)]
            if i > n: 
                return 0 
            if total == target and i == n: 
                return 1 

            memo[(i, total)] = dfs(i+1, total+nums[i-1]) + dfs(i+1, total-nums[i-1])

            return memo[(i, total)]

        return dfs(0, 0)

        