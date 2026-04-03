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

    def stack(self, root): 
        if not root: 
            return 0

        stack = [(root, 0)]
        max_depth = 0 

        while stack: 
            node, d = stack.pop() 
            if node:
                max_depth = max(max_depth, d)
                stack.append((node.left, d+1))
                stack.append(node.right, d+1)

        return max_depth 



    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0 
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))