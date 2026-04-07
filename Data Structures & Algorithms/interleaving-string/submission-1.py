class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        n = len(s1)
        m = len(s2)

        if len(s1) + len(s2) != len(s3): 
            return False 

        def dfs(i, j):

            if (i,j) in memo: 
                return memo[(i,j)]
            if i+j == len(s3): 
                return True 

            if i < n and s1[i] == s3[i+j]: 
                try_s1 = dfs(i+1,j)
            else: 
                try_s1 = False 
            if j < m and s2[j] == s3[i+j]: 
                try_s2 = dfs(i, j+1)
            else: 
                try_s2 = False 

            memo[(i,j)] = try_s1 or try_s2 

            return memo[(i,j)]

        return dfs(0,0)