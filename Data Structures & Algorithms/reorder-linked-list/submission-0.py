# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # First find the mid point of the list 
        slow = head 
        fast = head 

        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 

        # Now break the list into two 
        first = head 
        second = slow.next 
        slow.next = None 

        # Reverse the second list 
        curr = second 
        prev = None 
        while curr:
            nxt = curr.next 
            curr.next = prev 
            prev = curr 
            curr = nxt 

        second = prev 

        # Iterate through the first list 
        # 0, 1, 2, 3 
        # 6, 5, 4 
        curr1 = first 
        curr2 = second 
        while curr1 and curr2:  
            nxt1 = curr1.next 
            curr1.next = curr2
            nxt2 = curr2.next 
            curr2.next = nxt1 
            curr1 = nxt1
            curr2 = nxt2

        
