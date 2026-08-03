class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        R, C = len(matrix), len(matrix[0]) 

        for r in range(R):
            for c in range(C): 
                if matrix[r][c] == float('inf'):
                    continue
                
                if matrix[r][c] == 0:
                    if c < right:
                        for col in range(c+1, right+1):
                            matrix[r][col] = float('inf') 
                    if c > left:
                        for col in range(c-1, left-1, -1):
                            matrix[r][col] = float('inf') 

                    if r < bottom: 
                        for row in range(r+1, bottom+1):
                            matrix[row][c] = float('inf') 

                    if r > top: 
                        for row in range(r-1, top-1, -1):
                            matrix[row][c] = float('inf') 

        for r in range(R):
            for c in range(C):
                if matrix[r][c] == float('inf'):
                    matrix[r][c] = 0


        
    