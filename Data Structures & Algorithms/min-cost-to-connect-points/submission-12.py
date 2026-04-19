class Solution:
    def old(): 
        visited = set()
        n = len(points)

        heap = [(0, 0)]
        cost = 0 

        dist_list = [float('inf')]*len(points)
        dist_list[0] = 0 

        while len(visited) < n:

            idx = 0 
            # get idx of min 
            for j in range(1, len(dist_list)): 
                if dist_list[j] < dist_list[idx] and j not in visited: 
                    idx = j 

            manhattan_dist = dist_list[idx]

            if idx in visited: 
                continue
            visited.add(idx)

            cost+= manhattan_dist

            for j in range(n):
                if j not in visited:  
                    dist = abs(points[idx][0] - points[j][0]) + abs(points[idx][1] - points[j][1])
                    dist_list[j] = min(dist_list[j], dist) 

        return cost

    def old2(): 
        heap = [(0, (points[0][0], points[0][1]))]
        heapq.heapify(heap)
        visited = set()
        total_cost = 0
        
        while heap: 
            cost, p = heapq.heappop(heap)
            x1, y1 = p 

            if (x1, y1) in visited: 
                continue 

            visited.add((x1, y1))
            total_cost += cost 

            for x2, y2 in points: 
                if (x2,y2) not in visited: 
                    new_cost = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(heap, (new_cost, (x2, y2)))

        return total_cost



    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        visited = set()
        n = len(points)

        cost = 0 

        dist_list = [float('inf')]*len(points)
        dist_list[0] = 0 

        while len(visited) < n:

            idx = -1
            # get idx of min 
            for j in range(len(dist_list)): 
                if (idx == -1 or dist_list[j] < dist_list[idx]) and j not in visited: 
                    idx = j 

            visited.add(idx)
            cost+= dist_list[idx]

            for j in range(n):
                if j not in visited:  
                    dist = abs(points[idx][0] - points[j][0]) + abs(points[idx][1] - points[j][1])
                    dist_list[j] = min(dist_list[j], dist) 

        return cost
