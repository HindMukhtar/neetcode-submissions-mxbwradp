class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # smallest positive number that is not present 
        # the smallest positive number has to be between 1 and len(nums) + 1 
        # array is unsorted - we can't sort if we want O(n) time 

        # BF solutions 
        # 1 - create a hash of the array, then loop through from 1 to len(nums) + 1 
        # find the first number that is not in the hash - O(n) time and O(n) space 

        # for O(1) space, sort the array (O(nlogn)) then find the first positive value 
        # where where there is a gap i.e val - val-1 > 1 

        # how can we have O(1) space and O(n) time? 
        # nums = [1,2,4,5,6,3,1]
        #         1 2 3 4 5 6 7

        # better sorting approach for each value in n, place is nums[n+1]
        # so keep swapping until we no longer can then move on to the next one 
        # this pass would be O(n)
        # then do a second pass and find the first idx that has an invalid value (-1)

        # how to handle negative values? 

        n = len(nums)
        
        for i in range(len(nums)): 

            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]: 
                correct_idx = nums[i]
                nums[i], nums[correct_idx - 1] = nums[correct_idx - 1], nums[i]

        for i, num in enumerate(nums): 
            if num != i+1: 
                return i+1 


        return len(nums)+1



