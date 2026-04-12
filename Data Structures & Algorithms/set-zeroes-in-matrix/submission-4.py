class Solution:
    def BF(): 
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

    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        first_row = False
        first_col = False

        for j in range(m):
            if matrix[0][j] == 0:
                first_row = True

        for i in range(n):
            if matrix[i][0] == 0:
                first_col = True

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if first_row:
            for j in range(m):
                matrix[0][j] = 0

        if first_col:
            for i in range(n):
                matrix[i][0] = 0