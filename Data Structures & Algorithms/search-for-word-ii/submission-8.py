class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word): 
        curr = self 
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node() 
            curr = curr.children[char]

        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        root = Node()
        self.result = set()
        visited = set()
        for word in words: 
            root.addWord(word)

        def dfs(r, c, node, word): 
            if (r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visited or board[r][c] not in node.children ): 
                return

            char = board[r][c]
            node = node.children[char]
            word = word + char
            if node.endOfWord:
                self.result.add(word)

            visited.add((r,c))
            dfs(r+1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c-1, node, word)


            visited.remove((r,c))
            
        for r in range(ROWS):
            for c in range(COLS): 
                dfs(r, c, root, "")

        return list(self.result)
        
        