class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1 

        while lo < hi: 
            mid = (lo+hi)//2 

            if nums[mid] == target: 
                return mid

            elif nums[lo] <= nums[mid]: 
                # if left half is sorted 
                if target < nums[mid] and target >= nums[lo]: 
                    hi = mid - 1
                else: 
                    lo = mid + 1 
            else: 
                # otherwise right half is sorted 
                if target > nums[mid] and target <= nums[hi]: 
                    lo = mid + 1 
                else: 
                    hi = mid - 1 

        
        return lo if nums[lo] == target else -1

            