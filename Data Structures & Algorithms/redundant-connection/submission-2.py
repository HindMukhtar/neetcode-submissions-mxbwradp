class UnionFind: 
    def __init__(self, n): 
        self.parent = [i for i in range(n+1)]

    def find(self, x): 
        if self.parent[x] != x: 
            # path compression
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y): 
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y: 
            return False 

        self.parent[root_y] = root_x

        return True 

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        dsu = UnionFind(len(edges))

        for n1, n2 in edges: 
            if not dsu.union(n1,n2): 
                return [n1,n2]

        return edges[len(edges)-1]


        

        