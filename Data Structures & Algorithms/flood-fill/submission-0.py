from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0]) 
        change = image[sr][sc]
        if color == change:
            return image
        queue = deque([(sr, sc)])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            row, col = queue.popleft()
            if image[row][col] == change:
                image[row][col] = color

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r < 0 or c < 0 or r == ROWS or c == COLS or image[r][c] != change: 
                        continue 
                    queue.append((r,c))

        return image