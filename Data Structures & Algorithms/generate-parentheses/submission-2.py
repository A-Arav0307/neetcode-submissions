class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final_list = []

        def dfs(curr, left, right):
            if left > n or right > n: 
                return 
            
            if right > left: 
                return

            if left == n and right == n:
                final_list.append(curr)
                return 

            curr = curr + '('
            dfs(curr, left + 1, right)
            curr = curr[:-1]
            curr = curr + ')'
            dfs(curr, left, right + 1)

        dfs("", 0, 0)
        return final_list