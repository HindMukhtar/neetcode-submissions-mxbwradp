# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self): 
        self.diameter = 0 

    def traverse(self, node): 
        if not node: 
            return 0 

        left = self.traverse(node.left)
        right = self.traverse(node.right)

        self.diameter = max(self.diameter, left+right)

        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0 

        self.traverse(root)

        return self.diameter 
        