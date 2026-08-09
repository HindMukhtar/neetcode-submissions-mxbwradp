class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips.sort(key=lambda x: x[1])

        min_heap = []
        size = 0 

        for numPassengers, start, end in trips: 

            while min_heap and min_heap[0][0] <= start: 
                e, p = heapq.heappop(min_heap)
                size -= p 

            if numPassengers + size <= capacity: 
                heapq.heappush(min_heap, (end, numPassengers))
                size += numPassengers 
            else: 
                return False 

        return True 