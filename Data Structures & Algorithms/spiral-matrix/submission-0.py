class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R, C = len(matrix), len(matrix[0]) 
        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        visited = set()
        spiral = []
        

        while top <= bottom and left <= right:
            row = top
            for col in range(left, right+1):
                if (row, col) in visited:
                    continue
                spiral.append(matrix[row][col])
                visited.add((row, col))
            
            col = right
            for row in range(top, bottom+1):
                if (row, col) in visited:
                    continue
                spiral.append(matrix[row][col])
                visited.add((row, col))
               

            row = bottom
            for col in range(right, left-1, -1): 
                if (row, col) in visited:
                    continue
                spiral.append(matrix[row][col])
                visited.add((row, col))
                

            col = left
            for row in range(bottom, top-1, -1):
                if (row, col) in visited:
                    continue
                spiral.append(matrix[row][col])
                visited.add((row, col))
                

            top += 1
            right -= 1
            bottom -= 1
            left += 1

        return spiral 