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

        # remove trailing nulls 
        while output and output[-1] == "null": 
            output.pop()

        return ",".join(output)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: 
            return None

        values = data.split(',')

        nodes = deque([TreeNode(values[0])])
        i = 1 

        while nodes and i < len(values): 

            n = nodes.popleft()
            i += 1 

            if n: 
                if i < len(values) and values[i] != 'null': 
                    left = TreeNode(values[i])
                    n.left = left 
                    nodes.append(left)
                i += 1 
                if i < len(values) and values [i] != 'null': 
                    right = TreeNode(values[i])
                    n.right = right 
                    nodes.append(right)
                i+= 1 
                


        return root 
             


