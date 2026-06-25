class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        w = 0 
        r = 0 

        while r < len(nums): 

            if r > w and nums[r] != nums[w]: 
                w += 1 
                nums[w] = nums[r]

            r += 1 

        return w+1