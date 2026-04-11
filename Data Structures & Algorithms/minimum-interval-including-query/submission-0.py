class Solution:
    def BF(): 
        res = []

        for q in queries: 
            shortest = float('inf')
            for left, right in intervals:
                if left <= q <= right: 
                    shortest = min(shortest, right-left+1)
            if shortest == float('inf'): 
                res.append(-1)
            else: 
                res.append(shortest) 
        return res

    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x:x[0])
        sorted_queries = list(enumerate(queries))
        sorted_queries.sort(key=lambda x:x[1])
        heap = []
        res = [-1]*len(queries)
        j = 0 

        for i, q in sorted_queries:
            while j < len(intervals) and intervals[j][0] <= q: 
                heapq.heappush(heap, (intervals[j][1]-intervals[j][0]+1, intervals[j][1]))
                j+= 1 
            while heap and heap[0][1] < q: 
                shortest, upper = heapq.heappop(heap)
            if heap: 
                res[i] = heap[0][0]

        return res

        