class Solution:
    def mySqrt(self, x: int) -> int:

        lo = 0 
        hi = x 

        while lo < hi: 

            mid = (lo+hi+1)//2 

            sqrt = mid*mid

            if sqrt <= x: 
                lo = mid
            else:
                hi = mid - 1 

        return lo 