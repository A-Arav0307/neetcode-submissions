class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        final_list = []
        lst = range(1,n+1)

        def dfs(i, cur):
            if len(cur) == k:
                final_list.append(cur.copy())
                return

            if i >= n:
                return 

            cur.append(lst[i])
            dfs(i+1, cur)
            cur.pop()
            dfs(i+1, cur)



        dfs(0, [])
        return final_list
