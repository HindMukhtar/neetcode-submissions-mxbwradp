class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # [1, 2, 3, 2, 2]
        # [0, 1, 2, 3, 4]

        # slow pointer 
        # 0->1, 1->2, 2->3, 3->2 -- cycle detected 

        # fast pointer 
        # 0->1->2, 2->3->2 -- cycle detected 

        # iter 1 
        # slow 2->3, fast 2->3->2 
        # iter 2 
        # slow 3->2, fast 2->3->2 -- cycle detected, breaks from loop 

        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast: 
            slow = nums[slow]
            fast = nums[nums[fast]]

        # move one pointer to the start, increment both 
        slow = 0

        while slow != fast: 
            slow = nums[slow]
            fast = nums[fast]

        return slow

        


