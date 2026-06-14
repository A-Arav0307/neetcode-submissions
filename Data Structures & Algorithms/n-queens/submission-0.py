class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # (r+c)
        negDiag = set() # (r-c)
        board = [['.'] * n for i in range(n)]
        print(board)
        res = []

        def backtrack(r):
            if r == n:
                copy = []
                for row in board:
                    copy.append(''.join(row))
                res.append(copy)
                return 

            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                
                board[r][c] = 'Q'
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)

                backtrack(r+1)

                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = '.'

        backtrack(0)
        return res
      