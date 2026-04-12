class Solution:
    def BF(): 
        res = 1
        pwr = abs(n)

        while pwr > 0: 
            res*=x 
            pwr-=1 

        return res if n>0 else (1/res)

    def myPow(self, x: float, n: int) -> float:
        def fast_pow(x, y):
            if y == 0: 
                return 1 
            if y >= 1: 
                ans = fast_pow(x, y//2)
                if y%2 == 0: 
                    return ans*ans
                else: 
                    return ans*ans*x 
        
        pwr = abs(n)
        res = fast_pow(x, pwr)

        return res if n>0 else (1/res)