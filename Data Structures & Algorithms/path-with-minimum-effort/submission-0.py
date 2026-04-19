class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        visited = set() 

        minheap = [(0, 0, 0)]
        heapq.heapify(minheap)

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while minheap: 
            curr_effort, r, c = heapq.heappop(minheap)
            
            if (r,c) in visited: 
                continue 

            visited.add((r,c))

            if r == rows-1 and c == cols-1: 
                return curr_effort 

            for dr, dc in dirs: 
                nr = r + dr
                nc = c + dc 
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr,nc) in visited: 
                    continue 
                new_effort = max(curr_effort, abs(heights[r][c] - heights[nr][nc]))
                heapq.heappush(minheap, (new_effort, nr, nc))
            