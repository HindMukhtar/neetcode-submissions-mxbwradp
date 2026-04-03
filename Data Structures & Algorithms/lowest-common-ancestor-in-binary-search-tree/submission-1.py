# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def traverse(node): 
            if not node: 
                return 

            if node.val == p.val or node.val == q.val: 
                return node 

            left = traverse(node.left) 
            right = traverse(node.right) 

            if left and right: 
                return node 

            return left or right 

        return traverse(root) 