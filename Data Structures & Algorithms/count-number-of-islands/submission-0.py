class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False]*cols for _ in range(rows)]
        num_islands = 0 

        def dfs(i, j): 

            if i < 0 or j < 0 or i >= rows or j >= cols: 
                return False

            if visited[i][j]: 
                return False

            visited[i][j] = True 

            if grid[i][j] == "0": 
                return False 

            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
            
            return True 


        for i in range(rows): 
            for j in range(cols): 
                if dfs(i, j): 
                    num_islands += 1 
        return num_islands 