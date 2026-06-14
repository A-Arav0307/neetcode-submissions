class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if (
                r < 0 or c < 0 or r == rows or c == columns or grid[r][c] == 0
                
            ):
                return 1

            if (r,c) in visited:
                return 0

            visited.add((r,c))
            perimeter = dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
            
            
            return perimeter

        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == 1:
                    return dfs(row, col)  