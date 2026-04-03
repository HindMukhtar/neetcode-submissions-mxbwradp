class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix_max = [0]*n
        maxval = 0
        for i in range(n):
            maxval = max(maxval, height[i])
            prefix_max[i] = maxval
        
        suffix_max = [0]*n
        maxval = 0
        for i in range(n-1, -1, -1):
            maxval = max(maxval, height[i])
            suffix_max[i] = maxval
        
        water = 0 
        for i in range(n): 
            water += max(0, min(prefix_max[i], suffix_max[i]) - height[i])
        
        return water 
            
            
        