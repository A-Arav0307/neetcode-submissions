class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        R, C = len(matrix), len(matrix[0]) 

        zero_rows = set() 
        zero_cols = set() 

        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    zero_rows.add(r) 
                    zero_cols.add(c) 
        
        for r in range(R):
            for c in range(C): 
                if r in zero_rows or c in zero_cols: 
                    matrix[r][c] = 0
                    
        
    