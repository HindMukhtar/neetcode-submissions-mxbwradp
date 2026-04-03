class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        # get frequency of each number. O(n) 
        for n in nums: 
            freqs[n] = freqs.get(n, 0) + 1 
        
        buckets = [[] for _ in range(len(nums)+ 1)]

        # fill bucket with values that have each frequency. O(n)
        for key, value in freqs.items(): 
            buckets[value].append(key)

        # Now return only top k. We want highest frequences so start from the end of the bucket 
        # 4. Collect top k
        output = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                output.append(num)
                if len(output) == k:
                    return output



        
        