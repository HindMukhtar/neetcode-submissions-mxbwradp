class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        freq = {}
        max_freq = 0
        max_val = None  

        for n in nums: 
            freq[n] = freq.get(n, 0) + 1
            if freq[n] > max_freq: 
                max_freq = freq[n]
                max_val = n 

        return max_val 