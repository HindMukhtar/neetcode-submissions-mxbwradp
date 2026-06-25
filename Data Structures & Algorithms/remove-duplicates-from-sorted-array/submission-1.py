class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        w = 0 

        for r in range(1, len(nums)): 
            if nums[r] != nums[w]: 
                w += 1 
                nums[w] = nums[r]

            r += 1 

        return w+1