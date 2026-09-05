class Solution:
    def totalNQueens(self, n: int) -> int:

        cols = set() 
        pos_diagonals = set() 
        neg_diagonals = set() 
        solutions = 0 
        
        def backtrack(i): 
            nonlocal solutions

            if i == n: 
                solutions += 1 
                return 

            for j in range(n):
                if j not in cols and (i+j) not in pos_diagonals and (i-j) not in neg_diagonals: 
                    cols.add(j)
                    pos_diagonals.add(i+j)
                    neg_diagonals.add(i-j)
                    backtrack(i+1)
                    cols.remove(j)
                    pos_diagonals.remove(i+j)
                    neg_diagonals.remove(i-j)

        backtrack(0)

        return solutions 