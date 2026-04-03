# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        output = []
        nodes = deque([root]) 

        while nodes: 
            node = nodes.popleft()
            if node: 
                output.append(str(node.val))
                nodes.append(node.left)
                nodes.append(node.right)
            else: 
                output.append("null") 

        return ",".join(output)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = deque() 

        for n in data.split(','): 
            if n != "null": 
                node = nodes.append(TreeNode(int(n)))
            else: 
                nodes.append(None)

        root = nodes.popleft() 
        children = deque([root]) 

        while children: 
            node = children.popleft() 
            if node: 
                left = nodes.popleft() 
                right = nodes.popleft()
                node.left = left 
                node.right = right 
                children.append(left)
                children.append(right)

        return root 
             


