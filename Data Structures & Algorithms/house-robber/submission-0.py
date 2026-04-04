class Solution:
    def rob(self, nums: List[int]) -> int:
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