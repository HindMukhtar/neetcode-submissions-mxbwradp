class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        min_heap = []

        for p in points: 
            distance = math.sqrt(p[0]**2 + p[1]**2) 
            min_heap.append((distance, p))

        heapq.heapify(min_heap)

        res = []

        for i in range(k): 
            distance, p = heapq.heappop(min_heap)
            res.append(p)

        return res 

        