class Solution:
    def recurse(): 
        memo = {}
        if len(nums) == 1: 
            return nums[0]

        def dfs(i): 
            if i in memo: 
                return memo[i]
            if i == len(nums): 
                return 0 
            
            memo[i] = max(nums[i], nums[i]+ dfs(i+1)) 

            return memo[i]

        best = 0 

        for i in range(len(nums)): 
            best = max(best, dfs(i))

        return best 

    def maxSubArray(self, nums: List[int]) -> int:

        prev_sum = nums[-1]
        best = prev_sum

        for i in range(len(nums)-2, -1, -1):
            curr_sum = max(nums[i], nums[i]+prev_sum) 
            prev_sum = curr_sum
            best = max(best, curr_sum)
        
        return best