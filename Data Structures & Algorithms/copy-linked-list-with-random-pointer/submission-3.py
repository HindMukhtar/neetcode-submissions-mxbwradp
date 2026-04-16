"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def first_solution(): 
        if not head: 
            return None 

        curr = head 
        nodes = {}
        nodes[curr] = Node(curr.val)
        head2 = nodes[curr]

        while curr: 
            # create copy of node and store in dict if it hasn't already been created 
            if curr not in nodes: 
                nodes[curr] = Node(curr.val)
            
            # Now let's check the next pointer 
            if curr.next: 
                if curr.next in nodes: 
                    nxt = nodes[curr.next]
                else: 
                    nxt = Node(curr.next.val)
                    nodes[curr.next] = nxt 
            else: 
                nxt = None 
            
            # Repeat for random pointer 
            if curr.random: 
                if curr.random in nodes: 
                    rdm = nodes[curr.random]
                else: 
                    rdm = Node(curr.random.val)
                    nodes[curr.random] = rdm 
            else: 
                rdm = None 

            nodes[curr].next = nxt 
            nodes[curr].random = rdm 

            curr = curr.next 

        return head2
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head: 
            return None 

        nodes = {}
        curr = head 

        while curr: 

            if curr not in nodes: 
                nodes[curr] = Node(curr.val)

            if curr.next: 
                if curr.next not in nodes: 
                    nodes[curr.next] = Node(curr.next.val)
                nodes[curr].next = nodes[curr.next]

            if curr.random: 
                if curr.random not in nodes: 
                    nodes[curr.random] = Node(curr.random.val)
                nodes[curr].random = nodes[curr.random]

            curr = curr.next 

        return nodes[head]        