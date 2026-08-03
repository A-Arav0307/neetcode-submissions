class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set() 
        solution = []

        def backtrack(word, r, c, i):
            if (r, c) in visited or r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != word[i]:
                return
            if i == len(word)-1: 
                solution.append(word[:])
                i = 0
                return 
            
            visited.add((r,c))
            backtrack(word, r + 1, c, i+1)
            backtrack(word, r - 1, c, i+1)
            backtrack(word, r, c + 1, i+1)
            backtrack(word, r, c - 1, i+1)

            visited.remove((r,c))

        for word in words:
            for r in range(ROWS):
                for c in range(COLS):
                    backtrack(word, r, c, 0)

        return solution 


        


        