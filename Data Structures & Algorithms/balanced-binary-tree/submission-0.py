# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self): 
        self.isBalance = True

    def traverse(self, node): 
        if not node: 
            return 0 

        left = self.traverse(node.left)
        right = self.traverse(node.right)

        if abs(left - right) > 1: 
            self.isBalance = False 

        return 1+ max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root: 
            return True 

        self.traverse(root)

        return self.isBalance
        