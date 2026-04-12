class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        check_row = [False]*n
        check_col = [False]*m

        for i in range(n): 
            for j in range(m): 
                if matrix[i][j] == 0: 
                    check_row[i] = True 
                    check_col[j] = True 

        for i in range(n): 
            for j in range(m): 
                if check_row[i] or check_col[j]: 
                    matrix[i][j] = 0 


        
        