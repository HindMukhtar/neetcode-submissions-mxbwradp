class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False 
        rows = len(board)
        cols = len(board[0])
        visited = [[False]*cols for _ in range(rows)]

        def dfs(k, i,j): 

            if i<0 or j<0 or i>=rows or j>=cols: 
                return False 

            if visited[i][j]: 
                return False

            if board[i][j] != word[k]: 
                return False 

            if k == len(word)-1: 
                return True 

            visited[i][j] = True 
            
            found = dfs(k+1, i-1, j) or dfs(k+1, i+1, j) or dfs(k+1, i, j-1) or dfs(k+1, i, j+1)

            visited[i][j] = False 

            return found 

        for i in range(rows): 
            for j in range(cols): 
                if dfs(0, i, j):
                    return True 

        return res 
   