class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9 
        seen_row = defaultdict(set)
        seen_col = defaultdict(set)
        seen_box = defaultdict(set)
        for i in range(n): 
            for j in range(n): 
                val = board[i][j]
                if val != '.': 
                    if val in seen_row.get(i, ''): 
                        return False 
                    if val in seen_col.get(j, ''): 
                        return False
                    sb =  (i//3) * 3 + (j//3)
                    if val in seen_box.get(sb, ''): 
                        return False 
                    # Otherwise let's add them 
                    seen_row[i].add(val)
                    seen_col[j].add(val)
                    seen_box[sb].add(val)
        return True 
