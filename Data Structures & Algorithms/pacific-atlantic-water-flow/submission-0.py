class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()

        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs(r, c, visited, prevHeight):
            
            if r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prevHeight or (r,c) in visited:
                return
            visited.add((r,c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])
        
        ans = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in pac and (i, j) in atl:
                    ans.append([i, j])
        return ans 