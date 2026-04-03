# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head, k): 
        curr = head 
        prev = None 
        count = 0
        while curr and count < k: 
            nxt = curr.next 
            curr.next = prev 
            prev = curr
            curr = nxt 
            count += 1 
        
        return curr, prev, head 

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head 
        listhead = None 
        prev = None 
        while curr: 
            # check if we have at least k nodes 
            count = 0 
            temp = curr 
            while temp and count < k: 
                count += 1 
                temp = temp.next

            if count >= k: 
                curr, head, tail = self.reverseList(curr, k)
                if not listhead: 
                    listhead = head
                    
                if prev: 
                    prev.next = head 
                prev = tail 

            else: 
                prev.next = curr 
                curr = curr.next
                break
            
        return listhead
     