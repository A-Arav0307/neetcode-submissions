class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #m is rows and n is cols
        grid = [[0] * (n+1) for _ in range(m+1)]
        for row in range(m):
            grid[row][n-1] = 1

        for row in range(m-1, -1, -1):
            for col in range(n-2, -1, -1):
                grid[row][col] = grid[row+1][col] + grid[row][col+1]

        return grid[0][0]

        
        