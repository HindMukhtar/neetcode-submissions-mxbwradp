class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # [1,2,3,1]
        #  0 1 2 3
        
        if k == 0: 
            return False 

        n = len(nums)
        l = 0 
        seen = set() 

        for r in range(n): 

            if nums[r] in seen: 
                return True 

            if r-l == k: 
                seen.remove(nums[l])
                l += 1 

            seen.add(nums[r])

        return False 
