class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        final_list = []

        def dfs(i, value, lst):
            if value == target:
                new_lst = lst.copy()
                if new_lst not in final_list:
                    final_list.append(lst.copy())
            if i >= len(nums) or value > target:
                return 

            lst.append(nums[i])
            dfs(i, value + nums[i], lst)
            lst.pop()
            dfs(i+1, value, lst)

        dfs(0,0,[])
        return final_list