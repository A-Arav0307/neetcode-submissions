class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            count = {}
            for col in range(len(board)):
                if board[row][col] not in count and board[row][col] != '.': 
                    count[board[row][col]] = 1
                if board[row][col] in count:
                    return False
                if board[row][col] == '.':
                    continue

        return True

                