class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:

        def getprime(num): 
            factors = set() 

            # get even factors 
            d = 2
            while num%d == 0: 
                factors.add(d)
                num//=d 

            # get odd factors 
            d = 3 
            while d*d <= num: 
                while num%d==0: 
                    factors.add(d)
                    num//=d
                d+=2 

            if num > 1: 
                factors.add(num)

            return factors 

        parents = {i:i for i in range(len(nums))}
        rank = [1]*len(nums)

        def find(x): 
            if parents[x]!=x: 
                parents[x] = find(parents[x])
            return parents[x]

        def union(x,y): 

            parent_x = find(x)
            parent_y = find(y)

            if parent_x == parent_y: 
                return False 

            if rank[parent_x] > rank[parent_y]: 
                parents[parent_y] = parent_x
                rank[parent_x]+=1 
            else: 
                parents[parent_x] = parent_y
                rank[parent_y]+=1 

            return True 

        factor_owner = {}
        for i, n in enumerate(nums): 
            factors = getprime(n)

            for f in factors: 
                if f in factor_owner: 
                    union(i, factor_owner[f])
                else: 
                    factor_owner[f] = i 

        root = find(0)

        for i in range(len(nums)): 
            if find(i) != root: 
                return False 

        return True 


        
