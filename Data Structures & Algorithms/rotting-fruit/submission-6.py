class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()

        fruit_count = 0 

        for i in range(rows): 
            for j in range(cols): 
                if grid[i][j] == 2: 
                    queue.append((i,j, 0))
                elif grid[i][j] == 1: 
                    fruit_count+=1 

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        time = 0 

        while queue: 
            i, j, time = queue.popleft() 
            for di, dj in dirs: 
                ni, nj = i+di, j+dj 
                if ni>=0 and ni<rows and nj>=0 and nj<cols: 
                    if grid[ni][nj] == 1: 
                        grid[ni][nj] = 2
                        queue.append((ni,nj,time+1))
                        fruit_count-=1

        return time if fruit_count==0 else -1



        