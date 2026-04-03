# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, node, d): 
        left = None 
        right = None 
        if node.left: 
            left = self.traverse(node.left, d+1)
        if node.right: 
            right = self.traverse(node.right, d+1)

        if left and right: 
            return max(left, right)
        elif left or right: 
            return left or right 
        else: 
            return d+1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0 
        if root: 
            depth = self.traverse(root, depth)
        
        return depth