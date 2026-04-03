class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        heap = [(max(0, grid[0][0]), 0, 0)]
        visited = set()
        heapq.heapify(heap)

        while heap: 
            t, i, j = heapq.heappop(heap)
            if i == rows-1 and j == cols-1: 
                return t 
            if (i,j) in visited: 
                continue 
            visited.add((i,j))
            dirs = [(1,0), (-1,0), (0,1), (0,-1)]

            for di, dj in dirs: 
                ni, nj = i+di, j+dj 
                if 0 <= ni < rows and 0 <= nj < cols: 
                    heapq.heappush(heap, (max(t, grid[ni][nj]), ni, nj))

        return t 

        