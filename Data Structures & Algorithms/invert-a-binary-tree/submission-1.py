# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        stack = [root] if root else []

        while stack: 
            node = stack.pop() 
            left = node.left 
            right = node.right 
            if left: 
                stack.append(left)
            if right: 
                stack.append(right)
            node.left = right 
            node.right = left 
            
        return root