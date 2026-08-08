class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        max_heap = []

        for count, char in [(a, 'a'), (b, 'b'), (c, 'c')]: 
            if count > 0: 
                heapq.heappush(max_heap, (-count, char))

        res = []

        while max_heap: 

            freq, ch = heapq.heappop(max_heap)

            if len(res) >= 2 and res[-1] == ch and res[-2] == ch: 
                if not max_heap: 
                    break 
                freq2, ch2 = heapq.heappop(max_heap)
                res.append(ch2)
                if freq2 + 1 < 0: 
                    heapq.heappush(max_heap, (freq2 + 1, ch2))
                heapq.heappush(max_heap, (freq, ch))
                
            else: 
                res.append(ch)
                if freq + 1 < 0: 
                    heapq.heappush(max_heap, (freq + 1, ch))


        return ''.join(res) 