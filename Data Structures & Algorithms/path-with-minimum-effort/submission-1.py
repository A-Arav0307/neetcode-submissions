class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        min_effort = 0
        ROWS, COLS = len(heights), len(heights[0])  
        visited = set()
        heap = [ [0, 0, 0] ]
        heapq.heapify(heap) 
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


        while heap:
            diff, row, col = heapq.heappop(heap)
            if (row, col) in visited:
                continue 
            visited.add((row, col))
            if (row, col) == (ROWS-1, COLS-1): 
                return diff
           
            for dr, dc in directions: 
                r, c = row + dr, col + dc
                if r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in visited:
                    continue
                
                new_diff = max(diff, abs(heights[r][c] - heights[row][col]))
                heapq.heappush(heap, [new_diff, r, c])

