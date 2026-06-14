class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque 
        queue = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        for row in range(ROWS):
            for col in range(COLS): 
                if grid[row][col] == 0:
                    queue.append((row, col))
                    visited.add((row, col))
         

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
     
        while queue: 
            r, c = queue.popleft()
            for dr, dc in directions:
                if (r + dr) < 0 or (r + dr) == ROWS or (c + dc) < 0 or (c + dc) == COLS  or grid[r + dr][c + dc] == -1 or (r+dr, c +dc) in visited:
                    continue 
                
                visited.add((r+dr, c+dc))
                grid[r + dr][c + dc] = min(grid[r+dr][c+dc], 1 + grid[r][c])
                queue.append((r+dr, c+dc))

