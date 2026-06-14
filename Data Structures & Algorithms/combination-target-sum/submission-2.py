class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        final_list = []

        def backtrack(i, curr, total):
            if total > target:
                return 
            if i >= len(nums): 
                return 

            if total == target: 
                final_list.append(curr.copy())
                return 

            curr.append(nums[i])
            backtrack(i, curr, total + nums[i])
            curr.pop()
            backtrack(i+1, curr, total)

        backtrack(0, [], 0) 

        return final_list