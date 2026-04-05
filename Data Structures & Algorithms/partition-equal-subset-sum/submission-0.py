class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
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

        return dfs(0, 0)