class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = []
        num_set = set(nums)
        best = 0 
        for i, n in enumerate(nums): 
            if n-1 not in num_set: 
                current = n 
                longest = 1 
                while longest < len(nums): 
                    if current + 1 in num_set: 
                        longest += 1
                        current += 1
                    else: 
                        break 
                best = max(best, longest)
        
        return best 


            
        

            
