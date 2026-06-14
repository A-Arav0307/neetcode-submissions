class Solution:
    def partition(self, s: str) -> List[List[str]]:
        final_list = []
        curr = []

        def valid(word):
            start, end = 0, len(word) - 1
            while start < end:
                if word[start] != word[end]:
                    return False
                start += 1
                end -= 1

            return True 
        
        def dfs(i):
            if i == len(s): 
                final_list.append(curr.copy())
                return 
            
            for j in range(i, len(s)):
                word = s[i:j+1]
                if valid(word):
                    curr.append(word)
                    dfs(j+1)
                    curr.pop()

        dfs(0)
        return final_list