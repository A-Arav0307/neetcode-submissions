class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        R, C = len(matrix), len(matrix[0]) 

        zeroes = set()

        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    zeroes.add((r, c)) 

        for r in range(R):
            for c in range(C):
                if (r, c) in zeroes: 
                    row = r
                    for i in range(0, C):
                        matrix[row][i] = 0
                    
                    col = c
                    for j in range(0, R): 
                        matrix[j][col] = 0

                    
        
    