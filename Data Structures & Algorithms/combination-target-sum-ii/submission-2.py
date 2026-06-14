class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        final_list = []
        candidates.sort()

        def dfs(cur, i, total):
            
            if total == target:
                final_list.append(cur.copy())
                return

            if total > target:
                return 
            
            if i >= len(candidates):
                return 
                  
            cur.append(candidates[i])
            dfs(cur, i+1, total + candidates[i])
            cur.pop()
            num_to_skip = candidates[i]
            while i < len(candidates) and candidates[i] == num_to_skip:
                i += 1
            dfs(cur, i, total)

        dfs([], 0, 0)
        return final_list