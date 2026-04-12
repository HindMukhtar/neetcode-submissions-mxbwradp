class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        top = 0 
        bottom = n-1
        left = 0 
        right = m-1

        res = []

        while top < bottom and left < right: 
            i, j = top, left
            for j in range(left,right): 
                res.append(matrix[top][j])
            for i in range(top, bottom): 
                res.append(matrix[i][right])
            for j in range(right, left, -1): 
                res.append(matrix[bottom][j])
            for i in range(bottom, top, -1): 
                res.append(matrix[i][left])
            top+=1 
            bottom-=1
            left+=1
            right-=1

        if top == bottom:
            for j in range(left, right + 1):
                res.append(matrix[top][j])

        elif left == right:
            for i in range(top, bottom + 1):
                res.append(matrix[i][left])

        return res 
        
        