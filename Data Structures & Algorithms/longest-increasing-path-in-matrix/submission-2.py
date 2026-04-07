class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        n = len(matrix)
        m = len(matrix[0])

        def dfs(i, j): 
            if (i,j) in memo: 
                return memo[(i,j)]

            dirs = [(1,0), (-1,0), (0,1), (0,-1)]

            memo[(i,j)] = 1 

            for di, dj in dirs: 
                ni, nj = i+di, j+dj
                if ni >= 0 and nj >= 0 and ni < n and nj < m: 
                    if matrix[ni][nj] > matrix[i][j]: 
                        memo[(i,j)] = max(memo[(i,j)], 1+dfs(ni, nj))

            return memo[(i,j)]

        ans = 0 
        for i in range(n): 
            for j in range(m): 
                ans = max(ans, dfs(i,j))

        return ans 
       