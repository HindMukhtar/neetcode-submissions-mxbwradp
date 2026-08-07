class Solution:
    def reorganizeString(self, s: str) -> str:
        
        ch_freq = {}

        for ch in s: 
            ch_freq[ch] = ch_freq.get(ch, 0) + 1 

        max_heap = []

        for ch, freq in ch_freq.items(): 
            heapq.heappush(max_heap, (-freq, ch))

        res = []
        prev = None 

        while max_heap: 

            freq, ch = heapq.heappop(max_heap)
            res.append(ch)
            
            if prev: 
                heapq.heappush(max_heap, prev)

            new_freq = freq + 1 
            if new_freq < 0: 
                prev = (new_freq, ch)
            else: 
                prev = None


        return ''.join(res) if len(res) == len(s) else ''
