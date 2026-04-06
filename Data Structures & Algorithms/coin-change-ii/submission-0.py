class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        n = len(coins)

        def dfs(i, target): 

            if (i, target) in memo: 
                return memo[(i, target)]
            if target == amount: 
                return 1 
            if target > amount or i >=n : 
                return 0 

            memo[(i, target)] = 0 

            for c in range(i, n): 
                memo[(i, target)] += dfs(c, target+coins[c])

            return memo[(i, target)]

        return dfs(0,0)
            
        