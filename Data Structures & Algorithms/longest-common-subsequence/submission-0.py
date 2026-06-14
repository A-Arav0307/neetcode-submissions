class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [[0 for _ in range(len(text1)+1)] for __ in range(len(text2)+1)]
        ROWS, COLS = len(grid), len(grid[0])
        #text2 is row and text1 is column
        for row in range(ROWS-2, -1, -1):
            for col in range(COLS-2, -1, -1):
                if text2[row] == text1[col]:
                    grid[row][col] = 1 + grid[row+1][col+1]

                else:
                    grid[row][col] = max(grid[row+1][col], grid[row][col+1])

        return grid[0][0]