class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k 

    def add(self, val: int) -> int:
        self.nums.append(val)
        max_heap = [-x for x in self.nums]
        heapq.heapify(max_heap)

        for i in range(self.k):
            largest = heapq.heappop(max_heap)

        return -largest
        
