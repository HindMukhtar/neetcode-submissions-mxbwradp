class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergesort(left, right): 

            l = 0 
            r = 0 
            ans = []

            while l < len(left) and r < len(right): 
                if left[l] < right[r]: 
                    ans.append(left[l])
                    l +=1 
                else: 
                    ans.append(right[r])
                    r += 1 

            while l < len(left): 
                ans.append(left[l])
                l += 1 

            while r < len(right): 
                ans.append(right[r])
                r += 1 

            return ans 

        def merge(l, r): 

            if len(nums[l:r]) <= 1: 
                return nums[l:r] 

            mid = (l+r)//2 
            left = merge(l, mid)
            right = merge(mid, r)

            return mergesort(left, right)

        return merge(0, len(nums))