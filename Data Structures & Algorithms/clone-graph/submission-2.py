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
            if node not in visited: 
                n_clone = Node(node.val)
                visited[node] = n_clone
            else: 
                n_clone = visited[node]
            for n in node.neighbors: 
                if n not in visited: 
                    visited[n] = Node(n.val)
                    dfs(n)
                n_clone.neighbors.append(visited[n])
            return n_clone

        return dfs(node)     