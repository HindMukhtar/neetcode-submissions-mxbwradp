class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # [1,2,3,1]
        #  0 1 2 3
        
        if k == 0: 
            return False 

        n = len(nums)
        seen = set() 

        for r in range(n): 

            if nums[r] in seen: 
                return True 

            seen.add(nums[r])

            if len(seen) > k: 
                seen.remove(nums[r-k])

        return False 
