class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = {}
        def dfs(i, j):
            if i == ROWS or j == COLS or obstacleGrid[i][j] == 1:
                return 0
            if i == ROWS - 1 and j == COLS - 1:
                return 1

            if (i, j) in dp:
                return dp[(i, j)]

            down = dfs(i+1, j) 
            right = dfs(i, j+1) 

            dp[(i,j)] = down + right
            return dp[(i, j)]

        return dfs(0, 0)


