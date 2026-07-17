class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        ROWS, COLS = len(grid), len(grid[0]) 
        memo = {}

        def dfs(i, j):
            if i == ROWS-1 and j == COLS-1:
                return grid[i][j]
            if i == ROWS or j == COLS:
                return float('inf') 
            if (i, j) in memo: #what is the point of returning so early from here? 
                return memo[(i, j)] 

            down = dfs(i+1, j) 
            right = dfs(i, j+1) 

            memo[(i, j)] = grid[i][j] + min(down, right)


            return memo[(i, j)]

        return dfs(0, 0)