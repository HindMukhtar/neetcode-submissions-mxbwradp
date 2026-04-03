# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_dict = {val: i for i, val in enumerate(inorder)}
        pre_idx = 0 

        def dfs(left, right): 
            nonlocal pre_idx

            if left > right: 
                return 

            root_val = preorder[pre_idx] 
            mid = inorder_dict[root_val]
            pre_idx += 1

            node = TreeNode(root_val)
            # repeat on left subtree 
            node.left = dfs(left, mid-1)
            node.right = dfs(mid+1, right)

            return node 

        return dfs(0, len(inorder)-1)             
            
            

