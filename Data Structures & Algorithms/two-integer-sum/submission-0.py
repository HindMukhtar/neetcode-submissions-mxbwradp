class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums): 
            b = target - n
            if b in seen: 
                return[seen[b], i]
            seen[n] = i
        return 