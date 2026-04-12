class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 0 
        for i in range(0,n+1): 
            ans^=i

        for n in nums: 
            ans^=n

        return ans 
        