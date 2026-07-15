class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        # largest sum of any subarray is minimized 

        # example 
        # nums = [2,4,10,1,5], k = 2

        # binary search on answer - we want the minimum possible sum 
        # try different values in search space and define a function 
        # can_sum that returns true or false if we can split array into k 
        # sub arrays with min sum num 

        def can_sum(s): 

            subarrays = 1 
            total = 0 

            for n in nums: 

                total += n 

                if total > s: 
                    subarrays += 1 
                    total = n 

            return subarrays <= k 

        lo = max(nums)
        hi = sum(nums)

        while lo < hi: 
            
            mid = (lo+hi)//2 

            if can_sum(mid):
                hi = mid 
            else: 
                lo = mid + 1 

        return lo  
