class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        visited = set()
        n = len(points)

        heap = [(0, 0)]
        cost = 0 

        while len(visited) < n:

            manhattan_dist, idx = heapq.heappop(heap)
            if idx in visited: 
                continue
            visited.add(idx)
            cost+= manhattan_dist

            for j in range(n):
                if j not in visited:  
                    dist = abs(points[idx][0] - points[j][0]) + abs(points[idx][1] - points[j][1])
                    heapq.heappush(heap, (dist, j))

        return cost