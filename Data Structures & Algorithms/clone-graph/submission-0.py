"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node: 
            return None

        visited = {}

        def dfs(node): 
            for n in node.neighbors: 
                if n not in visited: 
                    visited[n] = Node(n.val)
                    dfs(n)
                visited[node].neighbors.append(visited[n])

        visited[node] = Node(node.val)
        dfs(node)

        return visited[node]

        



            





        