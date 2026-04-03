class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        lo, hi = 0, row*col - 1 

        while lo <= hi: 
            mid = lo + (hi-lo)//2 
            r,c = divmod(mid, col)

            if matrix[r][c] == target: 
                return True
            elif matrix[r][c] < target: 
                lo=mid+1 
            else: 
                hi=mid-1

        return False 