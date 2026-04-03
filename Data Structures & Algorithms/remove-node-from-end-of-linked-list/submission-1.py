# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # first let's figure out the length of the linked list 
        N = 0 
        curr = head 
        while curr: 
            curr = curr.next 
            N += 1 

        # Now let's find the node we want to remove, it'll be node N - n 
        counter = 0 
        curr = head 
        prev = None 
        while  counter < (N-n): 
            nxt = curr.next 
            prev = curr 
            curr = nxt 
            counter += 1 
        
        if prev: 
            prev.next = curr.next 
        else: 
            head = head.next
        
        return head
            

