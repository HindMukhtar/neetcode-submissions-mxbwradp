class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = [i for i in range(n)]
        visited = [False]*n 
        adj = defaultdict(list)
        count = 0 

        def dfs(node): 
            if visited[node]: 
                return False 

            visited[node] = True 

            for nei in adj[node]: 
                if not dfs(nei): 
                    continue

            return True 


        for n1, n2 in edges: 
            adj[n1].append(n2)
            adj[n2].append(n1)

        for node in nodes: 
            if dfs(node): 
                count +=1

        return count 
        