class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0 
        stack = []
        heights.append(0)
        for i, h in enumerate(heights): 
            while stack and heights[stack[-1]] > heights[i]: 
                mid = stack.pop() 
                height = heights[mid]
                left = stack[-1] if stack else -1 
                width = i - left - 1
                maxarea = max(maxarea, height*width)

            stack.append(i)

        return maxarea

            