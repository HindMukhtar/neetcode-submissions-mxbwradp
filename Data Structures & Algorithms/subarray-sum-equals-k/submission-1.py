class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix = {0:1}
        ans = 0 
        total = 0 

        # sum = prefix[right] - prefix[left]
        # k = prefix[right] - prefix[left]
        # prefix[left] = prefix[right] - k 

        for n in nums: 
            total += n
            if total-k in prefix: 
                ans += prefix[total-k] 

            prefix[total] = prefix.get(total, 0) + 1 

        return ans 
        