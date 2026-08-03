class Solution:
    def solve(self, board: List[List[str]]) -> None:
        border = set()
        ROWS, COLS = len(board), len(board[0])
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    if r == 0 or c == 0 or r == ROWS-1 or c == COLS-1:
                        border.add((r,c))
                        board[r][c] = 'S'

        def dfs(r,c):
            if r<0 or c<0 or r==ROWS or c==COLS or board[r][c] != 'O':
                return
            board[r][c] = 'S'

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for row, col in border:
            dfs(row, col)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'

    