class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        # Use topological sort to determine order for rows and columns 

        def topsort(conditions): 
            adj = defaultdict(list)
            indeg = {i:0 for i in range(1,k+1)}

            for above, below in conditions: 
                adj[above].append(below)
                indeg[below]+=1 

            dq = deque([k for k, v in indeg.items() if v == 0])
            res = []

            while dq: 
                val = dq.popleft()
                res.append(val)

                for nei in adj[val]: 
                    indeg[nei]-=1 
                    if indeg[nei] == 0: 
                        dq.append(nei)

            return res 

        row_order = topsort(rowConditions)
        col_order = topsort(colConditions)

        if not row_order or not col_order: 
            return []

        row_map = {val:idx for idx,val in enumerate(row_order)}
        col_map = {val:idx for idx,val in enumerate(col_order)}

        matrix = [[0]*k for _ in range(k)]

        for val, row in row_map.items(): 
            col = col_map[val]
            matrix[row][col] = val

        return matrix 
        