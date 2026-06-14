class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        values = list(range(1, n+1)) 
        final_list = []

        def backtrack(curr, i):
            if len(curr) == k:
                final_list.append(curr.copy())
                return 

            if i >= len(values): 
                return 

            curr.append(values[i])
            backtrack(curr, i+1)
            curr.pop()
            backtrack(curr, i+1)

    
        backtrack([], 0) 
        return final_list 
