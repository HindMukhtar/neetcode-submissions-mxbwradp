# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge2Lists(self, list1, list2): 
        l1 = list1 
        l2 = list2 
        head = ListNode()
        curr = head 
        while l1 and l2: 
            if l1.val < l2.val: 
                curr.next = l1 
                l1 = l1.next 
            else: 
                curr.next = l2 
                l2 = l2.next
            curr = curr.next 

        if l1: 
            curr.next = l1 
        elif l2: 
            curr.next = l2 

        return head.next 

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: 
            return
        for i in range(1, len(lists)): 
            lists[i] = self.merge2Lists(lists[i-1], lists[i])

        return lists[len(lists) - 1]
        


                


        