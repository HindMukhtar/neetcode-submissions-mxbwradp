class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        safe = [[False]*cols for _ in range(rows)]

        queue = deque()

        # Find all Os in the boarder 

        for i in range(rows): 
            if board[i][0] == 'O':
                safe[i][0] = True
                queue.append((i,0))
            if board[i][cols-1] == 'O':
                safe[i][cols-1] = True
                queue.append((i,cols-1))

        for j in range(1, cols-1): 
            if board[0][j] == 'O': 
                safe[0][j] = True
                queue.append((0, j))
            if board[rows-1][j] == 'O':
                safe[rows-1][j] = True
                queue.append((rows-1, j))

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue: 
            i, j = queue.popleft()
            for di, dj in dirs: 
                ni, nj = i+di, j+dj
                if (0<=ni<rows) and (0<=nj<cols):
                    if board[ni][nj] == 'O' and not safe[ni][nj]: 
                        safe[ni][nj] = True 
                        queue.append((ni,nj))

        for i in range(rows): 
            for j in range(cols): 
                if board[i][j] == 'O' and not safe[i][j]: 
                    board[i][j] = 'X'

