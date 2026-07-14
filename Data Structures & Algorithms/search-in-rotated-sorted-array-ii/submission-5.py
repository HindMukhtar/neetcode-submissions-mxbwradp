class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        # rotated sorted array - find which side of the array is sorted 

        # example 
        # nums = [3,4,4,5,6,1,2,2]
        #         0 1 2 3 4 5 6 7 

        # if nums[mid] >= nums[lo] -> left side is sorted 
        # else right side is sorted 
        # now to look for target. If target is between lo and mid then check 
        # there 
        # otherwise we need to check the unsorted side  

        lo = 0 
        hi = len(nums) - 1 

        while lo <= hi: 

            mid = (lo+hi)//2 

            if nums[mid] == target: 
                return True 
            elif nums[lo] == nums[mid] == nums[hi]: 
                lo += 1 
                hi -= 1 
            elif nums[mid] >= nums[lo]: 
                # left side is sorted 
                if nums[lo] <= target < nums[mid]:
                    hi = mid -1
                else: 
                    # its in the other side 
                    lo = mid + 1 
            else: 
                # right side is sorted 
                if nums[mid] < target <= nums[hi]: 
                    lo = mid + 1
                else: 
                    # its in the other side 
                    hi = mid - 1 

        return False
        