class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutation = []
        used = [False]*len(nums)

        def dfs(): 
            if len(permutation) == len(nums): 
                res.append(permutation.copy())
                return 

            for i in range(len(nums)): 
                if used[i]: 
                    continue
                permutation.append(nums[i])
                used[i] = True 
                dfs()
                used[i] = False
                permutation.pop() 
            
        dfs()

        return res
                
        