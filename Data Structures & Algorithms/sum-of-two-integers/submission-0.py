class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0 
        for i in range(32): 
            x = (a>>i)&1 
            y = (b>>i)&1 
            bit = x^y^carry 
            carry = (x&y)|(x&carry)|(y&carry)
            res |= (bit << i)

        # handle Python signed integer behavior
        if res >= (1 << 31):
            res -= (1 << 32)

        return res
