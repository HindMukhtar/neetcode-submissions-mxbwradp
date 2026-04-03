class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visited = [False]*n

        if len(edges) != n - 1:
            return False

        def dfs(node, parent): 
            if visited[node]: 
                return True 

            visited[node] = True 

            for nei in adj[node]:
                if nei == parent: 
                    continue 
                if dfs(nei, node): 
                    return True 

            return False 

        for n1, n2 in edges: 
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        if dfs(0, None): 
            return False 

        return all(visited)
        