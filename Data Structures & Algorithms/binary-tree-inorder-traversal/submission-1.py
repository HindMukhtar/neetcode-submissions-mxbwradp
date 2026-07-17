# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def recursive(): 
    ans = []

    def inorder(node): 

        if not node: 
            return 

        inorder(node.left)
        ans.append(node.val)
        inorder(node.right)

    inorder(root)


    return ans

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # in order traversal 
        # left, root, right 

        ans = []
        stack = []
        curr = root 

        while curr or stack: 

            while curr: 
                stack.append(curr)
                curr = curr.left 

            if stack: 
                curr = stack.pop() 
                ans.append(curr.val)
                curr = curr.right 

        return ans 

