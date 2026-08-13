class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        # [3,1,1]
        XORSum = 0 

        def dfs(i, current_xor): 
            nonlocal XORSum

            if i == len(nums): 
                XORSum += current_xor
                return 

            dfs(i+1, current_xor ^ nums[i])
            dfs(i+1, current_xor)

        dfs(0, 0)

        return XORSum


