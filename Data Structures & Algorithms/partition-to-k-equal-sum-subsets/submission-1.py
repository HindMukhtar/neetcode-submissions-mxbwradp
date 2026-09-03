class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        if sum(nums) % k != 0: 
            return False 

        target = sum(nums)//k 

        nums.sort()
        buckets = [0]*k 

        def backtrack(i): 

            if i == len(nums): 
                return True 

            num = nums[i]

            for bucket in range(k): 

                if buckets[bucket] + num > target: 
                    continue 

                buckets[bucket] += num
                if backtrack(i+1): 
                    return True
                buckets[bucket] -= num 

                if buckets[bucket] == 0: 
                    break 

            return False

        return backtrack(0)