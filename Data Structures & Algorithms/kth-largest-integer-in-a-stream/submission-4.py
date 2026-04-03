class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.min_heap = []
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)
        count = 0 
        while count < self.k and max_heap: 
            heapq.heappush(self.min_heap, -heapq.heappop(max_heap)) 
            count += 1
        

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k: 
            heapq.heappush(self.min_heap, val)
        elif self.min_heap and val > self.min_heap[0]: 
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, val)

        return self.min_heap[0]
        
