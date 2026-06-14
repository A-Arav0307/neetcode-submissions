class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        memo = {}
        
        def dfs(r, c):
            if (r,c) in memo: 
                return memo[(r,c)]

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            best = 1

            for dr, dc in directions: 
                nr, nc = r + dr, c + dc

                if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS 
                or matrix[nr][nc] <= matrix[r][c]):
                    continue
        
                best = max(best, 1 + dfs(nr, nc))

            memo[(r,c)] = best
            return memo[(r,c)]
            
        res = float('-inf')
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c))

        return res