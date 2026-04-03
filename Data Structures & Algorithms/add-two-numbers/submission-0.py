# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        prev = None  
        carry = 0     

        while l1 or l2 or carry: 

            a = l1.val if l1 else 0 
            b = l2.val if l2 else 0 

            if a + b + carry >= 10: 
                total = (a + b + carry)%10 
                carry = (a + b + carry)//10 
            else: 
                total = (a + b + carry)
                carry = 0 

            l3 = ListNode(total)
            if not head: 
                head = l3
            if prev: 
                prev.next = l3 

            if l1: 
                l1 = l1.next 
            if l2: 
                l2 = l2.next 
            prev = l3 

        return head

