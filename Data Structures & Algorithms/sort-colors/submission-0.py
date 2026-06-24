class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Example 
        # [1,0,1,2]
        # [0,1,1,2]

        # Approach 
        # want to move 0 to the left and 2 to the right 
        # if 1 then don't do anything 
        # Use 3 pointers, when we swap with left then increment left counter 

        lo = 0 
        mid = 0 
        hi = len(nums) - 1 

        while mid <= hi: 

            if nums[mid] == 0: 
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1 
                mid += 1 
            elif nums[mid] == 2: 
                nums[hi], nums[mid] = nums[mid], nums[hi]
                hi -= 1 
            else: 
                mid += 1

        return nums