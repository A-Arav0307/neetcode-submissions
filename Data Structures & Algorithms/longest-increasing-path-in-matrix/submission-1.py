class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        memo = {}
        
        def dfs(r, c, prevVal):
            if (r < 0 or c < 0 or r == ROWS or c == COLS 
            or matrix[r][c] <= prevVal):
                return 0

            if (r,c) in memo: 
                return memo[(r,c)]
            
            left = 1 + dfs(r, c-1, matrix[r][c])
            right = 1 + dfs(r, c+1, matrix[r][c])
            down = 1 + dfs(r-1, c, matrix[r][c])
            up = 1 + dfs(r+1, c, matrix[r][c])

        
            memo[(r,c)] = max(left, right, up, down)
            

            return memo[(r,c)]
            
        res = float('-inf')
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c, float('-inf')))

        return res