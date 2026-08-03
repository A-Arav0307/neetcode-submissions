class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        final_list = []

        def dfs(cur, i, total):
            
            if total == target:
                new_list = cur.copy()
                if new_list not in final_list:
                    final_list.append(new_list)
                return

            if total > target:
                return 
            
            if i >= len(candidates):
                return 

            cur.append(candidates[i])
            dfs(cur, i+1, total + candidates[i])
            cur.pop()
            dfs(cur, i+1, total) 

        dfs([], 0, 0)
        return final_list