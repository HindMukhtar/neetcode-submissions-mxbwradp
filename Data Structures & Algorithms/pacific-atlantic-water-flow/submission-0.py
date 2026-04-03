class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set() 
        atlantic = set() 

        def dfs(i, j, visited, prev): 
            
            if i < 0 or j < 0 or i >= rows or j >= cols: 
                return 
            if (i,j) in visited: 
                return 
            if heights[i][j] < prev: 
                return

            visited.add((i,j))

            dfs(i+1, j, visited, heights[i][j])
            dfs(i-1, j, visited, heights[i][j])
            dfs(i, j+1, visited, heights[i][j])
            dfs(i, j-1, visited, heights[i][j])
            

        for i in range(rows): 
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, cols-1, atlantic, heights[i][cols-1])


        for j in range(cols): 
            dfs(0, j, pacific, heights[0][j])
            dfs(rows-1, j, atlantic, heights[rows-1][j])
        
        output = [list(t) for t in (pacific & atlantic)]

        return output