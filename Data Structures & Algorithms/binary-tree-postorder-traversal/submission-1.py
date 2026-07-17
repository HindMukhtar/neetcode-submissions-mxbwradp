# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def recursive(): 
    ans = []

    def postorder(node): 

        if not node: 
            return 

        postorder(node.left)
        postorder(node.right)

        ans.append(node.val)

    postorder(root)


    return ans 

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # postorder - left, right, root 
        # stack -> LIFO 

        # inorder - root, left, right 
        # if we instead do root, right, left 

        # [1,3,7,6,2,5,4]
        # then in reverse order it becomes post order 

        if not root: 
            return []
        
        stack = [root]
        stack2 = []

        while stack: 

            node = stack.pop() 
            stack2.append(node)

            if node.left: 
                stack.append(node.left)

            if node.right: 
                stack.append(node.right)


        ans = []
        while stack2: 

            node = stack2.pop() 
            ans.append(node.val)

        return ans 

            
