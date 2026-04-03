class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()

        for i in range(rows): 
            for j in range(cols): 
                if grid[i][j] == 0: 
                    queue.append((i,j)) 

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue: 
            i, j = queue.popleft() 
            for di, dj in dirs: 
                ni, nj = i+di, j+dj 
                if ni>=0 and ni<rows and nj>=0 and nj<cols: 
                    if grid[ni][nj] == (2**31-1): 
                        grid[ni][nj] = grid[i][j] + 1 
                        queue.append((ni, nj))


        