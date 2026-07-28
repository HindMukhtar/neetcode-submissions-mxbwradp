"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def subGrid(n, r, c): 

            if n == 1: 
                return Node(grid[r][c], True, None, None, None, None)

            topLeft = subGrid(n//2, r, c)

            topRight = subGrid(n//2, r, c+n//2)

            bottomLeft = subGrid(n//2, r+n//2, c)

            bottomRight = subGrid(n//2, r+n//2, c+n//2)

            if ((topLeft.val == topRight.val == bottomLeft.val == bottomRight.val) 
            and (topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf)): 
                return Node(topLeft.val, True, None, None, None, None)
            else: 
                return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)

        return subGrid(len(grid), 0, 0)

            

            