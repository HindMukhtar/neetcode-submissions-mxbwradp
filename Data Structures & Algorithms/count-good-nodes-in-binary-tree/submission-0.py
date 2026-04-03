# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        nodes = deque([(root, root.val)]) 
        res = []

        while nodes: 
            node, max_val = nodes.popleft() 

            if node: 
                if node.val >= max_val: 
                    res.append(node.val) 
                nodes.append((node.left, max(max_val, node.val)))
                nodes.append((node.right, max(max_val, node.val)))

        return len(res)

        
        