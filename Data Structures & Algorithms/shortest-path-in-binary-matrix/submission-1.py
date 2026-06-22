class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        distance = float('inf')
        ROWS, COLS = len(grid)-1, len(grid[0])-1
        if grid[0][0] != 0 or grid[ROWS][COLS] != 0:
            return -1
        visited = set()

        queue = deque( [ [(0,0), 1] ] )
        directions = ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1))

        while queue:
            (row, col), length = queue.popleft()
            visited.add((row, col))
            grid[row][col] = 1
            if (row, col) == (ROWS, COLS):
                distance = min(distance, length) 
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if r < 0 or c < 0 or r == ROWS+1 or c == COLS+1 or grid[r][c] != 0:
                    continue
                queue.append([(r,c), length+1])

            

        if not queue and (ROWS, COLS) not in visited: 
            return -1
        

        return distance
