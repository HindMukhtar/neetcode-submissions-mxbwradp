class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        # we can get the length of the array 
        # array is 0 indexed 
        # and we can get the value of the array given an idex 

        # need to: return min index ST mountainArr.get(index) = target 
        # if does not exist reutrn -1 

        # approach 
        # we know there is a peak somewhere. Find the peak and seperate the 
        # array into 2. Then we search 0 to peak and peak to end as sorted arrays 

        # example 
        # nums = [2,4,10,1,5], k = 2

        # First find the peak 
        lenght = mountainArr.length() - 1 
        lo = 0 
        hi = lenght

        while lo < hi: 

            mid = (lo+hi)//2 
            val = mountainArr.get(mid)
            nxt = mountainArr.get(mid+1)

            if val > nxt: 
                hi = mid 
            else: 
                lo = mid + 1 

        peak = lo 

        # check left side 
        lo = 0 
        hi = peak 

        while lo <= hi: 

            mid = (lo + hi)//2 
            val = mountainArr.get(mid)

            if val == target: 
                return mid 
            elif val > target: 
                hi = mid - 1 
            else:
                lo = mid + 1 

        # check right side: 
        lo = peak + 1 
        hi = lenght 

        while lo <= hi: 

            mid = (lo + hi)//2 
            val = mountainArr.get(mid)

            if val == target: 
                return mid 
            elif val > target: 
                lo = mid + 1 
            else: 
                hi = mid - 1 

        return -1 

