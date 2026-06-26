class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # nums[a] + nums[b] + nums[c] + nums[d] = target 
        # so if we set a then: 
        # nums[b] + nums[c] + nums[d] = target - nums[a]
        # then we set b then 
        # numc[c] + nums[d] = target - nums[a] - nums[b]
        # this becomes a 2 sum problem 

        # first sort the array -> O(nlogn)
        # [3,2,3,-3,1,0]
        # [-3,0,1,2,3,3]
        # we want nums[b] + nums[c] = target value. Array is sorted 
        # so we can use 2 pointers. if nums[b] + nums[c] < target then increment 
        # left counter, otherwise decrement right counter 

        nums.sort() 
        ans = []
        for i in range(len(nums)): 

            if i > 0 and nums[i] == nums[i-1]:
                continue 
            a = nums[i]

            for j in range(i+1, len(nums)): 
                
                if j > i + 1 and nums[j] == nums[j-1]: 
                    continue 
                b = nums[j]

                l = j + 1 
                r = len(nums) - 1 
                
                while l < r: 

                    S = a + b + nums[l] + nums[r]

                    if S == target: 
                        ans.append([a, b, nums[l], nums[r]])
                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l-1]: 
                            l += 1 
                        while r > l and nums[r] == nums[r+1]: 
                            r -= 1

                    elif S < target: 
                        l += 1 
                    else: 
                        r -= 1 

        return ans 