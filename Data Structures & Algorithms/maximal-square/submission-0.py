class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        self.max_area = 0
        ROWS, COLS = len(matrix), len(matrix[0]) 
        memo = {}

        #dfs finds longest side length 
        def dfs(r, c):
            if (r, c) in memo: 
                return memo[(r, c)]
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or matrix[r][c] == '0': 
                memo[(r, c)] = 0
                return 0
            
            down, right, diagonal = dfs(r+1, c), dfs(r, c+1), dfs(r+1, c+1)
            if matrix[r][c] == '1':
                max_square = 1 + min(down, right, diagonal)

            self.max_area = max(self.max_area, max_square ** 2)
            memo[(r,c)] = max_square
            return max_square 
        
        for r in range(ROWS): 
            for c in range(COLS):
                dfs(r, c) 
        return self.max_area