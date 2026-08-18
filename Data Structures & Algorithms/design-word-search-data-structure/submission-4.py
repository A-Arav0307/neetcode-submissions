class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]
        curr.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(node, index):
            if node.endOfWord and index == len(word):
                return True 
            if index == len(word) and not node.endOfWord:
                return False

            if word[index] == '.':
                for child in node.children.values(): 
                    if dfs(child, index+1): 
                        return True 


            if word[index] not in node.children:
                return False 


            if word[index] in node.children:
                if dfs(node.children[word[index]], index+1):
                    return True

            return False

        return dfs(self.root, 0)


