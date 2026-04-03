class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1: 

            stone_a = -heapq.heappop(max_heap)
            stone_b = -heapq.heappop(max_heap)

            if stone_a > stone_b: 
                heapq.heappush(max_heap, -(stone_a - stone_b))
            elif stone_b > stone_a: 
                heapq.heappush(max_heap, -(stone_b - stone_a))

        return -max_heap[0] if max_heap else 0 

        