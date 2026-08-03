class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        solution = set()

        def backtrack(word, r, c, i, visited):
            if (
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r, c) in visited or
                board[r][c] != word[i]
            ):
                return

            # If this is the last character and it matches, we found the word
            if i == len(word) - 1:
                solution.add(word)
                return

            visited.add((r, c))

            backtrack(word, r + 1, c, i + 1, visited)
            backtrack(word, r - 1, c, i + 1, visited)
            backtrack(word, r, c + 1, i + 1, visited)
            backtrack(word, r, c - 1, i + 1, visited)

            visited.remove((r, c))

        for word in words:
            for r in range(ROWS):
                for c in range(COLS):
                    backtrack(word, r, c, 0, set())

        return list(solution)