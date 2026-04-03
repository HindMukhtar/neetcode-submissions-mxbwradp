class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list)
        weights = {}

        for u,v,w in times: 
            adj[u].append(v)
            weights[(u,v)] = w
        
        min_heap = [(0, k)] 
        heapq.heapify(min_heap)
        visited = [False]*n 

        while min_heap: 
            time, node = heapq.heappop(min_heap)
            if visited[node-1]: 
                continue
            visited[node-1] = True 
            if all(visited): 
                return time 
            for nei in adj[node]: 
                if not visited[nei-1]: 
                    heapq.heappush(min_heap, (time+weights[(node, nei)], nei))
        
        return time if all(visited) else -1
        