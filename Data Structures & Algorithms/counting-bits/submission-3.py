class Solution:
    def BF(): 
        res = []
        ans = 0 

        for i in range(n+1): 
            ans = 0 
            for j in range(0, i+1): 
                if (1<<j)&i: 
                    ans+=1 
            res.append(ans)

        return res 

    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)

        for i in range(0,n+1): 
            res[i] = res[i >> 1] + (i & 1)

        return res 
            
        