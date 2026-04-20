class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges_with_idx = [(u, v, w, i) for i, (u, v, w) in enumerate(edges)]
        edges_with_idx.sort(key=lambda x: x[2])
        
        def kruskal(skip=-1, force=-1): 
            parents = [i for i in range(n)]
            rank = [1]*n 

            def find(x): 
                if parents[x]!=x: 
                    parents[x] = find(parents[x])
                return parents[x] 

            def union (x,y): 
                parent_x = find(x)
                parent_y = find(y)

                if parent_x == parent_y: 
                    return False 

                if rank[parent_x] > rank[parent_y]: 
                    parents[parent_y] = parent_x
                    rank[parent_x] +=1 
                else: 
                    parents[parent_x] = parent_y
                    rank[parent_y] += 1 

                return True 

            cost = 0 
            used = 0

            if force != -1: 
                a, b, w, idx = edges_with_idx[force]
                if union(a,b): 
                    cost +=w 
                    used +=1 
                else: 
                    return float('-inf')

            for i, edge in enumerate(edges_with_idx): 
                a, b, w, idx = edge
                if i == skip: 
                    continue 
                if union(a, b): 
                    cost += w 
                    used += 1
                if used == n-1: 
                    break  

            return cost if used == n-1 else float('inf')
 
        base_cost = kruskal()
        critical = []
        pseudo = []
        for i, edge in enumerate(edges_with_idx): 
            a, b, w, idx = edge
            if kruskal(skip=i) > base_cost: 
                critical.append(idx)
            else: 
                if kruskal(force=i) == base_cost: 
                    pseudo.append(idx)

        return [critical, pseudo] 