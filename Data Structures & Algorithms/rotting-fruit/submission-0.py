class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        ROWS, COLUMNS = len(grid), len(grid[0])
        fresh = 0
        time = 0
        queue = deque()

        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        #multi-path bfs

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r<0 or r==ROWS or c<0 or c==COLUMNS or grid[r][c]!=1):
                        continue
                    if grid[r][c] == 1:
                        queue.append((r,c))
                        grid[r][c] = 2
                        fresh -= 1

            time += 1

        return time-1 if fresh == 0 else -1
                    