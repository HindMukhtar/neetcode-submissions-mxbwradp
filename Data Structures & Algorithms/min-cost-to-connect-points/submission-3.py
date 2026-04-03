class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        visited = set()
        n = len(points)

        heap = [(0, 0)]
        cost = 0 

        while len(visited) < n:

            manhattan_dist, p0 = heapq.heappop(heap)
            if p0 in visited: 
                continue
            visited.add(p0)
            cost+= manhattan_dist

            for j in range(n):
                if j not in visited:  
                    dist = abs(points[p0][0] - points[j][0]) + abs(points[p0][1] - points[j][1])
                    heapq.heappush(heap, (dist, j))

        return cost