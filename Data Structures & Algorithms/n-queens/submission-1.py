class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        rows = n 
        cols = n 
        board = [['.']*cols for _ in range(rows)]
        used_cols = set()
        used_diags = set() 
        used_anti_diags = set()
        res = []

        def dfs(i): 
            if i == n: 
                res.append(["".join(row) for row in board])
                return 

            for j in range(cols): 
                if j not in used_cols and (i-j) not in used_diags and (i+j) not in used_anti_diags: 
                    board[i][j] = 'Q'
                    used_cols.add(j)
                    used_diags.add(i-j)
                    used_anti_diags.add(i+j)
                    dfs(i+1)
                    board[i][j] = '.'
                    used_cols.remove(j)
                    used_diags.remove(i-j)
                    used_anti_diags.remove(i+j)

        dfs(0)
        return res 
