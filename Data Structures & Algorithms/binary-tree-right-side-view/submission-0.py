# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        nodes = deque([(root, 0)]) 
        levels = set() 
        res = []

        while nodes: 
            node,level = nodes.popleft() 
            if node: 
                if level not in levels: 
                    res.append(node.val)
                levels.add(level)
                nodes.append((node.right, level+1))
                nodes.append((node.left, level+1))

        return res 
        