class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0 
        j = n-1 
        best = 0 
        while i < j: 
            area = min(heights[i], heights[j]) * (j - i)
            best = max(best, area)
            if heights[i] < heights[j]: 
                i += 1
            else: 
                j -= 1
        return best 