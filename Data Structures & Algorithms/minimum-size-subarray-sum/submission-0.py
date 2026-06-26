class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        n = len(nums)
        total = 0 
        min_len = float('inf')
        l = 0 

        for r in range(n): 

            total += nums[r]

            while total >= target: 
                total -= nums[l]
                min_len = min(min_len, r-l+1)
                l += 1 

        return min_len if min_len != float('inf') else 0 

            