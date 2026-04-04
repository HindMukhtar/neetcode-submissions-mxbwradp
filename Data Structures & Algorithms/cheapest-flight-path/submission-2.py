class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = defaultdict(list)
        
        for depart, arrive, price in flights: 
            adj[depart].append((arrive, price))

        heap = ([(0, src, 0)])
        heapq.heapify(heap)

        best = {}

        while heap: 
            price, node, flights_used = heapq.heappop(heap)

            if node == dst: 
                return price

            if flights_used == k+1: 
                continue 

            for nei, cost in adj[node]: 
                new_price = price + cost
                state = (nei, flights_used+1)
                if state not in best or new_price < best[state]: 
                    best[state] = new_price
                    heapq.heappush(heap, (new_price, nei, flights_used+1))

        return -1
