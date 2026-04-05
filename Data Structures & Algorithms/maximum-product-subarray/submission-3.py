class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        res = nums[0]
        for i in range(1, len(nums)): 
            x = nums[i]
            temp_max = max(x, x*curr_max, x*curr_min)
            temp_min = min(x, x*curr_max, x*curr_min)

            curr_max = temp_max
            curr_min = temp_min

            res = max(res, curr_max)

        return res 
