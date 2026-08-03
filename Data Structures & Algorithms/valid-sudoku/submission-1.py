class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows
        for row in range(len(board)):
            rows = {}
            for column in range(len(board[row])):
                if board[row][column] == '.':
                    continue
                if board[row][column] in rows:
                    return False
                rows[board[row][column]] = 1

        #check columns
        i = 0
        while i < 9:
            for row in range(len(board)):
                columns = {}
                if board[row][i] in columns: 
                    return False 
                columns[board[row][i]] = 1
                i += 1 

        #check squares
        squares = {}
        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] == '.': 
                    continue
                square_key = (row // 3, column // 3)
                if square_key not in squares:
                    squares[square_key] = set()
                if board[row][column] in squares[square_key]: 
                    return False 
                squares[square_key].add(board[row][column])

        return True
