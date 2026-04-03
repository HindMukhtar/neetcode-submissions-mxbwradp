class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        # keep max heap of size k. When size exceeds k, remove from heap 
        # That way heap will contain k smallest distances 

        for p in points: 
            heapq.heappush(heap, (-(p[0]**2 + p[1]**2) , p))

            if len(heap) > k: 
                heapq.heappop(heap)

        return [p for d, p in heap]

        