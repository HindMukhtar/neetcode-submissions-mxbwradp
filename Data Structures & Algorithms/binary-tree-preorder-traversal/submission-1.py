# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def recursive(): 
    ans = []

    def preorder(node): 

        if not node: 
            return 
        
        ans.append(node.val)

        preorder(node.left)
        preorder(node.right)

    preorder(root)

    return ans 


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # peorder - root, left, right 
        # stack - LIFO

        if not root: 
            return []


        stack =[root]
        ans = []

        while stack: 

            node = stack.pop()
            ans.append(node.val)

            if node.right: 
                stack.append(node.right)

            if node.left: 
                stack.append(node.left)

        return ans 