# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = deque([(root, 0)]) 
        res_dict = {}

        while nodes: 
            node, level = nodes.popleft() 
            if node: 
                res_dict.setdefault(level, []).append(node.val)
                nodes.append((node.left, level+1))
                nodes.append((node.right, level+1))

        #res = []
        #for k, v in res_dict.items(): 
        #    res.append(v)

        return [v for v in res_dict.values()]

        