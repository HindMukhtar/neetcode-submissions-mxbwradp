class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        output = []

        def dfs(airport): 
            while adj[airport]: 
                nxt = heapq.heappop(adj[airport])
                dfs(nxt)
            output.append(airport)

        for source, destination in tickets: 
            adj[source].append(destination)

        for airport in adj: 
            heapq.heapify(adj[airport])

        dfs("JFK")

        l = 0 
        r = len(output)-1

        while l < r: 
            output[l], output[r] = output[r], output[l]
            l+=1 
            r-=1

        return output