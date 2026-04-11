class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix) 
        i = 0 
        j = n-1 
        
        # Reverse matrix vertically 
        while i < j: 
            matrix[i], matrix[j] = matrix[j], matrix[i]
            i+=1 
            j-=1

        for i in range(n): 
            for j in range(i, n): 
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]