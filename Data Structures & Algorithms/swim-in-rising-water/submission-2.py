class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        time = float('-inf') 
        n = len(grid)
        heap = [ [0,  (0,0)] ]
        heapq.heapify(heap)
        visited = set()

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        while heap:
            cost, (row, col) = heapq.heappop(heap)
            if (row, col) in visited:
                continue
            time = max(time, grid[row][col])
            if (row, col) == (n-1, n-1): 
                return time
            visited.add((row, col)) 
            
            for dr, dc in directions:
                r, c = row+dr, col+dc
                if r<0 or c<0 or r == n or c == n or (r, c) in visited:
                    continue
                heapq.heappush(heap, [max(time, grid[r][c]), (r, c)])

        return -1      