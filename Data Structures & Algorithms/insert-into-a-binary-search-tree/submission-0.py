# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        # insert to BST 
        # BST - everything to the right is greater than root, everything to the left is 
        # less than root 
        # all values in the subtree must satisfy this property 

        if not root: 
            return TreeNode(val)

        node = root 

        while node: 

            if val < node.val: 
                if not node.left: 
                    node.left = TreeNode(val)
                    return root 
                node = node.left 
            else:
                if not node.right: 
                    node.right = TreeNode(val)
                    return root 
                node = node.right 

        return root 

